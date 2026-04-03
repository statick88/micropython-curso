"""
Mock machine module for testing ESP-LEGO-SPIKE-Simulator.
Provides simulated hardware access without actual microcontroller.
"""


class Pin:
    """Mock Pin class for GPIO simulation."""

    # Pin modes
    IN = "in"
    OUT = "out"
    OPEN_DRAIN = "open_drain"

    # Pull modes
    PULL_UP = "pull_up"
    PULL_DOWN = "pull_down"
    PULL_NONE = "pull_none"

    # Pin states
    LOW = 0
    HIGH = 1

    def __init__(self, pin_id, mode=None, pull=None):
        """Initialize mock Pin.

        Args:
            pin_id: GPIO pin number
            mode: Pin mode (IN, OUT, OPEN_DRAIN)
            pull: Pull mode (PULL_UP, PULL_DOWN, PULL_NONE)
        """
        self.pin_id = pin_id
        self.mode = mode
        self.pull = pull
        self._value = 0
        self._callbacks = []

    def value(self, val=None):
        """Get or set pin value.

        Args:
            val: Optional value to set (0 or 1)

        Returns:
            Current pin value if val is None
        """
        if val is not None:
            self._value = val & 1
            # Notify callbacks
            for callback in self._callbacks:
                callback(self._value)
            return None
        return self._value

    def __call__(self, val=None):
        """Call the pin to set its value (MicroPython compatibility).

        Args:
            val: Optional value to set (0 or 1)

        Returns:
            Current pin value if val is None
        """
        return self.value(val)

    def on(self):
        """Set pin high."""
        self.value(1)

    def off(self):
        """Set pin low."""
        self.value(0)

    def irq(self, handler=None, trigger=None):
        """Configure interrupt handler.

        Args:
            handler: Callback function
            trigger: Trigger mode (IRQ_RISING, IRQ_FALLING, IRQ_ANY)
        """
        if handler:
            self._callbacks.append(handler)

    def __repr__(self):
        return f"<Pin(pin_id={self.pin_id}, mode={self.mode}, value={self._value})>"


class PWM:
    """Mock PWM class for pulse-width modulation simulation."""

    def __init__(self, pin, freq=0, duty=0):
        """Initialize mock PWM.

        Args:
            pin: Pin object or pin number
            freq: Initial frequency in Hz
            duty: Initial duty cycle (0-1023)
        """
        self.pin = pin if isinstance(pin, Pin) else Pin(pin)
        self._freq = freq
        self._duty = duty

    def init(self, freq=None, duty=None):
        """Initialize or reconfigure the PWM.

        Args:
            freq: Optional frequency to set in Hz
            duty: Optional duty cycle to set (0-1023)
        """
        if freq is not None:
            self._freq = freq
        if duty is not None:
            self._duty = duty & 0x3FF  # Clamp to 10-bit

    def deinit(self):
        """Deinitialize the PWM."""
        self._freq = 0
        self._duty = 0

    def freq(self, freq=None):
        """Get or set PWM frequency.

        Args:
            freq: Optional frequency to set in Hz

        Returns:
            Current frequency if freq is None
        """
        if freq is not None:
            self._freq = freq
            return None
        return self._freq

    def duty(self, duty=None):
        """Get or set PWM duty cycle.

        Args:
            duty: Optional duty cycle to set (0-1023)

        Returns:
            Current duty cycle if duty is None
        """
        if duty is not None:
            self._duty = duty & 0x3FF  # Clamp to 10-bit
            return None
        return self._duty

    def __repr__(self):
        return f"<PWM(pin={self.pin.pin_id}, freq={self._freq}, duty={self._duty})>"


class ADC:
    """Mock ADC class for analog-to-digital conversion."""

    # ADC attenuation constants (ESP32-like)
    ATTN_0DB = 0
    ATTN_2_5DB = 1
    ATTN_6DB = 2
    ATTN_11DB = 3

    def __init__(self, pin):
        """Initialize mock ADC.

        Args:
            pin: Pin object or pin number
        """
        self.pin = pin if isinstance(pin, Pin) else Pin(pin)
        self._value = 0
        self._atten = 0  # Attenuation

    def atten(self, atten):
        """Set ADC attenuation.

        Args:
            atten: Attenuation level (ATTN_0DB, ATTN_2_5DB, ATTN_6DB, ATTN_11DB)
        """
        self._atten = atten

    def read_u16(self):
        """Read ADC value as 16-bit unsigned integer.

        Returns:
            ADC value (0-65535)
        """
        return self._value << 8  # Scale to 16-bit

    def read(self):
        """Read ADC value as 12-bit unsigned integer.

        Returns:
            ADC value (0-4095)
        """
        return self._value

    def value(self, val=None):
        """Get or set simulated ADC value.

        Args:
            val: Optional value to set

        Returns:
            Current ADC value
        """
        if val is not None:
            self._value = val & 0xFFF  # 12-bit
            return None
        return self._value

    def __repr__(self):
        return f"<ADC(pin={self.pin.pin_id}, value={self._value})>"


class Signal:
    """Mock Signal class for LED/sensor control."""

    def __init__(self, pin, invert=False):
        """Initialize mock Signal.

        Args:
            pin: Pin object or pin number
            invert: Invert signal logic
        """
        self.pin = pin if isinstance(pin, Pin) else Pin(pin)
        self.invert = invert

    def on(self):
        """Turn signal on."""
        self.pin.value(0 if self.invert else 1)

    def off(self):
        """Turn signal off."""
        self.pin.value(1 if self.invert else 0)

    def value(self, val=None):
        """Get or set signal value."""
        if val is not None:
            self.pin.value(0 if (val ^ self.invert) else 1)
            return None
        return self.pin.value() ^ self.invert


class SoftI2C:
    """Mock SoftI2C class for software I2C simulation."""

    # Class-level device registry (shared across all instances)
    _devices = {}
    _initialized = False

    def __init__(self, sda, scl, freq=400000):
        """Initialize mock SoftI2C.

        Args:
            sda: SDA pin
            scl: SCL pin
            freq: I2C frequency
        """
        self.sda = sda if isinstance(sda, Pin) else Pin(sda)
        self.scl = scl if isinstance(scl, Pin) else Pin(scl)
        self.freq = freq

        # Always ensure TCS34725 device is registered
        self._ensure_tcs34725_device()

        # Link instance to class devices
        self._devices = SoftI2C._devices

    def _ensure_tcs34725_device(self):
        """Ensure TCS34725 device is registered in class registry."""
        if 0x29 not in SoftI2C._devices:

            def tcs34725_read(nbytes):
                """Mock TCS34725 read callback - returns RGB and clear values."""
                return bytes([50, 100, 75, 200])  # R, G, B, Clear

            def tcs34725_writeto_mem(memaddr, data):
                """Mock TCS34725 write to memory."""
                pass

            def tcs34725_readfrom_mem(memaddr, nbytes):
                """Mock TCS34725 read from memory."""
                # Remove COMMAND_BIT if set (0x80) - TCS34725 uses this for auto-increment
                register = memaddr & 0x7F
                # Return appropriate values based on register address
                # Handle both with and without COMMAND_BIT
                if register == 0x12:  # Sensor ID register (SENSORID)
                    return bytes([0x44])  # Valid sensor ID
                elif register == 0x13:  # Status register
                    return bytes([0x01])  # Valid status
                elif register == 0x14:  # CDATAL (clear data low)
                    return bytes([0xC8, 0x00])  # Clear data low
                elif register == 0x16:  # RDATAL (red data low)
                    return bytes([0x32, 0x00])  # Red data low
                elif register == 0x18:  # GDATAL (green data low)
                    return bytes([0x64, 0x00])  # Green data low
                elif register == 0x1A:  # BDATAL (blue data low)
                    return bytes([0x4B, 0x00])  # Blue data low
                elif register == 0x01:  # ATIME (integration time)
                    return bytes([0x00])  # Integration time
                elif register == 0x00:  # ENABLE
                    return bytes([0x03])  # Enable register
                elif register == 0x0F:  # CONTROL
                    return bytes([0x00])  # Control register (gain)
                return bytes(nbytes)

            # Set up mock I2C for TCS34725
            SoftI2C._devices[0x29] = {  # TCS34725 address
                "read": tcs34725_read,
                "write": lambda b: None,
                "writeto_mem": tcs34725_writeto_mem,
                "readfrom_mem": tcs34725_readfrom_mem,
            }

        # Also ensure MPU6050 device is registered (address 0x68)
        if 0x68 not in SoftI2C._devices:

            def mpu6050_read(nbytes):
                """Mock MPU6050 read callback."""
                return bytes(nbytes)  # Return empty bytes with correct length

            def mpu6050_readfrom_mem(memaddr, nbytes):
                """Mock MPU6050 read from memory."""
                register = memaddr & 0x7F
                # Return mock data for common registers (14 bytes needed for get_raw_values)
                if register == 0x3B:  # ACCEL_XOUT_H - need 14 bytes starting from here
                    # Return 14 bytes: Accel X, Y, Z, Temp, Gyro X, Y, Z
                    return bytes(
                        [
                            0,
                            0,  # Accel X (low, high)
                            0,
                            0,  # Accel Y (low, high)
                            64,
                            0,  # Accel Z (low, high) - ~1g
                            50,
                            0,  # Temperature (low, high)
                            0,
                            0,  # Gyro X (low, high)
                            0,
                            0,  # Gyro Y (low, high)
                            0,
                            0,  # Gyro Z (low, high)
                        ]
                    )
                elif register == 0x68:  # WHO_AM_I
                    return bytes([0x68])  # MPU6050 ID
                elif register == 0x3A:  # INT_STATUS
                    return bytes([0x01])  # Data ready
                return bytes(14)  # Default to 14 bytes for raw values read

            def mpu6050_writeto_mem(memaddr, data):
                """Mock MPU6050 write to memory."""
                pass

            SoftI2C._devices[0x68] = {  # MPU6050 address
                "read": mpu6050_read,
                "write": lambda b: None,
                "writeto_mem": mpu6050_writeto_mem,
                "readfrom_mem": mpu6050_readfrom_mem,
            }

    def start(self):
        """Mock start method for MicroPython compatibility."""
        pass

    def stop(self):
        """Mock stop method for MicroPython compatibility."""
        pass

    def _setup_default_devices(self):
        """Set up default I2C devices for testing."""

        def tcs34725_read(nbytes):
            """Mock TCS34725 read callback - returns RGB and clear values."""
            return bytes([50, 100, 75, 200])  # R, G, B, Clear

        def tcs34725_writeto_mem(memaddr, data):
            """Mock TCS34725 write to memory."""
            pass

        def tcs34725_readfrom_mem(memaddr, nbytes):
            """Mock TCS34725 read from memory."""
            # Return appropriate values based on register address
            if memaddr == 0x12:  # Sensor ID register
                return bytes([0x44])  # Valid sensor ID
            elif memaddr == 0x13:  # Status register
                return bytes([0x01])  # Valid status
            elif memaddr == 0x14:  # CDATAL
                return bytes([0xC8, 0x00])  # Clear data low
            elif memaddr == 0x16:  # RDATAL
                return bytes([0x32, 0x00])  # Red data low
            elif memaddr == 0x18:  # GDATAL
                return bytes([0x64, 0x00])  # Green data low
            elif memaddr == 0x1A:  # BDATAL
                return bytes([0x4B, 0x00])  # Blue data low
            elif memaddr == 0x01:  # ATIME
                return bytes([0x00])  # Integration time
            elif memaddr == 0x00:  # ENABLE
                return bytes([0x03])  # Enable register
            elif memaddr == 0x0F:  # CONTROL
                return bytes([0x00])  # Control register (gain)
            return bytes(nbytes)

        # Set up mock I2C for TCS34725
        SoftI2C._devices[0x29] = {  # TCS34725 address
            "read": tcs34725_read,
            "write": lambda b: None,
            "writeto_mem": tcs34725_writeto_mem,
            "readfrom_mem": tcs34725_readfrom_mem,
        }

    def scan(self):
        """Scan for I2C devices.

        Returns:
            List of device addresses
        """
        return list(self._devices.keys())

    def writeto(self, addr, buf, stop=True):
        """Write data to I2C device.

        Args:
            addr: Device address
            buf: Data to write
            stop: Send stop bit
        """
        if addr in self._devices:
            self._devices[addr]["write"](buf)

    def readfrom(self, addr, nbytes, stop=True):
        """Read data from I2C device.

        Args:
            addr: Device address
            nbytes: Number of bytes to read
            stop: Send stop bit

        Returns:
            Bytes read
        """
        if addr in self._devices:
            return self._devices[addr]["read"](nbytes)
        return bytes(nbytes)

    def writeto_mem(self, addr, memaddr, data, stop=True):
        """Write data to I2C device memory.

        Args:
            addr: Device address
            memaddr: Memory address
            data: Data to write
            stop: Send stop bit
        """
        if addr in self._devices and "writeto_mem" in self._devices[addr]:
            self._devices[addr]["writeto_mem"](memaddr, data)

    def readfrom_mem(self, addr, memaddr, nbytes=1, stop=True):
        """Read data from I2C device memory.

        Args:
            addr: Device address
            memaddr: Memory address
            nbytes: Number of bytes to read
            stop: Send stop bit

        Returns:
            Bytes read
        """
        if addr in self._devices and "readfrom_mem" in self._devices[addr]:
            return self._devices[addr]["readfrom_mem"](memaddr, nbytes)
        return bytes(nbytes)

    def register_device(
        self,
        addr,
        read_cb=None,
        write_cb=None,
        writeto_mem_cb=None,
        readfrom_mem_cb=None,
    ):
        """Register mock I2C device.

        Args:
            addr: Device address
            read_cb: Read callback function
            write_cb: Write callback function
            writeto_mem_cb: Write to memory callback
            readfrom_mem_cb: Read from memory callback
        """
        self._devices[addr] = {
            "read": read_cb or (lambda n: bytes(n)),
            "write": write_cb or (lambda b: None),
            "writeto_mem": writeto_mem_cb or (lambda m, d: None),
            "readfrom_mem": readfrom_mem_cb or (lambda m, n: bytes(n)),
        }

    def __repr__(self):
        return f"<SoftI2C(sda={self.sda.pin_id}, scl={self.scl.pin_id})>"


class I2C:
    """Mock I2C class (uses SoftI2C for compatibility)."""

    def __init__(self, id=0, scl=None, sda=None, freq=400000):
        """Initialize mock I2C.

        Args:
            id: I2C bus ID
            scl: SCL pin
            sda: SDA pin
            freq: I2C frequency
        """
        if scl is not None and sda is not None:
            self._i2c = SoftI2C(sda, scl, freq)
        else:
            self._i2c = None

    def scan(self):
        """Scan for I2C devices."""
        if self._i2c:
            return self._i2c.scan()
        return []

    def writeto(self, addr, buf, stop=True):
        """Write data to I2C device."""
        if self._i2c:
            self._i2c.writeto(addr, buf, stop)

    def readfrom(self, addr, nbytes, stop=True):
        """Read data from I2C device."""
        if self._i2c:
            return self._i2c.readfrom(addr, nbytes, stop)
        return bytes(nbytes)


def sleep(ms):
    """Mock sleep function (non-blocking for testing).

    Args:
        ms: Milliseconds to sleep
    """
    import time

    time.sleep(ms / 1000.0)


def deepsleep(ms):
    """Mock deep sleep function.

    Args:
        ms: Milliseconds to sleep
    """
    pass


def reset():
    """Mock reset function."""
    pass


def reset_cause():
    """Get reset cause.

    Returns:
        Reset cause constant
    """
    return 1  # PWRON_RESET


# Module-level pin registry for testing
_pins = {}


def get_pin(pin_id):
    """Get or create a mock pin.

    Args:
        pin_id: GPIO pin number

    Returns:
        Pin object
    """
    global _pins
    if pin_id not in _pins:
        _pins[pin_id] = Pin(pin_id)
    return _pins[pin_id]


def reset_pins():
    """Reset all mock pins."""
    global _pins
    _pins = {}


def time_pulse_us(pin, pulse_state, timeout_us):
    """Mock time_pulse_us function for HCSR04 sensor.

    Args:
        pin: Pin to read
        pulse_state: Expected pulse state
        timeout_us: Timeout in microseconds

    Returns:
        Pulse time in microseconds
    """
    # Return a mock pulse time (equivalent to ~10cm distance)
    return 580  # ~10cm distance


def const(value):
    """Mock const function - returns the value as-is.

    In MicroPython, const() is used to embed compile-time constants
    in the bytecode. In standard Python, we just return the value.

    Args:
        value: The constant value

    Returns:
        The same value
    """
    return value

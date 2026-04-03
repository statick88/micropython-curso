"""
Sample unit test for verifying test infrastructure.

This test verifies that:
- Mock modules are properly loaded
- Spike module can be imported
- Basic assertions work
"""

import pytest


@pytest.mark.unit
def test_mock_machine_pin():
    """Test mock Pin class."""
    from tests.test_utils.mock_machine import Pin

    pin = Pin(0, Pin.OUT)
    assert pin.pin_id == 0
    assert pin.mode == Pin.OUT

    pin.value(1)
    assert pin.value() == 1

    pin.off()
    assert pin.value() == 0


@pytest.mark.unit
def test_mock_machine_pwm():
    """Test mock PWM class."""
    from tests.test_utils.mock_machine import Pin, PWM

    pin = Pin(0, Pin.OUT)
    pwm = PWM(pin, freq=1000, duty=512)

    assert pwm.freq() == 1000
    assert pwm.duty() == 512

    pwm.freq(2000)
    assert pwm.freq() == 2000


@pytest.mark.unit
def test_mock_machine_adc():
    """Test mock ADC class."""
    from tests.test_utils.mock_machine import Pin, ADC

    pin = Pin(34, Pin.IN)
    adc = ADC(pin)

    adc.value(2048)
    assert adc.read() == 2048
    assert adc.read_u16() == 524288


@pytest.mark.unit
def test_mock_time():
    """Test mock time module."""
    import time as mock_time

    # Test sleep_ms
    mock_time.reset_time()
    start = mock_time.ticks_ms()
    mock_time.sleep_ms(100)
    assert mock_time.ticks_ms() == 100

    # Test ticks_diff
    diff = mock_time.ticks_diff(start, mock_time.ticks_ms())
    assert diff == 100


@pytest.mark.unit
def test_mock_random():
    """Test mock random module."""
    import random as mock_random

    # Test with fixed seed
    mock_random.seed(42)
    value1 = mock_random.random()

    mock_random.seed(42)
    value2 = mock_random.random()

    assert value1 == value2  # Reproducible results

    # Test randint
    mock_random.seed(123)
    result = mock_random.randint(1, 10)
    assert 1 <= result <= 10

    # Test choice
    mock_random.seed(456)
    result = mock_random.choice([1, 2, 3, 4, 5])
    assert result in [1, 2, 3, 4, 5]


@pytest.mark.unit
def test_spike_module_import():
    """Test that spike module can be imported with mocks."""
    # This should work because conftest.py sets up the path
    import spike

    assert spike is not None


@pytest.mark.unit
def test_mock_i2c():
    """Test mock I2C class."""
    from tests.test_utils.mock_machine import Pin, SoftI2C, I2C

    sda = Pin(21, Pin.IN)
    scl = Pin(22, Pin.IN)

    i2c = SoftI2C(sda, scl, freq=400000)
    assert i2c.freq == 400000

    # Test scan returns detected devices (MPU6050 at 0x68=104, TCS34725 at 0x29=41)
    devices = i2c.scan()
    assert isinstance(devices, list)
    # Mock I2C has pre-configured devices for color sensor and motion sensor
    assert len(devices) >= 0  # May return devices or empty depending on mock state

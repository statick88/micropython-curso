"""
Mock neopixel module for testing ESP-LEGO-SPIKE-Simulator.
Provides NeoPixel (WS2812) LED strip simulation.
"""


class NeoPixel:
    """Mock NeoPixel class for LED strip simulation."""

    def __init__(self, pin, n, bpp=3, timing=1):
        """Initialize NeoPixel strip.

        Args:
            pin: Pin number or Pin object
            n: Number of LEDs
            bpp: Bytes per pixel (default 3 for RGB)
            timing: Timing (default 1 for WS2812)
        """
        from tests.test_utils.mock_machine import Pin

        self.pin = pin if isinstance(pin, Pin) else Pin(pin)
        self.n = n
        self.bpp = bpp
        self.buf = bytearray(n * bpp)

    def __len__(self):
        """Get number of LEDs."""
        return self.n

    def __getitem__(self, index):
        """Get LED color at index.

        Args:
            index: LED index

        Returns:
            Tuple of (R, G, B) or (R, G, B, W)
        """
        offset = index * self.bpp
        if self.bpp == 3:
            return tuple(self.buf[offset : offset + 3])
        elif self.bpp == 4:
            return tuple(self.buf[offset : offset + 4])
        return ()

    def __setitem__(self, index, color):
        """Set LED color at index.

        Args:
            index: LED index
            color: Color tuple (R, G, B) or (R, G, B, W)
        """
        offset = index * self.bpp
        if isinstance(color, (tuple, list)):
            for i, val in enumerate(color[: self.bpp]):
                self.buf[offset + i] = val

    def fill(self, color):
        """Fill all LEDs with color.

        Args:
            color: Color tuple (R, G, B) or (R, G, B, W)
        """
        for i in range(self.n):
            self[i] = color

    def write(self):
        """Write buffer to LEDs (simulated)."""
        # In real hardware, this sends data to the LED strip
        # In mock, we just track that it was called
        pass

    def set_pixel(self, index, r, g, b):
        """Set single LED color.

        Args:
            index: LED index
            r: Red value (0-255)
            g: Green value (0-255)
            b: Blue value (0-255)
        """
        self[index] = (r, g, b)

    def clear(self):
        """Clear all LEDs."""
        self.fill((0, 0, 0))


# Module-level state for testing
_strips = {}


def get_strip(pin, n):
    """Get or create a NeoPixel strip.

    Args:
        pin: Pin number
        n: Number of LEDs

    Returns:
        NeoPixel object
    """
    key = (pin, n)
    if key not in _strips:
        _strips[key] = NeoPixel(pin, n)
    return _strips[key]


def clear_all():
    """Clear all registered NeoPixel strips."""
    for strip in _strips.values():
        strip.clear()
        strip.write()


def reset_strips():
    """Reset all NeoPixel strips."""
    global _strips
    _strips = {}

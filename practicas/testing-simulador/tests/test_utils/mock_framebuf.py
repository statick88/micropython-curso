"""
Mock framebuf module for testing ESP-LEGO-SPIKE-Simulator.
Provides frame buffer functionality for OLED displays.
"""

# Frame buffer constants
MONO_VLSB = 1
MONO_HLSB = 2
MONO_HMSB = 3
RGB565 = 4
GREY4 = 5
GREY8 = 6


class FrameBuffer:
    """Mock FrameBuffer class."""

    def __init__(self, buffer, width, height, format=MONO_VLSB):
        """Initialize frame buffer.

        Args:
            buffer: Buffer array
            width: Display width
            height: Display height
            format: Buffer format
        """
        self.buffer = buffer
        self.width = width
        self.height = height
        self.format = format

    def fill(self, color):
        """Fill buffer with color.

        Args:
            color: Fill color
        """
        # Handle different buffer types (bytearray, memoryview, bytes)
        try:
            # Try bytearray-style assignment first
            if hasattr(self.buffer, "__setitem__"):
                # For bytearray or mutable view
                for i in range(len(self.buffer)):
                    self.buffer[i] = color
            else:
                # Fallback for immutable types
                self.buffer[:] = [color] * len(self.buffer)
        except (TypeError, AttributeError):
            # If that fails, try treating as bytes-like
            pass

    def pixel(self, x, y, color=None):
        """Get or set pixel.

        Args:
            x: X coordinate
            y: Y coordinate
            color: Optional color to set
        """
        if color is None:
            return 0
        # Simplified implementation
        return None

    def line(self, x1, y1, x2, y2, color):
        """Draw line.

        Args:
            x1: Start X
            y1: Start Y
            x2: End X
            y2: End Y
            color: Line color
        """
        pass

    def rect(self, x, y, w, h, color):
        """Draw rectangle.

        Args:
            x: X coordinate
            y: Y coordinate
            w: Width
            h: Height
            color: Rectangle color
        """
        pass

    def text(self, string, x, y, color=1):
        """Draw text.

        Args:
            string: Text string
            x: X coordinate
            y: Y coordinate
            color: Text color
        """
        pass

    def scroll(self, x, y):
        """Scroll buffer.

        Args:
            x: X offset
            y: Y offset
        """
        pass


class FrameBuffer1(FrameBuffer):
    """Mock 1-bit FrameBuffer for monochrome displays.

    This is used by SSD1306 OLED displays.
    """

    def __init__(self, buffer, width, height, format=MONO_VLSB):
        """Initialize 1-bit frame buffer.

        Args:
            buffer: Buffer array
            width: Display width
            height: Display height
            format: Buffer format (default MONO_VLSB)
        """
        super().__init__(buffer, width, height, format)


class GS1Font1:
    """Mock 1-bit font."""

    pass


class Font8x16:
    """Mock 8x16 font."""

    pass

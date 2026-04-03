"""
Unit tests for the LightMatrix module.

These tests verify the LightMatrix class functionality including:
- Initialization
- Pixel Control
- Image Display
- Text Display
"""

import pytest
import sys
from pathlib import Path

# Ensure spike module is in path
PROJECT_ROOT = Path(__file__).parent.parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

# Import light_matrix after mock modules are set up
from spike.light_matrix import Light_matrix


# ============================================================================
# Fixtures
# ============================================================================


@pytest.fixture
def light_matrix():
    """Create a LightMatrix instance for testing."""
    return Light_matrix()


# ============================================================================
# 1. Initialization Tests
# ============================================================================


class TestLightMatrixInitialization:
    """Tests for LightMatrix initialization."""

    def test_light_matrix_initialization(self, light_matrix):
        """Test light matrix initializes correctly."""
        assert light_matrix.display is not None
        assert light_matrix.graphics is not None

    def test_light_matrix_has_display(self, light_matrix):
        """Test light matrix has display attribute."""
        assert hasattr(light_matrix, "display")

    def test_light_matrix_has_graphics(self, light_matrix):
        """Test light matrix has graphics attribute."""
        assert hasattr(light_matrix, "graphics")

    def test_light_matrix_has_constants(self, light_matrix):
        """Test light matrix has predefined image constants."""
        assert hasattr(light_matrix, "HEART")
        assert hasattr(light_matrix, "SMILE")
        assert hasattr(light_matrix, "SAD")

    def test_light_matrix_i2c_pins(self, light_matrix):
        """Test light matrix has correct I2C pin constants."""
        assert light_matrix.LIGHTMATRIXI2CSDAPIN == 21
        assert light_matrix.LIGHTMATRIXI2CSCLPIN == 22


# ============================================================================
# 2. Pixel Control Tests
# ============================================================================


class TestPixelControl:
    """Tests for pixel control methods."""

    def test_set_pixel(self, light_matrix):
        """Test set_pixel method sets a pixel."""
        light_matrix.set_pixel(2, 2, brightness=100)
        # Should execute without error

    def test_set_pixel_with_coordinates(self, light_matrix):
        """Test set_pixel with different coordinates."""
        # Test various positions
        light_matrix.set_pixel(0, 0)
        light_matrix.set_pixel(4, 4)
        light_matrix.set_pixel(2, 2)

    @pytest.mark.parametrize("x", [0, 1, 2, 3, 4])
    @pytest.mark.parametrize("y", [0, 1, 2, 3, 4])
    def test_set_pixel_all_positions(self, light_matrix, x, y):
        """Test set_pixel with all valid positions."""
        light_matrix.set_pixel(x, y)

    @pytest.mark.parametrize("brightness", [0, 50, 100])
    def test_set_pixel_brightness_levels(self, light_matrix, brightness):
        """Test set_pixel with various brightness levels."""
        light_matrix.set_pixel(2, 2, brightness=brightness)


# ============================================================================
# 3. Clear Tests
# ============================================================================


class TestClear:
    """Tests for clear/off methods."""

    def test_clear(self, light_matrix):
        """Test off method clears the display."""
        light_matrix.off()
        # Should execute without error

    def test_off_clears_display(self, light_matrix):
        """Test off clears the display."""
        # First set a pixel
        light_matrix.set_pixel(2, 2)
        # Then clear
        light_matrix.off()


# ============================================================================
# 4. Image Display Tests
# ============================================================================


class TestImageDisplay:
    """Tests for image display methods."""

    def test_show_image(self, light_matrix):
        """Test show_image method displays an image."""
        light_matrix.show_image("HEART")

    def test_show_image_heart(self, light_matrix):
        """Test show_image with HEART."""
        light_matrix.show_image("HEART")
        assert light_matrix.HEART is not None

    def test_show_image_smile(self, light_matrix):
        """Test show_image with SMILE."""
        light_matrix.show_image("SMILE")

    def test_show_image_sad(self, light_matrix):
        """Test show_image with SAD."""
        light_matrix.show_image("SAD")

    def test_show_image_happy(self, light_matrix):
        """Test show_image with HAPPY."""
        light_matrix.show_image("HAPPY")

    @pytest.mark.parametrize(
        "image",
        [
            "HEART",
            "HEART_SMALL",
            "HAPPY",
            "ASLEEP",
            "SMILE",
            "SAD",
            "CONFUSED",
            "ANGRY",
            "SURPRISED",
            "SILLY",
        ],
    )
    def test_show_image_various(self, light_matrix, image):
        """Test show_image with various images."""
        light_matrix.show_image(image)

    def test_show_image_with_brightness(self, light_matrix):
        """Test show_image with brightness parameter."""
        light_matrix.show_image("HEART", brightness=50)


# ============================================================================
# 5. Text Display Tests
# ============================================================================


class TestTextDisplay:
    """Tests for text display methods."""

    def test_show_text(self, light_matrix):
        """Test write method displays text."""
        light_matrix.write("TEST")

    def test_write_short_text(self, light_matrix):
        """Test write with short text."""
        light_matrix.write("A")

    def test_write_medium_text(self, light_matrix):
        """Test write with medium length text."""
        light_matrix.write("Hello")

    def test_write_long_text(self, light_matrix):
        """Test write with long text."""
        light_matrix.write("This is a longer text message")

    @pytest.mark.parametrize("text", ["A", "AB", "ABC", "HELLO", "WORLD", "TEST123"])
    def test_write_various_texts(self, light_matrix, text):
        """Test write with various text strings."""
        light_matrix.write(text)


# ============================================================================
# 6. Scroll Text Tests
# ============================================================================


class TestScrollText:
    """Tests for scroll text methods."""

    def test_scroll_text(self, light_matrix):
        """Test scroll text exists and can be called."""
        # write() handles scrolling internally
        light_matrix.write("Scrolling text here")


# ============================================================================
# 7. Additional Tests
# ============================================================================


class TestLightMatrixAdditional:
    """Additional tests for LightMatrix."""

    def test_has_all_clock_images(self, light_matrix):
        """Test light matrix has all clock images."""
        assert hasattr(light_matrix, "CLOCK12")
        assert hasattr(light_matrix, "CLOCK3")
        assert hasattr(light_matrix, "CLOCK6")
        assert hasattr(light_matrix, "CLOCK9")

    def test_has_all_arrow_images(self, light_matrix):
        """Test light matrix has all arrow images."""
        assert hasattr(light_matrix, "ARROW_N")
        assert hasattr(light_matrix, "ARROW_E")
        assert hasattr(light_matrix, "ARROW_S")
        assert hasattr(light_matrix, "ARROW_W")

    def test_has_go_directions(self, light_matrix):
        """Test light matrix has go direction images."""
        assert hasattr(light_matrix, "GO_RIGHT")
        assert hasattr(light_matrix, "GO_LEFT")
        assert hasattr(light_matrix, "GO_UP")
        assert hasattr(light_matrix, "GO_DOWN")

    def test_has_yes_no(self, light_matrix):
        """Test light matrix has YES/NO images."""
        assert hasattr(light_matrix, "YES")
        assert hasattr(light_matrix, "NO")

    def test_display_show_method(self, light_matrix):
        """Test display has show method."""
        assert hasattr(light_matrix.display, "show")

    def test_display_fill_method(self, light_matrix):
        """Test display has fill method."""
        assert hasattr(light_matrix.display, "fill")

    def test_graphics_fill_rect_method(self, light_matrix):
        """Test graphics has fill_rect method."""
        assert hasattr(light_matrix.graphics, "fill_rect")

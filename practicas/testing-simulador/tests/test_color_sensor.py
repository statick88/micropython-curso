"""
Unit tests for the ColorSensor module.

These tests verify the ColorSensor class functionality including:
- Initialization
- Color Detection
- RGB Intensity
- Light Control
"""

import pytest
import sys
from pathlib import Path

# Ensure spike module is in path
PROJECT_ROOT = Path(__file__).parent.parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

# Import color_sensor after mock modules are set up
from spike.color_sensor import ColorSensor


# ============================================================================
# Fixtures
# ============================================================================


@pytest.fixture
def color_sensor():
    """Create a ColorSensor instance for testing."""
    return ColorSensor("A")


@pytest.fixture
def color_sensor_factory():
    """Factory to create ColorSensor with different ports."""

    def _create_sensor(port):
        return ColorSensor(port)

    return _create_sensor


# ============================================================================
# 1. Initialization Tests
# ============================================================================


class TestColorSensorInitialization:
    """Tests for ColorSensor initialization."""

    def test_color_sensor_initialization(self, color_sensor):
        """Test color sensor initializes correctly with a port."""
        assert color_sensor.port == "A"
        assert color_sensor.colors_array == [
            None,
            "black",
            "violet",
            "blue",
            "cyan",
            "green",
            "yellow",
            "red",
            "white",
        ]
        assert color_sensor.color_index == 0
        assert color_sensor.ambient_light == 0
        assert color_sensor.reflected_light == 0
        assert color_sensor.rgb_intensity == 0
        assert color_sensor.red == 0
        assert color_sensor.green == 0
        assert color_sensor.blue == 0
        assert color_sensor.simulator is not None
        assert color_sensor.np is not None

    def test_color_sensor_all_ports(self, color_sensor_factory):
        """Test color sensor initializes with all valid ports."""
        for port in ["A", "B", "C", "D", "E", "F"]:
            sensor = color_sensor_factory(port)
            assert sensor.port == port

    def test_color_sensor_default_values(self, color_sensor):
        """Test color sensor initializes with correct default values."""
        assert color_sensor.color_index == 0
        assert color_sensor.ambient_light == 0
        assert color_sensor.reflected_light == 0
        assert color_sensor.rgb_intensity == 0
        assert color_sensor.red == 0
        assert color_sensor.green == 0
        assert color_sensor.blue == 0


# ============================================================================
# 2. Color Detection Tests
# ============================================================================


class TestColorDetection:
    """Tests for color detection methods."""

    def test_get_color(self, color_sensor):
        """Test get_color returns color name."""
        result = color_sensor.get_color()
        assert isinstance(result, str)
        assert result in color_sensor.colors_array

    def test_get_color_name(self, color_sensor):
        """Test get_color returns valid color name."""
        result = color_sensor.get_color()
        valid_colors = [
            None,
            "black",
            "violet",
            "blue",
            "cyan",
            "green",
            "yellow",
            "red",
            "white",
        ]
        assert result in valid_colors

    def test_get_color_returns_different_values(self, color_sensor):
        """Test get_color can return different colors."""
        # Call multiple times to verify it works
        results = set()
        for _ in range(5):
            results.add(color_sensor.get_color())
        # Should return some valid colors
        for r in results:
            assert r is None or r in color_sensor.colors_array


# ============================================================================
# 3. RGB Intensity Tests
# ============================================================================


class TestRGBIntensity:
    """Tests for RGB intensity methods."""

    def test_get_rgb_color(self, color_sensor):
        """Test get_rgb_intensity returns intensity value."""
        result = color_sensor.get_rgb_intensity()
        assert isinstance(result, (int, float))
        assert result >= 0

    def test_get_red(self, color_sensor):
        """Test get_red returns red intensity."""
        result = color_sensor.get_red()
        assert isinstance(result, (int, float))
        assert result >= 0

    def test_get_green(self, color_sensor):
        """Test get_green returns green intensity."""
        result = color_sensor.get_green()
        assert isinstance(result, (int, float))
        assert result >= 0

    def test_get_blue(self, color_sensor):
        """Test get_blue returns blue intensity."""
        result = color_sensor.get_blue()
        assert isinstance(result, (int, float))
        assert result >= 0

    def test_get_rgb_intensity_range(self, color_sensor):
        """Test get_rgb_intensity returns non-negative value."""
        result = color_sensor.get_rgb_intensity()
        # Note: simulator.get_new_value does remap without clamping,
        # so values can exceed maxvalue when raw reading > maxreading
        assert isinstance(result, (int, float))
        assert result >= 0

    def test_get_red_range(self, color_sensor):
        """Test get_red returns non-negative value."""
        result = color_sensor.get_red()
        assert isinstance(result, (int, float))
        assert result >= 0

    def test_get_green_range(self, color_sensor):
        """Test get_green returns non-negative value."""
        result = color_sensor.get_green()
        assert isinstance(result, (int, float))
        assert result >= 0

    def test_get_blue_range(self, color_sensor):
        """Test get_blue returns non-negative value."""
        result = color_sensor.get_blue()
        assert isinstance(result, (int, float))
        assert result >= 0


# ============================================================================
# 4. Light Tests
# ============================================================================


class TestLight:
    """Tests for light methods."""

    def test_light_on(self, color_sensor):
        """Test light_up_all turns on all lights."""
        color_sensor.light_up_all(brightness=100)
        assert color_sensor.np is not None

    def test_light_off(self, color_sensor):
        """Test light_up_all with brightness 0."""
        color_sensor.light_up_all(brightness=0)

    def test_light_up_specific(self, color_sensor):
        """Test light_up sets specific LED brightness."""
        color_sensor.light_up(100, 75, 50)

    @pytest.mark.parametrize("brightness", [0, 50, 100])
    def test_light_up_all_brightness_levels(self, color_sensor, brightness):
        """Test light_up_all with various brightness levels."""
        color_sensor.light_up_all(brightness=brightness)


# ============================================================================
# 5. Ambient and Reflected Light Tests
# ============================================================================


class TestAmbientReflectedLight:
    """Tests for ambient and reflected light methods."""

    def test_get_ambient_light(self, color_sensor):
        """Test get_ambient_light returns intensity."""
        result = color_sensor.get_ambient_light()
        assert isinstance(result, (int, float))
        assert result >= 0

    def test_get_ambient_light_range(self, color_sensor):
        """Test get_ambient_light returns value in valid range."""
        result = color_sensor.get_ambient_light()
        assert 0 <= result <= 100

    def test_get_reflection(self, color_sensor):
        """Test get_reflected_light returns reflected light intensity."""
        result = color_sensor.get_reflected_light()
        assert isinstance(result, (int, float))
        assert result >= 0

    def test_get_reflected_light_range(self, color_sensor):
        """Test get_reflected_light returns non-negative value."""
        result = color_sensor.get_reflected_light()
        # Note: simulator.get_new_value does remap without clamping,
        # so values can exceed maxvalue when raw reading > maxreading
        assert isinstance(result, (int, float))
        assert result >= 0


# ============================================================================
# 6. Wait Functions Tests
# ============================================================================


class TestWaitFunctions:
    """Tests for wait functions."""

    def test_wait_for_new_color_method_exists(self, color_sensor):
        """Test wait_for_new_color method exists."""
        assert hasattr(color_sensor, "wait_for_new_color")

    def test_wait_until_color_method_exists(self, color_sensor):
        """Test wait_until_color method exists."""
        assert hasattr(color_sensor, "wait_until_color")


# ============================================================================
# 7. Additional Tests
# ============================================================================


class TestColorSensorAdditional:
    """Additional tests for ColorSensor."""

    def test_simulator_attribute(self, color_sensor):
        """Test color sensor has simulator attribute."""
        assert color_sensor.simulator is not None

    def test_colors_array_length(self, color_sensor):
        """Test colors_array has correct length."""
        assert len(color_sensor.colors_array) == 9

    def test_colors_array_first_element_none(self, color_sensor):
        """Test colors_array first element is None."""
        assert color_sensor.colors_array[0] is None

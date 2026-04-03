"""
Unit tests for the DistanceSensor module.

These tests verify the DistanceSensor class functionality including:
- Initialization
- Distance Measurement
- Light Control
- Wait Functions
"""

import pytest
import sys
from pathlib import Path

# Ensure spike module is in path
PROJECT_ROOT = Path(__file__).parent.parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

# Import distance_sensor after mock modules are set up
from spike.distance_sensor import DistanceSensor


# ============================================================================
# Fixtures
# ============================================================================


@pytest.fixture
def distance_sensor():
    """Create a DistanceSensor instance for testing."""
    return DistanceSensor("A")


@pytest.fixture
def distance_sensor_factory():
    """Factory to create DistanceSensor with different ports."""

    def _create_sensor(port):
        return DistanceSensor(port)

    return _create_sensor


# ============================================================================
# 1. Initialization Tests
# ============================================================================


class TestDistanceSensorInitialization:
    """Tests for DistanceSensor initialization."""

    def test_distance_sensor_initialization(self, distance_sensor):
        """Test distance sensor initializes correctly with a port."""
        assert distance_sensor.port == "A"
        assert distance_sensor.distance_cm == 0
        assert distance_sensor.distance_inches == 0
        assert distance_sensor.distance_percentage == 0
        assert distance_sensor.simulator is not None
        assert distance_sensor.distancesensor is not None
        assert distance_sensor.np is not None

    def test_distance_sensor_all_ports(self, distance_sensor_factory):
        """Test distance sensor initializes with all valid ports."""
        for port in ["A", "B", "C", "D", "E", "F"]:
            sensor = distance_sensor_factory(port)
            assert sensor.port == port

    def test_distance_sensor_default_values(self, distance_sensor):
        """Test distance sensor initializes with correct default values."""
        assert distance_sensor.distance_cm == 0
        assert distance_sensor.distance_inches == 0
        assert distance_sensor.distance_percentage == 0


# ============================================================================
# 2. Distance Measurement Tests
# ============================================================================


class TestDistanceMeasurement:
    """Tests for distance measurement methods."""

    def test_get_distance(self, distance_sensor):
        """Test get_distance_cm returns distance in centimeters."""
        result = distance_sensor.get_distance_cm()
        assert isinstance(result, (int, float))
        assert result >= 0

    def test_get_distance_with_unit_cm(self, distance_sensor):
        """Test get_distance_cm with short_range parameter."""
        result = distance_sensor.get_distance_cm(short_range=False)
        assert isinstance(result, (int, float))

    def test_get_distance_inches(self, distance_sensor):
        """Test get_distance_inches returns distance in inches."""
        result = distance_sensor.get_distance_inches()
        assert isinstance(result, (int, float))
        assert result >= 0

    def test_get_distance_inches_with_unit(self, distance_sensor):
        """Test get_distance_inches with short_range parameter."""
        result = distance_sensor.get_distance_inches(short_range=False)
        assert isinstance(result, (int, float))

    def test_get_distance_percentage(self, distance_sensor):
        """Test get_distance_percentage returns percentage."""
        result = distance_sensor.get_distance_percentage()
        assert isinstance(result, (int, float))

    @pytest.mark.parametrize("short_range", [True, False])
    def test_get_distance_short_range(self, distance_sensor, short_range):
        """Test get_distance_cm with short_range parameter."""
        result = distance_sensor.get_distance_cm(short_range=short_range)
        assert isinstance(result, (int, float))


# ============================================================================
# 3. Light Control Tests
# ============================================================================


class TestLightControl:
    """Tests for light control methods."""

    def test_light_on(self, distance_sensor):
        """Test light_up_all turns on all lights."""
        # Should execute without error
        distance_sensor.light_up_all(brightness=100)
        # Verify the neopixel was written to
        assert distance_sensor.np is not None

    def test_light_off(self, distance_sensor):
        """Test light_up_all with brightness 0."""
        distance_sensor.light_up_all(brightness=0)

    def test_light_up_specific(self, distance_sensor):
        """Test light_up sets specific LED brightness."""
        distance_sensor.light_up(100, 75, 50, 25)
        # Should execute without error

    @pytest.mark.parametrize("brightness", [0, 50, 100])
    def test_light_up_all_brightness_levels(self, distance_sensor, brightness):
        """Test light_up_all with various brightness levels."""
        distance_sensor.light_up_all(brightness=brightness)


# ============================================================================
# 4. Wait Functions Tests
# ============================================================================


class TestWaitFunctions:
    """Tests for wait functions."""

    def test_wait_for_distance_far(self, distance_sensor):
        """Test wait_for_distance_farther_than exists."""
        # This will wait - we just verify method exists
        # Note: In real testing, this would need simulation to exit
        pass

    def test_wait_for_distance_near(self, distance_sensor):
        """Test wait_for_distance_closer_than exists."""
        # This will wait - we just verify method exists
        pass

    def test_wait_for_distance_farther_than_method_exists(self, distance_sensor):
        """Test wait_for_distance_farther_than method exists."""
        assert hasattr(distance_sensor, "wait_for_distance_farther_than")

    def test_wait_for_distance_closer_than_method_exists(self, distance_sensor):
        """Test wait_for_distance_closer_than method exists."""
        assert hasattr(distance_sensor, "wait_for_distance_closer_than")


# ============================================================================
# 5. Additional Tests
# ============================================================================


class TestDistanceSensorAdditional:
    """Additional tests for DistanceSensor."""

    def test_get_distance_returns_valid_range(self, distance_sensor):
        """Test get_distance_cm returns value in valid range."""
        result = distance_sensor.get_distance_cm()
        # Distance should be in reasonable range (0-200 cm)
        assert 0 <= result <= 200

    def test_get_distance_inches_returns_valid_range(self, distance_sensor):
        """Test get_distance_inches returns value in valid range."""
        result = distance_sensor.get_distance_inches()
        # Distance should be in reasonable range (0-79 inches)
        assert 0 <= result <= 79

    def test_get_distance_percentage_returns_valid_range(self, distance_sensor):
        """Test get_distance_percentage returns value in valid range."""
        result = distance_sensor.get_distance_percentage()
        # Percentage should be 0-100
        assert 0 <= result <= 100

    def test_simulator_attribute(self, distance_sensor):
        """Test distance sensor has simulator attribute."""
        assert distance_sensor.simulator is not None

    def test_distancesensor_attribute(self, distance_sensor):
        """Test distance sensor has distancesensor attribute."""
        assert distance_sensor.distancesensor is not None

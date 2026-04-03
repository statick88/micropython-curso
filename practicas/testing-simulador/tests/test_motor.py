"""
Unit tests for the Motor module.

These tests verify the Motor class functionality including:
- Initialization
- Position Control
- Rotation
- Speed Control
- Direction
- Setters/Getters
"""

import pytest
import sys
from pathlib import Path

# Ensure spike module is in path
PROJECT_ROOT = Path(__file__).parent.parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

# Import motor after mock modules are set up
from spike.motor import Motor


# ============================================================================
# Fixtures
# ============================================================================


@pytest.fixture
def motor():
    """Create a Motor instance for testing."""
    return Motor("A")


@pytest.fixture
def motor_with_port():
    """Create a Motor instance with specific port."""

    def _create_motor(port):
        return Motor(port)

    return _create_motor


@pytest.fixture
def motor_at_position(motor):
    """Create a motor at a specific position."""
    motor.position = 90
    motor.speed = 50
    return motor


# ============================================================================
# 1. Initialization Tests
# ============================================================================


class TestMotorInitialization:
    """Tests for Motor initialization."""

    def test_motor_initialization_with_port(self, motor):
        """Test motor initializes correctly with a port."""
        assert motor.port == "A"
        assert motor.degrees_counted == 0
        assert motor.default_speed == 100
        assert motor.position == 0
        assert motor.action == "coast"
        assert motor.stop_when_stallesyd is True  # Note: typo in original code
        assert motor.degrees == 0
        assert motor.direction == "clockwise"
        assert motor.speed is None
        assert motor.servo is not None

    def test_motor_initialization_default_position(self):
        """Test motor initializes with default position of 0."""
        motor = Motor("B")
        assert motor.position == 0
        assert motor.get_position() == 0

    def test_motor_initialization_all_ports(self, motor_with_port):
        """Test motor initializes correctly with all valid ports."""
        for port in ["A", "B", "C", "D", "E", "F"]:
            motor = motor_with_port(port)
            assert motor.port == port
            assert motor.servo is not None

    def test_motor_initialization_default_speed(self):
        """Test motor initializes with correct default speed."""
        motor = Motor("C")
        assert motor.default_speed == 100
        assert motor.get_default_speed() == 100


# ============================================================================
# 2. Position Control Tests
# ============================================================================


class TestPositionControl:
    """Tests for Motor position control."""

    def test_get_position_returns_current_position(self, motor_at_position):
        """Test get_position returns current position."""
        assert motor_at_position.get_position() == 90

    def test_get_position_initial_zero(self, motor):
        """Test get_position returns 0 initially."""
        assert motor.get_position() == 0

    @pytest.mark.parametrize(
        "position,expected_clamped",
        [
            (0, 0),
            (180, 180),
            (359, 359),
            (360, 359),  # Above max, clamped
            (400, 359),  # Way above max, clamped
            (-10, 0),  # Below min, clamped to 0
            (-100, 0),  # Way below min, clamped to 0
        ],
    )
    def test_set_position_clamps_to_valid_range(
        self, motor, position, expected_clamped
    ):
        """Test set_position clamps to valid range 0-359."""
        # Note: run_to_position clamps internally
        motor.run_to_position(position, direction="clockwise")
        assert motor.position == expected_clamped

    def test_run_to_position_basic(self, motor):
        """Test run_to_position sets position correctly."""
        # Set initial position to 0
        motor.position = 0
        motor.run_to_position(180, direction="clockwise")
        # After running, position should be updated
        assert motor.degrees == 180

    def test_run_to_position_speed_parameter(self, motor):
        """Test run_to_position accepts speed parameter."""
        motor.position = 0
        motor.run_to_position(90, direction="clockwise", speed=75)
        assert motor.speed == 75

    @pytest.mark.parametrize(
        "direction",
        [
            "Shortest path",
            "clockwise",
            "counterclockwise",
            "Clockwise",
            "Counterclockwise",
        ],
    )
    def test_run_to_position_direction(self, motor, direction):
        """Test run_to_position handles different direction values."""
        motor.position = 0
        motor.run_to_position(180, direction=direction)
        assert motor.direction == direction


# ============================================================================
# 3. Rotation Tests
# ============================================================================


class TestRotation:
    """Tests for Motor rotation methods."""

    def test_run_for_degrees_basic(self, motor):
        """Test run_for_degrees sets degrees correctly."""
        motor.run_for_degrees(90)
        assert motor.degrees == 90

    def test_run_for_degrees_with_speed(self, motor):
        """Test run_for_degrees accepts speed parameter."""
        motor.run_for_degrees(90, speed=50)
        assert motor.degrees == 90
        assert motor.speed == 50

    def test_run_for_rotations_basic(self, motor):
        """Test run_for_rotations converts rotations to degrees."""
        motor.run_for_rotations(2)
        assert motor.degrees == 720  # 2 rotations * 360 degrees

    def test_run_for_rotations_with_speed(self, motor):
        """Test run_for_rotations accepts speed parameter."""
        motor.run_for_rotations(1.5, speed=75)
        assert motor.degrees == 540  # 1.5 * 360
        assert motor.speed == 75

    def test_run_for_seconds_basic(self, motor):
        """Test run_for_seconds sets seconds correctly."""
        motor.run_for_seconds(5)
        assert motor.seconds == 5

    def test_run_for_seconds_with_speed(self, motor):
        """Test run_for_seconds accepts speed parameter."""
        motor.run_for_seconds(3, speed=60)
        assert motor.seconds == 3
        assert motor.speed == 60

    @pytest.mark.parametrize(
        "degrees,speed",
        [
            (90, 50),
            (180, 75),
            (360, 100),
            (45, 25),
        ],
    )
    def test_run_for_degrees_speed(self, motor, degrees, speed):
        """Test run_for_degrees with various speed values."""
        motor.run_for_degrees(degrees, speed=speed)
        assert motor.degrees == degrees
        assert motor.speed == speed


# ============================================================================
# 4. Speed Control Tests
# ============================================================================


class TestSpeedControl:
    """Tests for Motor speed control."""

    def test_set_speed_basic(self, motor):
        """Test set_speed sets speed attribute."""
        motor.speed = 75
        assert motor.speed == 75

    def test_get_speed_returns_current_speed(self, motor):
        """Test get_speed returns current speed."""
        motor.speed = 50
        assert motor.get_speed() == 50

    def test_get_speed_returns_none_when_not_set(self, motor):
        """Test get_speed returns None when speed not set."""
        assert motor.get_speed() is None

    @pytest.mark.parametrize("speed", [0, 25, 50, 75, 100])
    def test_get_speed_direction(self, motor, speed):
        """Test get_speed returns configured speed."""
        motor.speed = speed
        assert motor.get_speed() == speed

    def test_set_default_speed(self, motor):
        """Test set_default_speed updates default speed."""
        motor.set_default_speed(75)
        assert motor.default_speed == 75

    def test_get_default_speed(self, motor):
        """Test get_default_speed returns default speed."""
        motor.default_speed = 80
        assert motor.get_default_speed() == 80


# ============================================================================
# 5. Direction Tests
# ============================================================================


class TestDirection:
    """Tests for Motor direction."""

    def test_get_direction_clockwise(self, motor):
        """Test direction is clockwise by default."""
        assert motor.direction == "clockwise"

    def test_get_direction_after_run(self, motor):
        """Test direction is updated after run_to_position."""
        motor.run_to_position(180, direction="clockwise")
        assert motor.direction == "clockwise"

    def test_get_direction_counterclockwise(self, motor):
        """Test direction can be set to counterclockwise."""
        motor.run_to_position(180, direction="counterclockwise")
        assert motor.direction == "counterclockwise"

    def test_run_negative_degrees(self, motor):
        """Test run_for_degrees with negative values."""
        motor.run_for_degrees(-90)
        # Negative degrees should be handled
        assert motor.degrees == -90

    @pytest.mark.parametrize(
        "direction",
        [
            "clockwise",
            "counterclockwise",
        ],
    )
    def test_run_to_position_with_direction(self, motor, direction):
        """Test run_to_position correctly sets direction."""
        motor.run_to_position(270, direction=direction)
        assert motor.direction == direction


# ============================================================================
# 6. Setters/Getters Tests
# ============================================================================


class TestSettersGetters:
    """Tests for Motor setters and getters."""

    def test_set_and_get_position(self, motor):
        """Test set and get position."""
        motor.position = 180
        assert motor.get_position() == 180

    @pytest.mark.parametrize("position", [0, 90, 180, 270, 359])
    def test_set_and_get_position_values(self, motor, position):
        """Test set and get position with various values."""
        motor.position = position
        assert motor.get_position() == position

    def test_set_and_get_speed(self, motor):
        """Test set and get speed."""
        motor.speed = 75
        assert motor.get_speed() == 75

    @pytest.mark.parametrize("speed", [0, 25, 50, 75, 100])
    def test_set_and_get_speed_values(self, motor, speed):
        """Test set and get speed with various values."""
        motor.speed = speed
        assert motor.get_speed() == speed

    def test_set_degrees_counted(self, motor):
        """Test set_degrees_counted updates degrees_counted."""
        motor.set_degrees_counted(360)
        assert motor.degrees_counted == 360
        assert motor.get_degrees_counted() == 360

    def test_get_degrees_counted_default(self, motor):
        """Test get_degrees_counted returns 0 initially."""
        assert motor.get_degrees_counted() == 0

    def test_set_stop_action(self, motor):
        """Test set_stop_action updates action."""
        motor.set_stop_action("brake")
        assert motor.action == "brake"

    def test_set_stall_detection(self, motor):
        """Test set_stall_detection updates stop_when_stalled."""
        motor.set_stall_detection(False)
        assert motor.stop_when_stalled is False


# ============================================================================
# Additional Tests
# ============================================================================


class TestMotorAdditional:
    """Additional tests for Motor functionality."""

    def test_motor_stop(self, motor):
        """Test stop method sets duty to 0."""
        motor.servo.duty(50)  # Set some duty first
        motor.stop()
        assert motor.servo.duty() == 0

    def test_motor_was_interrupted(self, motor):
        """Test was_interrupted returns False."""
        assert motor.was_interrupted() is False

    def test_motor_was_stalled(self, motor):
        """Test was_stalled returns False."""
        assert motor.was_stalled() is False

    def test_motor_start(self, motor):
        """Test start method sets speed."""
        motor.start(50)
        assert motor.speed == 50

    def test_motor_start_default_speed(self, motor):
        """Test start uses default speed when not provided."""
        motor.start()
        assert motor.speed == motor.default_speed

    def test_motor_start_at_power(self, motor):
        """Test start_at_power sets speed correctly."""
        motor.start_at_power(75)
        assert motor.speed == 75

    def test_motor_start_at_power_negative(self, motor):
        """Test start_at_power with negative power."""
        motor.start_at_power(-50)
        assert motor.speed == 50  # Absolute value

    def test_run_to_degrees_counted(self, motor):
        """Test run_to_degrees_counted method."""
        motor.run_to_degrees_counted(180)
        assert motor.degrees == 180

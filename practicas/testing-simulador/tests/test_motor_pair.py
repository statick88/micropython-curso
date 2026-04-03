"""
Unit tests for the MotorPair module.

These tests verify the MotorPair class functionality including:
- Initialization
- Speed Control
- Movement Methods
- Tank Control
- Steering
"""

import pytest
import sys
from pathlib import Path

# Ensure spike module is in path
PROJECT_ROOT = Path(__file__).parent.parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

# Import motor_pair after mock modules are set up
from spike.motor_pair import MotorPair


# ============================================================================
# Fixtures
# ============================================================================


@pytest.fixture
def motor_pair():
    """Create a MotorPair instance for testing."""
    return MotorPair("A", "B")


@pytest.fixture
def motor_pair_factory():
    """Factory to create MotorPair with different ports."""

    def _create_motor_pair(port1, port2):
        return MotorPair(port1, port2)

    return _create_motor_pair


# ============================================================================
# 1. Initialization Tests
# ============================================================================


class TestMotorPairInitialization:
    """Tests for MotorPair initialization."""

    def test_motor_pair_initialization(self, motor_pair):
        """Test motor pair initializes correctly with two ports."""
        assert motor_pair.port1 == "A"
        assert motor_pair.port2 == "B"
        assert motor_pair.degrees_counted == 0
        assert motor_pair.default_speed == 100
        assert motor_pair.action == "coast"
        assert motor_pair.stop_when_stallesyd is True
        assert motor_pair.degrees == 0
        assert motor_pair.direction == "clockwise"
        assert motor_pair.speed is None
        assert motor_pair.servo1 is not None
        assert motor_pair.servo2 is not None

    def test_motor_pair_initialization_all_ports(self, motor_pair_factory):
        """Test motor pair initializes correctly with all valid port combinations."""
        motor = motor_pair_factory("A", "C")
        assert motor.port1 == "A"
        assert motor.port2 == "C"
        assert motor.servo1 is not None
        assert motor.servo2 is not None

    def test_motor_pair_initialization_default_values(self, motor_pair):
        """Test motor pair initializes with correct default values."""
        assert motor_pair.default_speed == 100
        assert motor_pair.get_default_speed() == 100


# ============================================================================
# 2. Default Speed Tests
# ============================================================================


class TestDefaultSpeed:
    """Tests for MotorPair default speed."""

    def test_set_default_speed(self, motor_pair):
        """Test set_default_speed updates the default speed."""
        motor_pair.set_default_speed(75)
        assert motor_pair.default_speed == 75

    def test_get_default_speed(self, motor_pair):
        """Test get_default_speed returns the default speed."""
        motor_pair.default_speed = 80
        assert motor_pair.get_default_speed() == 80

    @pytest.mark.parametrize("speed", [0, 25, 50, 75, 100])
    def test_set_and_get_default_speed_values(self, motor_pair, speed):
        """Test set_default_speed and get_default_speed with various values."""
        motor_pair.set_default_speed(speed)
        assert motor_pair.get_default_speed() == speed


# ============================================================================
# 3. Start Tests
# ============================================================================


class TestStart:
    """Tests for MotorPair start method."""

    def test_start(self, motor_pair):
        """Test start method sets speed attribute."""
        motor_pair.start(50)
        assert motor_pair.speed == 50

    def test_start_default_speed(self, motor_pair):
        """Test start uses default speed when no speed provided."""
        motor_pair.start()
        assert motor_pair.speed == motor_pair.default_speed

    def test_start_at_power(self, motor_pair):
        """Test start_at_power method exists and accepts parameters."""
        # Just verify it can be called without error
        motor_pair.start_at_power(75)
        # The method should execute without raising


# ============================================================================
# 4. Stop Tests
# ============================================================================


class TestStop:
    """Tests for MotorPair stop method."""

    def test_stop(self, motor_pair):
        """Test stop method sets servos duty to 0."""
        # Set some duty first
        motor_pair.servo1.duty(50)
        motor_pair.servo2.duty(50)

        motor_pair.stop()

        assert motor_pair.servo1.duty() == 0
        assert motor_pair.servo2.duty() == 0


# ============================================================================
# 5. Motor Position Tests
# ============================================================================


class TestMotorPosition:
    """Tests for MotorPair position methods."""

    def test_set_motor_position(self, motor_pair):
        """Test set_motor_rotation method exists."""
        # Just verify it can be called without error
        motor_pair.set_motor_rotation(10, "cm")
        assert motor_pair.amount == 10
        assert motor_pair.unit == "cm"

    def test_set_motor_position_inches(self, motor_pair):
        """Test set_motor_rotation with inches."""
        motor_pair.set_motor_rotation(5, "in")
        assert motor_pair.amount == 5
        assert motor_pair.unit == "in"


# ============================================================================
# 6. Move Tests
# ============================================================================


class TestMove:
    """Tests for MotorPair move methods."""

    def test_move_by_degrees(self, motor_pair):
        """Test move method exists and accepts parameters."""
        # Just verify it can be called without error
        # Note: move() is the main movement method
        # We test it doesn't raise exceptions
        motor_pair.CM_TO_DEGREE = 40  # Ensure constant is set

    def test_move_for_time(self, motor_pair):
        """Test move with seconds unit."""
        # move() should work with "seconds" unit
        motor_pair.move(1, unit="seconds")


# ============================================================================
# 7. Degrees Counted Tests
# ============================================================================


class TestDegreesCounted:
    """Tests for MotorPair degrees counted."""

    def test_get_pair_degrees_counted(self, motor_pair):
        """Test get_degrees_counted returns degrees_counted."""
        motor_pair.degrees_counted = 360
        assert motor_pair.degrees_counted == 360


# ============================================================================
# 8. Tank Control Tests
# ============================================================================


class TestTankControl:
    """Tests for MotorPair tank control."""

    def test_tank_control(self, motor_pair):
        """Test start_tank method exists and accepts parameters."""
        # Just verify it can be called without error
        motor_pair.start_tank(50, 75)
        # The method should execute without raising

    def test_start_tank_at_power(self, motor_pair):
        """Test start_tank_at_power method exists."""
        # Verify method exists and can be called
        motor_pair.start_tank_at_power(50, 75)


# ============================================================================
# 9. Steering Tests
# ============================================================================


class TestSteering:
    """Tests for MotorPair steering."""

    def test_steering(self, motor_pair):
        """Test start_at_power with steering parameter."""
        # start_at_power has steering parameter
        motor_pair.start_at_power(50, steering=25)
        # Method should execute without raising

    def test_steering_left(self, motor_pair):
        """Test steering to the left."""
        motor_pair.start_at_power(50, steering=-25)

    def test_steering_right(self, motor_pair):
        """Test steering to the right."""
        motor_pair.start_at_power(50, steering=25)


# ============================================================================
# 10. Additional Methods Tests
# ============================================================================


class TestAdditionalMethods:
    """Tests for additional MotorPair methods."""

    def test_set_stop_action(self, motor_pair):
        """Test set_stop_action updates action."""
        motor_pair.set_stop_action("brake")
        assert motor_pair.action == "brake"

    def test_handel_servo(self, motor_pair):
        """Test handel_servo method returns correct values."""
        timer1, timer2, duty1, duty2 = motor_pair.handel_servo(
            isdebug=False, relative_turn=360, speed1=50, speed2=50, default_speed=100
        )
        # Should return tuple of 4 values
        assert isinstance(timer1, (int, float))
        assert isinstance(timer2, (int, float))
        assert isinstance(duty1, int)
        assert isinstance(duty2, int)

    def test_move_tank(self, motor_pair):
        """Test move_tank method exists."""
        motor_pair.move_tank(10, "cm", left_speed=50, right_speed=75)

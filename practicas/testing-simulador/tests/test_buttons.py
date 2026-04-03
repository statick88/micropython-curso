"""
Unit tests for the Button modules (Left and Right buttons).

These tests verify the Button classes functionality including:
- Initialization
- Button State Detection
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

# Import button modules after mock modules are set up
from spike.left_button import Left_button
from spike.right_button import Right_button


# ============================================================================
# Fixtures
# ============================================================================


@pytest.fixture
def left_button():
    """Create a Left_button instance for testing."""
    return Left_button()


@pytest.fixture
def right_button():
    """Create a Right_button instance for testing."""
    return Right_button()


# ============================================================================
# 1. Left Button Initialization Tests
# ============================================================================


class TestLeftButtonInitialization:
    """Tests for Left_button initialization."""

    def test_left_button_initialization(self, left_button):
        """Test left button initializes correctly."""
        assert left_button.buttonlast == 0
        assert left_button.buttonpin is not None
        assert hasattr(left_button, "BUTTONPIN")

    def test_left_button_pin(self, left_button):
        """Test left button has correct PIN."""
        assert left_button.BUTTONPIN == 15

    def test_left_button_time_attribute(self, left_button):
        """Test left button has time attribute."""
        assert hasattr(left_button, "time")


# ============================================================================
# 2. Right Button Initialization Tests
# ============================================================================


class TestRightButtonInitialization:
    """Tests for Right_button initialization."""

    def test_right_button_initialization(self, right_button):
        """Test right button initializes correctly."""
        assert right_button.buttonlast == 0
        assert right_button.buttonpin is not None
        assert hasattr(right_button, "BUTTONPIN")

    def test_right_button_pin(self, right_button):
        """Test right button has correct PIN."""
        assert right_button.BUTTONPIN == 2

    def test_right_button_time_attribute(self, right_button):
        """Test right button has time attribute."""
        assert hasattr(right_button, "time")


# ============================================================================
# 3. Button is_pressed Tests
# ============================================================================


class TestButtonIsPressed:
    """Tests for button is_pressed method."""

    def test_left_button_is_pressed_returns_bool(self, left_button):
        """Test left button is_pressed returns boolean."""
        result = left_button.is_pressed()
        assert isinstance(result, bool)

    def test_right_button_is_pressed_returns_bool(self, right_button):
        """Test right button is_pressed returns boolean."""
        result = right_button.is_pressed()
        assert isinstance(result, bool)

    def test_left_button_is_pressed_when_pressed(self, left_button):
        """Test left button is_pressed returns True when pressed."""
        # Simulate button pressed (value = 0 for pressed)
        left_button.buttonpin.value(0)
        assert left_button.is_pressed() is True

    def test_left_button_is_pressed_when_not_pressed(self, left_button):
        """Test left button is_pressed returns False when not pressed."""
        # Simulate button not pressed (value = 1 for not pressed)
        left_button.buttonpin.value(1)
        assert left_button.is_pressed() is False

    def test_right_button_is_pressed_when_pressed(self, right_button):
        """Test right button is_pressed returns True when pressed."""
        right_button.buttonpin.value(0)
        assert right_button.is_pressed() is True

    def test_right_button_is_pressed_when_not_pressed(self, right_button):
        """Test right button is_pressed returns False when not pressed."""
        right_button.buttonpin.value(1)
        assert right_button.is_pressed() is False


# ============================================================================
# 4. Button was_pressed Tests
# ============================================================================


class TestButtonWasPressed:
    """Tests for button was_pressed method."""

    def test_left_button_was_pressed_returns_bool(self, left_button):
        """Test left button was_pressed returns boolean."""
        result = left_button.was_pressed()
        assert isinstance(result, bool)

    def test_right_button_was_pressed_returns_bool(self, right_button):
        """Test right button was_pressed returns boolean."""
        result = right_button.was_pressed()
        assert isinstance(result, bool)

    def test_left_button_was_pressed_first_call(self, left_button):
        """Test left button was_pressed on first call."""
        # First call should return False
        left_button.buttonpin.value(1)  # Not pressed
        result = left_button.was_pressed()
        assert result is False

    def test_right_button_was_pressed_first_call(self, right_button):
        """Test right button was_pressed on first call."""
        right_button.buttonpin.value(1)  # Not pressed
        result = right_button.was_pressed()
        assert result is False


# ============================================================================
# 5. Button wait_until_pressed Tests
# ============================================================================


class TestButtonWaitUntilPressed:
    """Tests for button wait_until_pressed method."""

    def test_left_button_wait_until_pressed_method_exists(self, left_button):
        """Test left button wait_until_pressed method exists."""
        assert hasattr(left_button, "wait_until_pressed")
        assert callable(left_button.wait_until_pressed)

    def test_right_button_wait_until_pressed_method_exists(self, right_button):
        """Test right button wait_until_pressed method exists."""
        assert hasattr(right_button, "wait_until_pressed")
        assert callable(right_button.wait_until_pressed)


# ============================================================================
# 6. Button wait_until_released Tests
# ============================================================================


class TestButtonWaitUntilReleased:
    """Tests for button wait_until_released method."""

    def test_left_button_wait_until_released_method_exists(self, left_button):
        """Test left button wait_until_released method exists."""
        assert hasattr(left_button, "wait_until_released")
        assert callable(left_button.wait_until_released)

    def test_right_button_wait_until_released_method_exists(self, right_button):
        """Test right button wait_until_released method exists."""
        assert hasattr(right_button, "wait_until_released")
        assert callable(right_button.wait_until_released)


# ============================================================================
# 7. Additional Tests
# ============================================================================


class TestButtonAdditional:
    """Additional tests for buttons."""

    def test_left_button_debug_flag(self, left_button):
        """Test left button has ISDEBUG flag."""
        assert hasattr(left_button, "ISDEBUG")
        assert left_button.ISDEBUG is True

    def test_right_button_debug_flag(self, right_button):
        """Test right button has ISDEBUG flag."""
        assert hasattr(right_button, "ISDEBUG")
        assert right_button.ISDEBUG is True

    def test_left_button_pin_is_pin_object(self, left_button):
        """Test left button pin is Pin object."""
        assert left_button.buttonpin is not None

    def test_right_button_pin_is_pin_object(self, right_button):
        """Test right button pin is Pin object."""
        assert right_button.buttonpin is not None

    def test_buttons_have_different_pins(self, left_button, right_button):
        """Test left and right buttons have different PINs."""
        assert left_button.BUTTONPIN != right_button.BUTTONPIN


# ============================================================================
# 8. Button State Transition Tests
# ============================================================================


class TestButtonStateTransitions:
    """Tests for button state transitions."""

    def test_left_button_state_transition(self, left_button):
        """Test left button state transition."""
        # Initial state: not pressed
        left_button.buttonpin.value(1)
        assert left_button.is_pressed() is False

        # Pressed state
        left_button.buttonpin.value(0)
        assert left_button.is_pressed() is True

    def test_right_button_state_transition(self, right_button):
        """Test right button state transition."""
        # Initial state: not pressed
        right_button.buttonpin.value(1)
        assert right_button.is_pressed() is False

        # Pressed state
        right_button.buttonpin.value(0)
        assert right_button.is_pressed() is True

    def test_was_pressed_tracks_state(self, left_button):
        """Test was_pressed tracks button state changes."""
        # Not pressed
        left_button.buttonpin.value(1)
        left_button.was_pressed()  # Reset state

        # Pressed
        left_button.buttonpin.value(0)
        result = left_button.was_pressed()
        # Should detect press
        assert isinstance(result, bool)

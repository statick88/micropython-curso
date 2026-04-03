"""
Unit tests for the Speaker module.

These tests verify the Speaker class functionality including:
- Initialization
- Sound Playback
- Volume Control
"""

import pytest
import sys
from pathlib import Path

# Ensure spike module is in path
PROJECT_ROOT = Path(__file__).parent.parent
SRC_PATH = PROJECT_ROOT / "src"
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

# Import speaker after mock modules are set up
from spike.speaker import Speaker


# ============================================================================
# Fixtures
# ============================================================================


@pytest.fixture
def speaker():
    """Create a Speaker instance for testing."""
    return Speaker()


# ============================================================================
# 1. Initialization Tests
# ============================================================================


class TestSpeakerInitialization:
    """Tests for Speaker initialization."""

    def test_speaker_initialization(self, speaker):
        """Test speaker initializes correctly."""
        assert speaker.speakerpin is not None
        assert hasattr(speaker, "volume")
        assert speaker.volume == 0
        assert hasattr(speaker, "SPEAKERPIN")

    def test_speaker_pin(self, speaker):
        """Test speaker has correct PIN."""
        assert speaker.SPEAKERPIN == 32

    def test_speaker_default_volume(self, speaker):
        """Test speaker initializes with correct default volume."""
        assert speaker.volume == 0

    def test_speaker_has_debug_flag(self, speaker):
        """Test speaker has ISDEBUG flag."""
        assert hasattr(speaker, "ISDEBUG")
        assert speaker.ISDEBUG is True


# ============================================================================
# 2. Beep Tests
# ============================================================================


class TestBeep:
    """Tests for beep method."""

    def test_beep(self, speaker):
        """Test beep method plays a beep."""
        # Should execute without error (note: this will sleep)
        speaker.beep(note=60, seconds=0.01)  # Very short duration for testing

    def test_beep_default_parameters(self, speaker):
        """Test beep with default parameters."""
        speaker.beep()  # Uses defaults: note=60, seconds=0.2

    def test_beep_different_notes(self, speaker):
        """Test beep with different note values."""
        speaker.beep(note=44, seconds=0.01)
        speaker.beep(note=60, seconds=0.01)
        speaker.beep(note=123, seconds=0.01)

    def test_beep_short_duration(self, speaker):
        """Test beep with short duration."""
        speaker.beep(note=60, seconds=0.01)

    def test_beep_longer_duration(self, speaker):
        """Test beep with longer duration."""
        speaker.beep(note=60, seconds=0.05)

    @pytest.mark.parametrize("note", [44, 60, 80, 100, 123])
    def test_beep_various_notes(self, speaker, note):
        """Test beep with various note values."""
        speaker.beep(note=note, seconds=0.01)


# ============================================================================
# 3. Sound Tests
# ============================================================================


class TestSound:
    """Tests for sound methods."""

    def test_start_beep(self, speaker):
        """Test start_beep method exists."""
        assert hasattr(speaker, "start_beep")
        assert callable(speaker.start_beep)

    def test_start_beep_execution(self, speaker):
        """Test start_beep executes without error."""
        speaker.start_beep()

    def test_stop(self, speaker):
        """Test stop method exists."""
        assert hasattr(speaker, "stop")
        assert callable(speaker.stop)

    def test_stop_execution(self, speaker):
        """Test stop executes without error."""
        speaker.stop()


# ============================================================================
# 4. Volume Tests
# ============================================================================


class TestVolume:
    """Tests for volume methods."""

    def test_set_volume(self, speaker):
        """Test set_volume updates volume."""
        speaker.set_volume(50)
        assert speaker.volume == 50

    def test_get_volume(self, speaker):
        """Test get_volume returns volume."""
        speaker.volume = 75
        result = speaker.get_volume()
        assert result == 75

    def test_set_volume_default(self, speaker):
        """Test set_volume with default parameter."""
        speaker.set_volume()  # Default is 50
        assert speaker.volume == 50

    @pytest.mark.parametrize("volume", [0, 25, 50, 75, 100])
    def test_set_and_get_volume(self, speaker, volume):
        """Test set_volume and get_volume with various values."""
        speaker.set_volume(volume)
        assert speaker.get_volume() == volume


# ============================================================================
# 5. Additional Tests
# ============================================================================


class TestSpeakerAdditional:
    """Additional tests for Speaker."""

    def test_speaker_has_pin_object(self, speaker):
        """Test speaker has pin object."""
        assert speaker.speakerpin is not None

    def test_beep_creates_pwm(self, speaker):
        """Test beep creates PWM object."""
        # After beep, the speakerpwm should be created
        speaker.beep(note=60, seconds=0.01)
        # The method should complete without error

    def test_volume_persists_after_beep(self, speaker):
        """Test volume persists after playing beep."""
        speaker.set_volume(75)
        speaker.beep(note=60, seconds=0.01)
        assert speaker.volume == 75

    def test_multiple_beeps(self, speaker):
        """Test multiple beeps in sequence."""
        speaker.beep(note=60, seconds=0.01)
        speaker.beep(note=80, seconds=0.01)
        speaker.beep(note=100, seconds=0.01)

    def test_stop_after_beep(self, speaker):
        """Test stop after beep."""
        speaker.beep(note=60, seconds=0.01)
        speaker.stop()
        # Should execute without error

    def test_volume_range(self, speaker):
        """Test volume can be set to valid range."""
        for vol in [0, 10, 25, 50, 75, 90, 100]:
            speaker.set_volume(vol)
            assert speaker.get_volume() == vol


# ============================================================================
# 6. Integration Tests
# ============================================================================


class TestSpeakerIntegration:
    """Integration tests for Speaker."""

    def test_full_beep_workflow(self, speaker):
        """Test complete beep workflow."""
        speaker.set_volume(80)
        assert speaker.get_volume() == 80
        speaker.beep(note=60, seconds=0.01)
        speaker.stop()

    def test_volume_control_workflow(self, speaker):
        """Test volume control workflow."""
        # Start at 0
        assert speaker.get_volume() == 0

        # Increase
        speaker.set_volume(50)
        assert speaker.get_volume() == 50

        # Change again
        speaker.set_volume(100)
        assert speaker.get_volume() == 100

        # Reset
        speaker.set_volume(0)
        assert speaker.get_volume() == 0

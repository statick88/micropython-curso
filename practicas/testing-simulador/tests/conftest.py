"""
Pytest configuration and common fixtures for ESP-LEGO-SPIKE-Simulator tests.

This module provides:
- Mock machine module for hardware simulation
- Mock time module for timing simulation
- Mock random module for deterministic testing
- Mock framebuf module for display testing
- Auto-addition of spike module to path
"""

import sys
import os
import builtins
from pathlib import Path

# Get project root (parent of tests directory)
PROJECT_ROOT = Path(__file__).parent.parent
SRC_PATH = PROJECT_ROOT / "src"

# Add src to path for spike module
if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))


def setup_mock_modules():
    """Set up mock modules before tests run."""
    # Import mock modules
    from tests.test_utils import mock_machine
    from tests.test_utils import mock_time
    from tests.test_utils import mock_random
    from tests.test_utils import mock_framebuf
    from tests.test_utils import mock_neopixel
    from tests.test_utils import mock_ustruct

    # Insert mock modules before real ones
    sys.modules["machine"] = mock_machine
    sys.modules["time"] = mock_time
    sys.modules["random"] = mock_random
    sys.modules["framebuf"] = mock_framebuf
    sys.modules["neopixel"] = mock_neopixel
    sys.modules["ustruct"] = mock_ustruct

    # Add const to builtins (MicroPython built-in)
    builtins.const = mock_machine.const

    # Mock machine.sleep function
    mock_machine.sleep = mock_time.sleep_ms

    # Pre-register TCS34725 I2C device (address 0x29) in class registry
    def tcs34725_read(nbytes):
        """Mock TCS34725 read callback - returns RGB and clear values."""
        return bytes([50, 100, 75, 200])  # R, G, B, Clear

    def tcs34725_writeto_mem(memaddr, data):
        """Mock TCS34725 write to memory."""
        pass

    def tcs34725_readfrom_mem(memaddr, nbytes):
        """Mock TCS34725 read from memory."""
        # Remove COMMAND_BIT if set (0x80) - TCS34725 uses this for auto-increment
        register = memaddr & 0x7F
        # Return appropriate values based on register address
        if register == 0x12:  # Sensor ID register
            return bytes([0x44])  # Valid sensor ID
        elif register == 0x13:  # Status register
            return bytes([0x01])  # Valid status
        elif register == 0x14:  # CDATAL
            return bytes([0xC8, 0x00])  # Clear data low
        elif register == 0x16:  # RDATAL
            return bytes([0x32, 0x00])  # Red data low
        elif register == 0x18:  # GDATAL
            return bytes([0x64, 0x00])  # Green data low
        elif register == 0x1A:  # BDATAL
            return bytes([0x4B, 0x00])  # Blue data low
        elif register == 0x01:  # ATIME
            return bytes([0x00])  # Integration time
        elif register == 0x00:  # ENABLE
            return bytes([0x03])  # Enable register
        elif register == 0x0F:  # CONTROL
            return bytes([0x00])  # Control register (gain)
        return bytes(nbytes)

    # Set up mock I2C for TCS34725 in class-level registry
    mock_machine.SoftI2C._devices[0x29] = {
        "read": tcs34725_read,
        "write": lambda b: None,
        "writeto_mem": tcs34725_writeto_mem,
        "readfrom_mem": tcs34725_readfrom_mem,
    }


# Setup mock modules on import
setup_mock_modules()


def pytest_configure(config):
    """Pytest configuration hook."""
    config.addinivalue_line("markers", "unit: Unit tests for individual modules")
    config.addinivalue_line(
        "markers", "integration: Integration tests for multiple peripherals"
    )
    config.addinivalue_line("markers", "example: Tests for course examples")


def pytest_collection_modifyitems(config, items):
    """Modify test items during collection."""
    # Add markers based on test location
    for item in items:
        if "test_examples" in item.nodeid or "examples" in item.nodeid:
            item.add_marker("example")
        elif "test_integration" in item.nodeid or "integration" in item.nodeid:
            item.add_marker("integration")
        else:
            item.add_marker("unit")

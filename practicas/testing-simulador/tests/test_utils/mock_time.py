"""
Mock time module for testing ESP-LEGO-SPIKE-Simulator.
Provides simulated timing without actual hardware delays.
"""

import time as _time

# Time constants
_MS_PER_SEC = 1000
_US_PER_SEC = 1000000
_US_PER_MS = 1000

# Track elapsed time for testing
_elapsed_ms = 0


def sleep_ms(ms):
    """Sleep for specified milliseconds.

    Args:
        ms: Milliseconds to sleep
    """
    global _elapsed_ms
    _elapsed_ms += ms


def sleep_us(us):
    """Sleep for specified microseconds.

    Args:
        us: Microseconds to sleep
    """
    global _elapsed_ms
    _elapsed_ms += us / _US_PER_MS


def sleep(seconds):
    """Sleep for specified seconds.

    Args:
        seconds: Seconds to sleep
    """
    global _elapsed_ms
    _elapsed_ms += int(seconds * _MS_PER_SEC)


def ticks_ms():
    """Get current time in milliseconds.

    Returns:
        Current time in milliseconds
    """
    return _elapsed_ms


def ticks_us():
    """Get current time in microseconds.

    Returns:
        Current time in microseconds
    """
    return _elapsed_ms * _US_PER_MS


def ticks():
    """Get current time in milliseconds (alias for ticks_ms).

    Returns:
        Current time in milliseconds
    """
    return _elapsed_ms


def tick_diff(start, end):
    """Calculate difference between two tick values.

    Args:
        start: Start tick value
        end: End tick value

    Returns:
        Difference in milliseconds
    """
    return end - start


def time():
    """Get current Unix timestamp.

    Returns:
        Current Unix timestamp
    """
    return int(_time.time())


def localtime(timestamp=None):
    """Get broken-down local time.

    Args:
        timestamp: Optional Unix timestamp

    Returns:
        Tuple: (year, month, day, hour, minute, second, weekday, yearday)
    """
    if timestamp is None:
        timestamp = time()
    return _time.localtime(timestamp)


def mktime(tuple_time):
    """Convert broken-down time to Unix timestamp.

    Args:
        tuple_time: Time tuple

    Returns:
        Unix timestamp
    """
    return _time.mktime(tuple_time)


def set_elapsed_ms(ms):
    """Set elapsed time (for testing).

    Args:
        ms: Elapsed milliseconds to set
    """
    global _elapsed_ms
    _elapsed_ms = ms


def get_elapsed_ms():
    """Get elapsed time (for testing).

    Returns:
        Elapsed milliseconds
    """
    global _elapsed_ms
    return _elapsed_ms


def reset_time():
    """Reset elapsed time (for testing)."""
    global _elapsed_ms
    _elapsed_ms = 0


# Additional time functions from MicroPython
def ticks_diff(start, end):
    """Calculate ticks difference (same as tick_diff).

    Args:
        start: Start tick value
        end: End tick value

    Returns:
        Difference in milliseconds
    """
    return tick_diff(start, end)


# Module initialization
reset_time()

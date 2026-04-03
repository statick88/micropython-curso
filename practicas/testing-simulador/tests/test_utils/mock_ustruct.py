"""
Mock ustruct module for testing ESP-LEGO-SPIKE-Simulator.
Provides struct module compatibility for MicroPython.
"""

import struct as _struct


# Expose all struct functions and classes
def pack(fmt, *args):
    """Pack values into bytes.

    Args:
        fmt: Format string
        *args: Values to pack

    Returns:
        Packed bytes
    """
    return _struct.pack(fmt, *args)


def pack_into(fmt, buffer, offset, *args):
    """Pack values into buffer.

    Args:
        fmt: Format string
        buffer: Buffer to write to
        offset: Offset to start writing
        *args: Values to pack
    """
    return _struct.pack_into(fmt, buffer, offset, *args)


def unpack(fmt, buffer):
    """Unpack values from buffer.

    Args:
        fmt: Format string
        buffer: Buffer to unpack

    Returns:
        Tuple of unpacked values
    """
    return _struct.unpack(fmt, buffer)


def unpack_from(fmt, buffer, offset=0):
    """Unpack values from buffer at offset.

    Args:
        fmt: Format string
        buffer: Buffer to unpack
        offset: Offset to start unpacking

    Returns:
        Tuple of unpacked values
    """
    return _struct.unpack_from(fmt, buffer, offset)


def calcsize(fmt):
    """Calculate size of packed data.

    Args:
        fmt: Format string

    Returns:
        Size in bytes
    """
    return _struct.calcsize(fmt)


# Aliases for MicroPython compatibility
unpack_from = unpack_from
calcsize = calcsize


# Format codes (compatible with MicroPython)
CalcSize = _struct.calcsize
pack_into = pack_into
unpack = unpack
pack = pack

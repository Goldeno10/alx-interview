#!/usr/bin/env python3
"""UTF-8 Validation module.

Task:
    Write a method that determines if a given data set represents a
      valid UTF-8 encoding.
    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to
      handle the 8 least significant bits of each integer.
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8
    encoding
    """
    def getNumBytes(byte):
        """Count the number of leading '1's in the binary
        representation of the byte"""
        if byte & 0x80 == 0:    # 1-byte character (starts with 0)
            return 1
        elif byte & 0xE0 == 0xC0:  # 2-byte character (starts with 110)
            return 2
        elif byte & 0xF0 == 0xE0:  # 3-byte character (starts with 1110)
            return 3
        elif byte & 0xF8 == 0xF0:  # 4-byte character (starts with 11110)
            return 4
        else:
            return -1  # Invalid byte pattern

    i = 0
    while i < len(data):
        num_bytes = getNumBytes(data[i])
        if num_bytes == -1:  # Invalid byte pattern
            return False

        # Check if the data has enough bytes to form the character
        if i + num_bytes > len(data):
            return False

        # Check if the next bytes are valid continuation bytes
        for j in range(1, num_bytes):
            # Continuation byte should start with 10
            if data[i + j] & 0xC0 != 0x80:
                return False

        i += num_bytes

    return True

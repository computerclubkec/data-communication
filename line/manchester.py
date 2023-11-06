"""
This module contains the function to encode a binary signal using the Manchester encoding scheme.

Example usage:

    >>> signal = Signals("11011101")
    >>> manchester(signal)
    >>> signal.display()
"""
from signals import Signals

def manchester_encode(signal):
    """
    Encodes a binary signal using the Manchester encoding scheme.

    The Manchester encoding scheme represents binary
    1 = -V volt to +V volt transition each of half clock period
    0 = +V volt to -V volt transition each of half clock period

    Args:
        signal (Signals): A Signals object representing the binary signal to be encoded.

    Returns:
        None
    """
    encoded_bits = []
    for bit in signal.get_signal():
        if bit == 1:
            encoded_bits.extend([-1] * Signals.HALF_CLOCK)
            encoded_bits.extend([1] * Signals.HALF_CLOCK)
        else:
            encoded_bits.extend([1] * Signals.HALF_CLOCK)
            encoded_bits.extend([-1] * Signals.HALF_CLOCK)
    signal.set_signal(encoded_bits,"Manchester Encoded")

def manchester_decode(signal):
    """
    This function decodes a signal that was encoded using the Manchester encoding scheme.

    Args:
        signal (Signals): The signal to be decoded.

    Returns:
        None
    """
    decoded_bits =[]
    for bit in signal.get_signal():
        if bit == -1:
            decoded_bits.extend([1] * Signals.ONE_CLOCK)
        else:
            decoded_bits.extend([0] * Signals.ONE_CLOCK)
    signal.set_signal(decoded_bits,"Manchester Decoded")

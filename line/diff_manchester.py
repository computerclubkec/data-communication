"""
Differential Manchester

This module contains the function to encode a binary signal using the Differential Manchester encoding scheme.

Example usage:

    >>> signal = Signals("11011101")
    >>> diff_manchester_encode(signal)
    >>> signal.display()
"""
from signals import Signals

def diff_manchester_encode(signal,previous_bit=0):
    """
    Encodes a binary signal using the Manchester encoding scheme.

    The Manchester encoding scheme represents binary
    1 = -V volt to +V volt transition each of half clock period
    0 = +V volt to -V volt transition each of half clock period
    Inversion when 1 is encountered, No inversion when 0 is encountered

    Args:
        signal (Signals): A Signals object representing the binary signal to be encoded.

    Returns:
        None
    """
    encoded_bits = []
    alt_bit = -1 if previous_bit == 0 else 1
    for bit in signal.get_signal():
        if bit == 1:
            alt_bit = -alt_bit
        encoded_bits.extend([alt_bit] * Signals.HALF_CLOCK)
        encoded_bits.extend([-alt_bit] * Signals.HALF_CLOCK)
    signal.set_signal(encoded_bits, "Encoded Diff Manchester")

def diff_manchester_decode(signal, previous_bit=0):
    """
    This function decodes a signal that was encoded using the Manchester encoding scheme.

    Args:
        signal (Signals): The signal to be decoded.
        previous_bit (int): The previous bit that was used for encoding

    Returns:
        None
    """
    decoded_bits =[]
    for bit in signal.get_signal():
        if bit == previous_bit:
            decoded_bits.extend([0] * Signals.ONE_CLOCK)
        else:
            decoded_bits.extend([1] * Signals.ONE_CLOCK)
        previous_bit = bit
    signal.set_signal(decoded_bits, "Decoded Diff Manchester")

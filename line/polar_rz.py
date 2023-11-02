"""
Polar RZ encoding and decoding.

Example usage:

    >>> signal = Signals("11010101")
    >>> polar_rz_encode(signal)
    >>> signal.display()
"""
from signals import Signals

def polar_rz_encode(signal):
    '''
    Encodes a binary signal using the polar RZ encoding scheme.

    The polar RZ encoding scheme represents a binary 1 as a positive voltage
    for half bit duration and a binary 0 as a negative voltage for half bit duration.

    Args:
        signal (Signals): A Signals object representing the binary signal to be encoded.

    Returns:
        None
    '''

    encoded_bits = []
    for bit in signal.get_signal():
        if bit == 1:
            encoded_bits.extend([1] * Signals.HALF_CLOCK)
            encoded_bits.extend([0] * Signals.HALF_CLOCK)
        else:
            encoded_bits.extend([-1] * Signals.HALF_CLOCK)
            encoded_bits.extend([0] * Signals.HALF_CLOCK)
    signal.set_signal(encoded_bits,"Polar RZ")

def polar_rz_decode(signal):
    '''
    Decodes a binary signal encoded with the polar RZ scheme.

    Args:
        signal (Signals): A Signals object representing the binary signal to be decoded.

    Returns:
        None
    '''
    decoded_bits = []
    for bit in signal.get_signal():
        if bit == 1:
            decoded_bits.extend([1] * Signals.ONE_CLOCK)
        else:
            decoded_bits.extend([0] * Signals.ONE_CLOCK)
    signal.set_signal(decoded_bits,"Decoded Polar RZ")

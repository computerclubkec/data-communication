"""
Bipolar NRZ line code.

Example usage:

    >>> signal = Signals("11011101")
    >>> polar_nrz_encode(signal)
    >>> signal.display()
"""
from signals import Signals

def bipolar_nrz_encode(signal):
    """
    Encodes a binary signal using the bipolar NRZ encoding scheme.

    The bipolar NRZ encoding scheme represents binary
    1 = +V volt and -V volt alternately for one bit duration
    0 = 0 volt

    Args:
        signal (Signals): A Signals object representing the binary signal to be encoded.

    Returns:
        None
    """
    encoded_bits = []
    alt_one = 1 # alternate_ones
    for bit in signal.get_signal():
        if bit == 1:
            encoded_bits.extend([alt_one] * Signals.ONE_CLOCK)
            alt_one *= -1
        else:
            encoded_bits.extend([0] * Signals.ONE_CLOCK)
    signal.set_signal(encoded_bits,"Bipolar NRZ")

def bipolar_nrz_decode(signal):
    """
    This function decodes a signal that was encoded using the Biolar NRZ encoding scheme.

    Args:
        signal (Signals): The signal to be decoded.

    Returns:
        None
    """
    decoded_bits = []
    for bit in signal.get_signal():
        if bit in (1, -1):
            decoded_bits.extend([1] * Signals.ONE_CLOCK)
        else:
            decoded_bits.extend([0] * Signals.ONE_CLOCK)
    signal.set_signal(decoded_bits,"Polar NRZ Decoded")

"""
Unipolar NRZ (Non Return to Zero)

Example usage:

    >>> signal = Signals("11010101")
    >>> unipolar_nrz_encode(signal)
    >>> signal.display()
"""
from signals import Signals

def unipolar_nrz_encode(signal):
    """
    Encodes a binary signal using the unipolar NRZ encoding scheme.

    The unipolar NRZ encoding scheme represents a binary 1 as a positive voltage 
    and a binary 0 as zero voltage.

    Args:
        signal (Signals): A Signals object representing the binary signal to be encoded.

    Returns:
        None
    """
    encoded_bits = []
    for bit in signal.get_signal():
        if bit == 1:
            encoded_bits.extend([1] * Signals.ONE_CLOCK)
        elif bit == 0:
            encoded_bits.extend([0] * Signals.ONE_CLOCK)
    signal.set_signal(encoded_bits,"Unipolar NRZ")

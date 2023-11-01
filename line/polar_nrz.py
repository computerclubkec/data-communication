"""
Polar NRZ

Example usage:

    >>> signal = Signals("11010101")
    >>> polar_nrz_encode(signal)
    >>> signal.display()

"""
from signals import Signals
def polar_nrz_encode(signal):
    """
    Encodes a binary signal using the polar NRZ encoding scheme.

    The polar NRZ encoding scheme represents a binary 1 as a positive voltage 
    and a binary 0 as a negative voltage.

    Args:
        signal (Signals): A Signals object representing the binary signal to be encoded.

    Returns:
        None
    """
    encoded_bits = []
    for bit in signal.get_signal():
        if bit == 1:
            encoded_bits.extend([1] * Signals.ONE_CLOCK)
        else:
            encoded_bits.extend([-1] * Signals.ONE_CLOCK)
    signal.set_signal(encoded_bits,"Polar NRZ")

def polar_nrz_decode(signal):
    """
    This function decodes a signal that was encoded using the Polar NRZ encoding scheme.

    Args:
        signal (Signals): The signal to be decoded.

    Returns:
        None     
    """
    decoded_bits = []
    for bit in signal.get_signal():
        if bit == 1:
            decoded_bits.extend([1] * Signals.ONE_CLOCK)    # pylint: disable=duplicate-code
        else:
            decoded_bits.extend([0] * Signals.ONE_CLOCK)
    signal.set_signal(decoded_bits,"Polar NRZ Decoded")

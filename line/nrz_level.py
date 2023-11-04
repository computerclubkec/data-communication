"""
NRZ Level Encoding and Decoding

Example usage:

        >>> signal = Signals("11011101")
        >>> nrz_level_encode(signal)
        >>> signal.display()

"""
from signals import Signals
def nrz_level_encode(signal):
    """
    Encodes a binary signal using the NRZ Level encoding scheme.

    The NRZ Level encoding scheme represents binary
    1 = -V volt
    0 = +V volt

    Args:
        signal (Signals): A Signals object representing the binary signal to be encoded.

    Returns:
        None
    """
    encoded_bits = []
    for bit in signal.get_signal():
        if bit ==1:
            encoded_bits.extend([-1] * Signals.ONE_CLOCK)
        else:
            encoded_bits.extend([1] * Signals.ONE_CLOCK)
    signal.set_signal(encoded_bits,"NRZ Level")

def nrz_level_decode(signal):
    """
    This function decodes a signal that was encoded using the NRZ Level encoding scheme.

    Args:
        signal (Signals): The signal to be decoded.

    Returns:
        None
    """
    decoded_bits = []
    for bit in signal.get_signal():
        if bit == -1:
            decoded_bits.extend([1] * Signals.ONE_CLOCK)
        else:
            decoded_bits.extend([0] * Signals.ONE_CLOCK)
    signal.set_signal(decoded_bits,"NRZ Level Decoded")

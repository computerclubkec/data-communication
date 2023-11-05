"""
NRZ-Invert Line Coding

Example usage:

    >>> signal = Signals("11011101")
    >>> nrz_invert_encode(signal)
    >>> signal.display()
"""
from signals import Signals

def nrz_invert_encode(signal, previous_bit=1):
    """
    Encodes a binary signal using the NRZ Invert encoding scheme.

    The bipolar NRZ encoding scheme represents binary
    1 = Transition from +V volts to –V volts or vice-versa
    0 = No transition (i.e. as it is of previous bit),

    Args:
        signal (Signals): A Signals object representing the binary signal to be encoded.
        previous_bit (int): The previous bit before the actual data bits. Defaults to 1.

    Returns:
        None
    """
    encoded_bits = []
    alt_bit = previous_bit if previous_bit == 1 else -1
    for bit in signal.get_signal():
        if bit == 1:
            alt_bit = -alt_bit
            encoded_bits.extend([alt_bit] * Signals.ONE_CLOCK)
        else:
            encoded_bits.extend([alt_bit] * Signals.ONE_CLOCK)
    signal.set_signal(encoded_bits,"NRZ Invert Encoded")

def nrz_invert_decode(signal, previous_bit=1):
    """
    This function decodes a signal that was encoded using the NRZ Invert encoding scheme.

    Args:
        signal (Signals): The signal to be decoded.
        previous_bit (int): The previous bit that was used for encoding.
        
    Returns:
        None
    """
    decoded_bits = []
    alt_bit = previous_bit if previous_bit == 1 else -1
    for bit in signal.get_signal():
        if bit == alt_bit:
            decoded_bits.extend([1] * Signals.ONE_CLOCK)
        else:
            decoded_bits.extend([0] * Signals.ONE_CLOCK)
            alt_bit = -alt_bit
    signal.set_signal(decoded_bits,"NRZ Invert Decoded")

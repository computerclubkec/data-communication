"""
Unipolar RZ (Return to Zero)

Example usage:

    >>> signal = Signals("11010101")
    >>> unipolar_rz_encode(signal)
    >>> signal.display()
"""

from signals import Signals

def unipolar_rz_encode(signal):
    '''
    Encode a binary signal using the unipolar RZ encoding scheme.

    The unipolar RZ encoding scheme represents a binary 1 as a positive voltage
    for half bit duration and a binary 0 as zero voltage.

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
            encoded_bits.extend([0] * Signals.ONE_CLOCK)
    signal.set_signal(encoded_bits, "Unipolar RZ")

def unipolar_rz_decode(signal):
    '''
    Decode a binary signal encoded with the unipolar RZ scheme.

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
    signal.set_signal(decoded_bits, "Decoded Unipolar RZ")

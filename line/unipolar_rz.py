'''
This module provides functions for encoding and decoding binary signals using the unipolar RZ encoding scheme.

The unipolar RZ (Return to Zero) encoding scheme represents a binary 1 as a positive voltage for half bit duration 
and a binary 0 as zero voltage for the entire bit duration.

This module imports the `Signals` class from the `signals` module to represent binary signals.

Example usage:

    >>> signal = Signals("11010101")
    >>> unipolar_rz_encode(signal)
    >>> signal.display()
    Signal type: Unipolar RZ
    Signal data: [1, 0, 1, 0, 1, 0, 1, 0]
'''
from signals import Signals

def unipolar_rz_encode(signal):
    '''
    Encodes a binary signal using the unipolar RZ encoding scheme.

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
    signal.set_signal(encoded_bits,"Unipolar RZ")


def unipolar_rz_decode(signal):

    decoded_bits = []
    for bit in signal.get_signal():
        if bit == 1:
            encoded_bits.append(1)
        else:
            encoded_bits.append(0)
    signal.set_signal(encoded_bits, "NRZ", "Decoded Unipolar RZ")

"""
This module provides functions for encoding and decoding binary signals
using the unipolar NRZ encoding scheme.

This module imports the `Signals` class from the `signals` module to represent binary signals.

Example usage:

    >>> signal = Signals("11010101")
    >>> unipolar_nrz_encode(signal)
    >>> signal.display()
    Signal type: Unipolar NRZ
    Signal data: [1, 0, 1, 0, 1, 0, 1, 0]

This will create a `Signals` object with a binary signal,
encode and decode the signal using the unipolar NRZ encoding scheme,
and display the encoded and decoded signal as a digital waveform.

"""

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
            encoded_bits.append(1)
        else:
            encoded_bits.append(0)
    
    signal.set_signal(encoded_bits,"Unipolar NRZ")
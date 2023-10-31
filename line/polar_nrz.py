"""
This module provides functions for encoding and decoding binary signals
using the polar NRZ encoding scheme.

This module imports the `Signals` class from the `signals` module to represent binary signals.

Example usage:

    >>> signal = Signals("11010101")
    >>> polar_nrz_encode(signal)
    >>> signal.display()
    Signal type: Polar NRZ
    Signal data: [1, -1, 1, -1, 1, -1, 1, -1]

This will create a `Signals` object with a binary signal,
encode and decode the signal using the polar NRZ encoding scheme,
and display the encoded and decoded signal as a digital waveform.

"""

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
            encoded_bits.append(1)
        else:
            encoded_bits.append(-1)
    
    signal.set_signal(encoded_bits,"Polar NRZ")


def polar_nrz_decode(signal):
    """
    This function decodes a signal that was encoded using the Polar NRZ encoding scheme.

    In this scheme, a binary 1 is represented as a positive voltage and a binary 0 as a negative voltage.
    This function takes a Signals object as input, which should have a method get_signal that returns the 
    encoded signal, and a method set_signal that sets the decoded signal.

    Parameters:
        signal (Signals): The signal to be decoded.

    Example:
        signal = Signals([1, -1, 1, 1, -1])
        polar_nrz_decode(signal)
    """
    decoded_bits = []
    for bit in signal.get_signal():
        if bit == 1:
            decoded_bits.append(1)
        else:
            decoded_bits.append(0)

    signal.set_signal(decoded_bits,"Polar NRZ Decoded")



"""
This module provides a class for Signals.

The Signals class is used to represent binary signals and display them.

Example:
    >>> signal = Signals('0101010101')
    >>> signal.display()
"""
import numpy as np
import matplotlib.pyplot as plt


class Signals:
    """
    A class for digital signals.

    Attributes:
        name (str): The name of the signal
        original_signal (str): The original signal as a string.
        signal (list of int): The signal as a list of integer values (0 or 1).
    
    Methods:
        get_signal: Get the signal as a list of bits.
        display: Display the signal as a waveform.
    """

    ONE_CLOCK = 1000
    HALF_CLOCK = 500

    def __init__(self, signal:str) -> None:
        """
        Initialize a Signals object.

        Args:
            signal (str): A binary signal represented as a string of 0s and 1s.
        """
        self.name = "Original Signal"
        self.intial_bits = [int(bit) for bit in signal]
        self.bits = self.intial_bits
        self.bits_len = len(self.bits)
        self.bits_duration = np.linspace(0,self.bits_len, self.bits_len * self.ONE_CLOCK, endpoint=False)
        self.signal = [int(bit) for bit in signal for _ in range(self.ONE_CLOCK)]
        

    def get_signal(self) -> list:
        """
        Get the signal as a list of bits.

        Returns:
            list of int: The signal as a list of integer values (0 or 1).
        """
        return self.bits

    def set_signal(self, signal, name):
        '''
        Set the signal to a new list of bits.

        This method sets the signal to a new list of bits and updates the name of the signal.

        Args:
            signal (list of int): The new signal as a list of integer values (0 or 1).
            d_type (str): The duration type. Either RZ or NRZ.
            name (str): The name of the new signal.

        Returns:
            None
        '''
        self.name = name
        self.signal = signal

    def restore_signal(self) -> list:
        '''
        Restore the signal to its original state.

        This method restores the signal to its original states
        by setting the signal to the original signal and updating the name of the signal.

        Returns:
            None
        '''
        self.name = "Original Signal"
        self.signal = self.intial_bits

    def display(self) -> None:
        """
        Display the signal as a waveform.

        This function plots the binary signal as a digital waveform.

        Returns:
            None
        """
        plt.figure()
        plt.plot(self.bits_duration,self.signal)
        plt.grid(True)
        plt.xticks(range(0,len(self.bits)+1))
        plt.yticks([-1,0,1])
        plt.title(f"{self.name} for: {self.intial_bits}")
        plt.show()

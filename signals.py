"""
This module provides a class for Signals.

Author: Gaurav Giri
Date: November 1, 2023
"""

import numpy as np
import matplotlib.pyplot as plt

class Signals:
    """
    A class for generating and manipulating digital signal representations.

    Attributes:
        ONE_CLOCK (int): Constant representing one clock cycle's duration in samples (default: 1000).
        HALF_CLOCK (int): Constant representing half a clock cycle's duration in samples (default: 500).
        name (str): The name of the signal.
        initial_bits (list): The original binary signal as a list of integers.
        bits (list): The current binary signal as a list of integers.
        bits_len (int): The length of the binary signal.
        bits_duration (numpy.ndarray): The time duration of the binary signal.
        signal (list): The binary signal as a list of integers, where each bit lasts for ONE_CLOCK duration.

    Methods:
        __init__(self, signal: str) -> None:
            Initialize a Signals object with an initial binary signal string.

        get_signal(self) -> list:
            Get the current binary signal as a list of bits.

        set_signal(self, signal, name):
            Set the binary signal to a new one and assign a name to the signal.

        restore_signal(self) -> None:
            Restore the original binary signal and reset its name.

        display(self) -> None:
            Display a plot of the binary signal with timestamps and labels.
    """
    ONE_CLOCK = 1000
    HALF_CLOCK = 500

    def __init__(self, signal: str) -> None:
        """
        Initialize a Signals object.

        Args:
            signal (str): A binary signal represented as a string of '0's and '1's.
        """
        self.name = "Original Signal"
        self.intial_bits = [int(bit) for bit in signal]
        self.bits = self.intial_bits
        self.bits_len = len(self.bits)
        self.bits_duration = np.linspace(0, self.bits_len, self.bits_len * self.ONE_CLOCK, endpoint=False)
        self.signal = [int(bit) for bit in signal for _ in range(self.ONE_CLOCK)]

    def get_signal(self) -> list:
        """
        Get the current binary signal as a list of bits.

        Returns:
            list: A list containing the binary bits of the current signal.
        """
        return self.bits

    def set_signal(self, signal, name):
        """
        Set the binary signal to a new one and assign a name to the signal.

        Args:
            signal: A new binary signal.
            name (str): A name to associate with the signal.

        Returns:
            None
        """
        self.name = name
        self.signal = signal
        self.bits = []
        for bit in range(0,len(self.signal),self.ONE_CLOCK):
            self.bits.append(self.signal[bit])

    def restore_signal(self) -> None:
        """
        Restore the original binary signal and reset its name.

        Returns:
            None
        """
        self.name = "Original Signal"
        self.signal = self.intial_bits

    def display(self, show=True) -> plt.figure:
        """
        Display a plot of the binary signal with timestamps and labels.

        Returns:
           matplotlib figure 
        """
        fig = plt.figure()
        plt.plot(self.bits_duration, self.signal)
        plt.grid(True)
        plt.xticks(range(0, len(self.bits) + 1))
        plt.yticks([-1, 0, 1])
        plt.title(f"{self.name} for: {self.intial_bits}")
        if show:
            plt.show()
        return fig

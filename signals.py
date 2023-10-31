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
        duriation_type (str): The signal duration for a bit, 
                                either Return to Zero (RZ) or Non-Return to Zero (NRZ)
    
    Methods:
        get_signal: Get the signal as a list of bits.
        display: Display the signal as a waveform.
    """

    def __init__(self, signal:str) -> None:
        """
        Initialize a Signals object.

        Args:
            signal (str): A binary signal represented as a string of 0s and 1s.
        """
        self.name = "Original Signal"
        self.original_signal = signal
        self.signal = [int(bit) for bit in signal]
        self.duration_type = "NRZ"

    def get_signal(self) -> list:
        """
        Get the signal as a list of bits.

        Returns:
            list of int: The signal as a list of integer values (0 or 1).
        """
        return self.signal

    def set_signal(self, signal, duration, name):
        '''
        Set the signal to a new list of bits.

        This method sets the signal to a new list of bits and updates the name of the signal.

        Args:
            signal (list of int): The new signal as a list of integer values (0 or 1).
            duration (str): The duration type. Either RZ or NRZ.
            name (str): The name of the new signal.

        Returns:
            None
        '''
        self.name = name
        self.duration_type = duration
        self.signal = [int(bit) for bit in signal]

    def restore_signal(self) -> list:
        '''
        Restore the signal to its original state.

        This method restores the signal to its original states
        by setting the signal to the original signal and updating the name of the signal.

        Returns:
            None
        '''
        self.name = "Original Signal"
        self.signal = self.original_signal

    def display(self) -> None:
        """
        Display the signal as a waveform.

        This function plots the binary signal as a digital waveform.

        Returns:
            None
        """
        if self.duration_type == "NRZ":
            x_axis = np.repeat(range(len(self.signal)), 2)
        else:
            x_axis = np.arange(0,len(self.signal)/2,0.5)
            x_axis = np.repeat(x_axis,2)
        y_axis = np.repeat(self.signal, 2)
        x_axis = x_axis[1:]
        y_axis = y_axis[:-1]
        x_axis = np.append(x_axis, x_axis[-1] + 1)
        y_axis = np.append(y_axis, y_axis[-1])
        plt.xticks(range(len(self.signal)+1))
        plt.yticks([-1,0,1])
        plt.ylim(-1.1,1.1)
        plt.plot(x_axis, y_axis)
        plt.grid(linewidth=0.5)
        plt.title(f"{self.name}: {self.signal}")
        plt.tight_layout()
        plt.show()

import numpy as np
import matplotlib.pyplot as plt

class Signals:
    """
    A class for displaying signals.

    Attributes:
        original_signal (str): The original signal as a string.
        signal (list of int): The signal as a list of integer values (0 or 1).
    """

    def __init__(self, signal):
        """
        Initialize a Signals object.

        Args:
            signal (str): A binary signal represented as a string of 0s and 1s.
        """
        self.original_signal = signal
        self.signal = [int(bit) for bit in signal]

    def display(self):
        """
        Display the signal as a waveform.

        This function plots the binary signal as a digital waveform.

        Returns:
            None
        """
        x_axis = np.repeat(range(len(self.signal)), 2)
        y_axis = np.repeat(self.signal, 2)
        x_axis = x_axis[1:]
        y_axis = y_axis[:-1]
        x_axis = np.append(x_axis, x_axis[-1] + 1)
        y_axis = np.append(y_axis, y_axis[-1])
        plt.xticks(range(len(self.signal)+1))
        plt.yticks([0,1])
        plt.ylim(-0.1,1.1)
        plt.plot(x_axis, y_axis)
        plt.grid(linewidth=0.5)
        plt.title(self.original_signal)
        plt.tight_layout()
        plt.show()

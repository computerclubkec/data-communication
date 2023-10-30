"""
This is the main driver code for the data-communication project.

Example usage:

    $ python main.py

"""

from .signals import Signals
from .line.unipolar_nrz import unipolar_nrz_encode

def main():
    """
    Main function to run any encoding and decoding modules.

    Returns:
        None
    """
    signal = Signals("11011100111")
    signal.display()
    unipolar_nrz_encode(signal)
    signal.display()

if __name__ == "__main__":
    main()

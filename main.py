"""
This is the main driver code for the data-communication project.

Example usage:

    $ python main.py

"""
from signals import Signals
from line.nrz_level import nrz_level_encode, nrz_level_decode

def main():
    """
    Main function to run any encoding and decoding modules.

    Returns:
        None
    """
    signal = Signals("101001110")
    signal.display()
    nrz_level_encode(signal)
    signal.display()
    print(signal.bits)
    nrz_level_decode(signal)
    signal.display()
if __name__ == "__main__":
    main()

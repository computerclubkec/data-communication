"""
This is the main driver code for the data-communication project.

Example usage:

    $ python main.py

"""
from signals import Signals
from line.bipolar_nrz import bipolar_nrz_encode,bipolar_nrz_decode

def main():
    """
    Main function to run any encoding and decoding modules.

    Returns:
        None
    """
    signal = Signals("101001110")
    signal.display()
    bipolar_nrz_encode(signal)
    signal.display()
    print(signal.bits)
    bipolar_nrz_decode(signal)
    signal.display()
if __name__ == "__main__":
    main()

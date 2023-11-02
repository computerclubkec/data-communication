"""
This is the main driver code for the data-communication project.

Example usage:

    $ python main.py

"""
from signals import Signals
from line.bipolar_rz import bipolar_rz_encode,bipolar_rz_decode

def main():
    """
    Main function to run any encoding and decoding modules.

    Returns:
        None
    """
    signal = Signals("101001110")
    signal.display()
    bipolar_rz_encode(signal)
    signal.display()
    print(signal.bits)
    bipolar_rz_decode(signal)
    signal.display()
if __name__ == "__main__":
    main()

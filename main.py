"""
This is the main driver code for the data-communication project.

Example usage:

    $ python main.py

"""
from signals import Signals
from line.nrz_invert import nrz_invert_encode, nrz_invert_decode

def main():
    """
    Main function to run any encoding and decoding modules.

    Returns:
        None
    """
    signal = Signals("010010110110")
    signal.display()
    nrz_invert_encode(signal,0)
    signal.display()
    nrz_invert_decode(signal,0)
    signal.display()
    
if __name__ == "__main__":
    main()

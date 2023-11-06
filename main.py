"""
This is the main driver code for the data-communication project.

Example usage:

    $ python main.py

"""
from signals import Signals
from line.manchester import manchester_encode, manchester_decode

def main():
    """
    Main function to run any encoding and decoding modules.

    Returns:
        None
    """
    signal = Signals("010010110110")
    signal.display()
    manchester_encode(signal)
    signal.display()
    manchester_decode(signal)
    signal.display()
    
if __name__ == "__main__":
    main()

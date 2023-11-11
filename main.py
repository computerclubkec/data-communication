"""
This is the main driver code for the data-communication project.

Example usage:

    $ python main.py

"""
from signals import Signals
from line.diff_manchester import diff_manchester_encode,diff_manchester_decode

def main():
    """
    Main function to run any encoding and decoding modules.

    Returns:
        None
    """
    signal = Signals("10110010")
    signal.display()
    diff_manchester_encode(signal)
    signal.display()
    diff_manchester_decode(signal)
    signal.display()
    
if __name__ == "__main__":
    main()

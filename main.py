"""
This is the main driver code for the data-communication project.

Example usage:

    $ python main.py

"""
from signals import Signals
from line.polar_rz import polar_rz_encode,polar_rz_decode

def main():
    """
    Main function to run any encoding and decoding modules.

    Returns:
        None
    """
    signal = Signals("1011")
    signal.display()
    polar_rz_encode(signal)
    signal.display()
    polar_rz_decode(signal)
    signal.display()

if __name__ == "__main__":
    main()

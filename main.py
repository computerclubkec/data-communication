from signals import Signals

def main():
    """
    Main function to demonstrate the Signals class.

    This function creates a Signals object with a binary signal,
    then displays the signal as a digital waveform.

    Returns:
        None
    """
    signal = Signals("11011100111")
    signal.display()

if __name__ == "__main__":
    main()

print("Starting main.py")
import time
print("Imported time")
from muselsl import stream, list_muses
print("Imported muselsl")
from eeg_processor import EEGProcessor
print("Imported EEGProcessor")
from spotify_controller import SpotifyController
print("Imported SpotifyController")

def main():
    print("Entering main function")
    # ... rest of your code ...

if __name__ == "__main__":
    print("Starting main execution")
    main()

import time
from muselsl import stream, list_muses
from eeg_processor import EEGProcessor
from spotify_controller import SpotifyController

def main():
    # Find and connect to Muse device
    muses = list_muses()
    if not muses:
        print("No Muse devices found")
        return
    
    # Start streaming
    stream(muses[0]['address'])
    
    # Initialize EEG processor and Spotify controller
    eeg_processor = EEGProcessor()
    spotify_controller = SpotifyController()
    
    try:
        while True:
            # Process EEG data
            command = eeg_processor.process_and_classify()
            
            # Control Spotify based on the command
            if command:
                spotify_controller.execute_command(command)
            
            time.sleep(0.1)  # Small delay to prevent overwhelming the CPU
    except KeyboardInterrupt:
        print("Stopping...")

if __name__ == "__main__":
    main()
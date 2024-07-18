from pylsl import StreamInlet, resolve_stream
import numpy as np

class EEGProcessor:
    def __init__(self):
        print("Initializing EEG Processor...")
        streams = resolve_stream('type', 'EEG')
        self.inlet = StreamInlet(streams[0])

    def process_and_classify(self):
        chunk, timestamps = self.inlet.pull_chunk()
        if chunk:
            print(f"Received EEG data: {chunk[:5]}...")  # Print first 5 data points
            # Process your data here
            # For now, just return a random command
            return np.random.choice(['next_track', 'previous_track', 'pause', 'play'])
        else:
            print("No data received")
        return None
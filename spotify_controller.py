import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyController:
    def __init__(self):
        # Set up Spotify API connection
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id="6d650633301b42b894016b1346a78e06",
            client_secret="28dd88fb81c4800a12d3ee8c0bc0e7d",
            redirect_uri="http://localhost:8888/callback",
            scope="user-modify-playback-state,user-read-playback-state"
        ))

    def execute_command(self, command):
        if command == 'next_track':
            self.sp.next_track()
        elif command == 'previous_track':
            self.sp.previous_track()
        elif command == 'pause':
            self.sp.pause_playback()
        elif command == 'play':
            self.sp.start_playback()
        else:
            print(f"Unknown command: {command}")
import spotipy, json, logging
from connect_spotify import ConnectSpotify

import requests
import secrets

logger = secrets.logger

class PlaySong(ConnectSpotify):

    def get_songs_from_playlist(self):
        # use playlist_items() to get tracks from the playlist, then add those to the queue
        playlist_id = secrets.PLAYLIST_ID
        songs = self.spotifyObject.playlist_items(playlist_id)


        for song in songs['items']:
            self.queue[song['track']['name']] = song['track']['id']
        
        logger.info("Successfully got songs Good Morning in 2034")


    def add_to_queue(self):
        # iter thru dict and add to queue 
        for song in self.queue:

            self.spotifyObject.add_to_queue(self.queue[song])
            logger.info((" Added '{}' to queue").format(song))


    def play_track(self):
        # transfer_playback to mac - starts playing the song
        self.spotifyObject.transfer_playback(device_id=self.device_id)

        # next_track, skips the song currently playing
        self.spotifyObject.next_track()
        




    





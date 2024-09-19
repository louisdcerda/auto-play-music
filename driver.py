#!/usr/bin/env python3

from play_song import PlaySong
from speaker_connect import SpeakerConnect


class Driver:

    def connect_and_play(self):

        # connects and plays song class
        player = PlaySong()
        # speaker connection class
        speaker_connection = SpeakerConnect()


        # sign in and play songs from playlist
        player.spotify_sign_in()

        player.get_songs_from_playlist()
        player.add_to_queue()
        player.play_track()


if __name__ == "__main__":
    play = Driver()
    play.connect_and_play()

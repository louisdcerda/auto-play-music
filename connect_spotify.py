import json 
import spotipy 
import webbrowser
from spotipy.oauth2 import SpotifyOAuth
import secrets


class ConnectSpotify:
    def __init__(self):

        self.__username = secrets.USERNAME
        self.__clientID = secrets.CLIENT_ID
        self.__clientSecret = secrets.CLIENT_SECRET
        self.__redirect_uri = secrets.REDIRECT_URL
        self.scope = "user-read-playback-state user-modify-playback-state user-read-currently-playing"
        self.user_name = None
        self.spotifyObject = None
        self.queue = {}
        self.token = None
        self.device_id =  secrets.DEVICE_ID # mac

    def spotify_sign_in(self):
        oauth_object = spotipy.SpotifyOAuth(self.__clientID, self.__clientSecret, self.__redirect_uri, scope=self.scope) 
        token_dict = oauth_object.get_access_token() 
        self.token = token_dict['access_token'] 
        self.spotifyObject = spotipy.Spotify(auth=self.token) 
        self.user_name = self.spotifyObject.current_user() 

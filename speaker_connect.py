import subprocess, logging
from os import system
import secrets 

logger = secrets.logger

class SpeakerConnect:
    def __init__(self):
        self.mac_addy = secrets.MAC_ADDY

    def connect_to_speakers(self):
        connect_command = "BluetoothConnector --connect {}".format(self.mac_addy)
        system(connect_command)

        logger.info("Successfully Connected to boom boom machine")

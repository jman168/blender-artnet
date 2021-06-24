import bpy
from threading import Lock 

class ChannelManager:
    def __init__(self):
        self._data = {}
        self._mutex = Lock()

    def ingest_data(self, universe, channels, channel_data):
        with self._mutex:
            if(universe not in self._data):
                self._data.update({universe: channel_data})
            elif(channels >= len(self._data[universe])):
                self._data[universe] = channel_data
            else:
                self._data[:channels] = channel_data
    
    def get_data(self):
        with self._mutex:
            return self._data
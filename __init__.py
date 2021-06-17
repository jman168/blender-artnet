from .src.ArtNetSocket import ArtNetSocket
from .src.ChannelManager import ChannelManager

bl_info = {
    "name": "Blender Art-Net",
    "description": "A blender plugin for controling lights via the Art-Net protocol.",
    "author": "Jason Beckmann",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "category": "Lighting",
}

socket = None
channel_manager = None

def register():
    global socket
    channel_manager = ChannelManager()
    socket = ArtNetSocket(channel_manager)

def unregister():
    global socket
    socket.disconnect()
    socket.shutdown()
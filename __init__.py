from .src.ArtNetSocket import ArtNetSocket
from .src.ChannelManager import ChannelManager
from .src.BlenderSync import BlenderSync

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
blender_sync = None

def register():
    global socket
    channel_manager = ChannelManager()
    blender_sync = BlenderSync(channel_manager)
    socket = ArtNetSocket(channel_manager)

def unregister():
    global socket
    socket.disconnect()
    socket.shutdown()
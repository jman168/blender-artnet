from .src.ArtNetSocket import ArtNetSocket

bl_info = {
    "name": "Blender Art-Net",
    "description": "A blender plugin for controling lights via the Art-Net protocol.",
    "author": "Jason Beckmann",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "category": "Lighting",
}

socket = None

def register():
    global socket
    socket = ArtNetSocket()

def unregister():
    global socket
    socket.disconnect()
    socket.shutdown()
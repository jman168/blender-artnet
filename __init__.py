import bpy
from bpy.types import  Light
from bpy.props import BoolProperty, IntProperty, EnumProperty

from .src.ArtNetSocket import ArtNetSocket
from .src.ChannelManager import ChannelManager
from .src.BlenderSync import BlenderSync
from .src.ui.UI import UI_Panel

COLOR_TYPE_TARGETS = [
    ('dim', 'Dimmer', 'Single channel dimmer color mixing', 0),
    ('rgb', 'RGB', 'Red, Green, Blue color mixing', 1),
    ('rgba', 'RGBA', 'Red, Green, Blue, Amber color mixing', 2),
    ('rgbw', 'RGBW', 'Red, Green, Blue, White color mixing', 3)
]

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
    
    register_light_properties()

    channel_manager = ChannelManager()
    blender_sync = BlenderSync(channel_manager)
    socket = ArtNetSocket(channel_manager)

    bpy.utils.register_class(UI_Panel)

def unregister():
    global socket
    socket.disconnect()
    socket.shutdown()

def register_light_properties():
    Light.artnet_enabled: BoolProperty = BoolProperty(
        name="Enabled",
    )

    Light.artnet_universe: IntProperty = IntProperty(
        name="Universe",
    )

    Light.artnet_channel: IntProperty = IntProperty(
        name="DMX Channel",
    )

    Light.artnet_color_type: EnumProperty = EnumProperty(
        name="Color Type",
        items=COLOR_TYPE_TARGETS,
        default="dim",
    )

    Light.artnet_dimmer_channel: IntProperty = IntProperty(
        name="Dimmer Channel",
    )
    Light.artnet_red_channel: IntProperty = IntProperty(
        name="Red Channel",
    )
    Light.artnet_green_channel: IntProperty = IntProperty(
        name="Green Channel",
    )
    Light.artnet_blue_channel: IntProperty = IntProperty(
        name="Blue Channel",
    )
    Light.artnet_white_channel: IntProperty = IntProperty(
        name="White Channel",
    )
    Light.artnet_amber_channel: IntProperty = IntProperty(
        name="Amber Channel",
    )

    Light.artnet_master_dimmer: BoolProperty = BoolProperty(
        name="Master Dimmer",
    )
    Light.artnet_master_dimmer_channel: IntProperty = IntProperty(
        name="Master Dimmer Channel",
    )
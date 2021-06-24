import bpy
import math
import time

class BlenderSync:
    def __init__(self, channel_manager):
        self._channel_manager = channel_manager
        bpy.app.timers.register(self._update_blender, persistent=True)

    def _update_blender(self):
        channel_data = self._channel_manager.get_data()

        for light in bpy.data.lights:
            if light.artnet_enabled:
                if light.artnet_universe in channel_data:
                    uni = light.artnet_universe
                    if light.artnet_color_type == "dim":
                        if light.artnet_master_dimmer_channel < len(channel_data[uni]):
                            light.color = (channel_data[uni][light.artnet_master_dimmer_channel]/255.0, channel_data[uni][light.artnet_master_dimmer_channel]/255.0, channel_data[uni][light.artnet_master_dimmer_channel]/255.0)
                    


        return 0.02

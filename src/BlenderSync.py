import bpy
import math
import time

class BlenderSync:
    def __init__(self, channel_manager):
        self._channel_manager = channel_manager
        bpy.app.timers.register(self._update_blender, persistent=True)

    def _update_blender(self):
        channel_data = self._channel_manager.get_data()

        if 0 in channel_data and len(channel_data[0])>=3:
            for light in bpy.data.lights:
                light.color = (channel_data[0][0]/255.0, channel_data[0][1]/255.0, channel_data[0][2]/255.0)
        return 0.033333333

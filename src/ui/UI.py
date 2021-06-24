import bpy


class UI_Panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_blender_artnet"
    bl_label = "Blender ArtNet"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        if context.object.type != 'LIGHT':
            return False
        return (context.object is not None)

    def draw_header(self, context):
        layout = self.layout
        layout.prop(context.object.data, "artnet_enabled", text="")

    def draw(self, context):
        layout = self.layout
        data = context.object.data
        if not data.artnet_enabled:
            return

        layout.prop(data, "artnet_universe")
        layout.prop(data, "artnet_channel")

        box = layout.box()
        box.prop(data, "artnet_color_type")
        if data.artnet_color_type == "dim":
            box.prop(data, "artnet_dimmer_channel")
        if data.artnet_color_type == "rgb":
            box.prop(data, "artnet_red_channel")
            box.prop(data, "artnet_green_channel")
            box.prop(data, "artnet_blue_channel")
        if data.artnet_color_type == "rgba":
            box.prop(data, "artnet_red_channel")
            box.prop(data, "artnet_green_channel")
            box.prop(data, "artnet_blue_channel")
            box.prop(data, "artnet_amber_channel")
        if data.artnet_color_type == "rgbw":
            box.prop(data, "artnet_red_channel")
            box.prop(data, "artnet_green_channel")
            box.prop(data, "artnet_blue_channel")
            box.prop(data, "artnet_white_channel")

        box = layout.box()
        box.prop(data, "artnet_master_dimmer")
        if data.artnet_master_dimmer:
            box.prop(data, "artnet_master_dimmer_channel")
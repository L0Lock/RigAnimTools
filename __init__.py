# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

bl_info = {
        "name": "Rigging Tools",
        "description": "A regroupment of little tools to automate redundant and boring rigging tasks (isn't that what programs are made for in the first place ?).",
        "author": "-L0Lock-",
        "version": (0, 2),
        "blender": (2, 80, 0),
        "location": "Pose Mode > Sidebar > RiggingTools tab",
        "warning": "made by a python noob",
        "wiki_url": "https://github.com/L0Lock/RiggingTools",
        "tracker_url": "https://github.com/L0Lock/RiggingTools/issues",
        "support": "COMMUNITY",
        "category": "Rigging"
        }

import bpy

from . Reset_Stretch_To import RGT_OT_Reset_Stretch_To
from . Set_Inverse_Child_Of import RGT_OT_Set_Inverse_Child_Of

class VIEW3D_MT_pose_riggingtools(bpy.types.Panel):
    bl_idname = "POSE_MT_rigging_tools"
    bl_label = "RiggingTools"
    bl_category = "RiggingTools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "posemode"


    def draw(self, context):
        layout = self.layout

        layout.operator("view3d.reset_stretch_to")
        layout.operator("view3d.set_inverse_child_of")

classes = (RGT_OT_Reset_Stretch_To, RGT_OT_Set_Inverse_Child_Of, VIEW3D_MT_pose_riggingtools)

register, unregister = bpy.utils.register_classes_factory(classes)


# bpy.ops.script.python_file_run(filepath="")
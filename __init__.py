# ##### GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

bl_info = {
        "name": "Rigging Tools",
        "description": "A regroupment of little tools to automate redundant and boring rigging tasks (isn't that what programs are made for in the first place ?).",
        "author": "-L0Lock-",
        "version": (0, 1),
        "blender": (2, 79),
        "location": "Pose Mode > Specials Menu",
        "warning": "made by a python noob",
        "wiki_url": "https://github.com/L0Lock/Blender-Stuff/tree/master/Addons/Rigging_Tools",
        "tracker_url": "https://github.com/L0Lock/Blender-Stuff/issues",
        "support": "COMMUNITY",
        "category": "Rigging"
        }

import bpy

#
# Add additional functions here
#

def register():
    from . import Reset_Stretch_To
    from . import Set_Inverse_Child_Of
    properties.register()
    ui.register()

def unregister():
    from . import Reset_Stretch_To
    from . import Set_Inverse_Child_Of
    properties.unregister()
    ui.unregister()

if __name__ == '__main__':
    register()

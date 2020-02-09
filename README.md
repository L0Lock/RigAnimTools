# RigAnim Tools

[![GitHub license](https://img.shields.io/github/license/L0Lock/RigAnimTools?style=for-the-badge)](https://github.com/L0Lock/RigAnimTools/blob/master/LICENSE.md)

RigAnim Tools (or RAT) is a regroupment of little tools to automate redundant and boring tasks (isn't that what programs are made for in the first place ?) or make your life easyier, for rigging and animation.

# Installation
- Download the latset release on [the release page](https://github.com/L0Lock/RigAnimTools/releases), or download the entire repository using the big green button on the top-right corned of this page. You will obtain an archive file (usually `.zip` or `.7z`).
- In Blender, go to Edit → Preferences, then in the Add-ons tab click the Install button an navigate to the downloaded .zip and double-click it
- Enable the addon via its checkbox on the top-left corner.

You will find the addon's content in the viewport's sidebar while in pose mode:

![location of the addon](https://i.imgur.com/PSKIGQc.png)

# List of tools
**Reset: Stretch To**
In pose mode, resets every "Stretch To" constraint in the armature.
>**From the [Blender Manual](https://docs.blender.org/manual/en/latest/animation/constraints/relationship/child_of.html?highlight=set%20inverse#options)**:
>[This] will recalculate the Rest Length value, so that it corresponds to the actual distance between the owner and its target (i.e. the distance before this constraint is applied).

**Set Inverse: Child Of**
 In pose mode, sets the inverse of every "Child Of" constraint in the armature.
>**From the [Blender Manual](https://docs.blender.org/manual/en/latest/animation/constraints/relationship/child_of.html?highlight=set%20inverse#options)**:
>By default, when you parent your owner to your target, the target becomes the origin of the owner’s space. This means that the location, rotation and scale of the owner are offset by the same properties of the target. In other words, the owner is transformed when you parent it to your target. This might not be desired! So, if you want to restore your owner to its before-parenting state, click on the Set Inverse button.


**Clear Inverse: Child Of**
 In pose mode, clears the inverse of every "Child Of" constraint in the armature.
>**From the [Blender Manual](https://docs.blender.org/manual/en/latest/animation/constraints/relationship/child_of.html?highlight=set%20inverse#options)**:
>This button reverses (cancels) the effects of the above one, restoring the owner/child to its default state regarding its target/parent.

## Trunk

![image](../img/parts_chest.JPG)

Motors list:

| Sub-assembly name |   Motor name   |   Type  | ID |
|-------------------|:--------------:|:-------:|:--:|
| Double MX64       |     abs\_y     | MX-64AT | 31 |
| Double MX64       |     abs\_x     | MX-64AT | 32 |
| Spine             |     abs\_z     | MX-28AT | 33 |
| Double MX28       |     bust\_y    | MX-28AT | 34 |
| Double MX28       |     bust\_x    | MX-28AT | 35 |
| Chest             |     head\_z    |  AX-12A | 36 |
| Chest             | l\_shoulder\_y | MX-28AT | 41 |
| Chest             | r\_shoulder\_y | MX-28AT | 51 |

**Reminder**: be careful with orientation while mounting [Dynamixel horns](dynamixel_hardware.md)

-   **[Double
    MX64](https://github.com/poppy-project/Robotis-library/blob/master/doc/en/double_MX64_assembly.md)**

-   **[Double
    MX28](https://github.com/poppy-project/Robotis-library/blob/master/doc/en/double_MX28_assembly.md)**
    Don’t screw the i101-Set\_to\_ MX28\_link (the plastic part with a
    free horn on it) too tightly, or don’t screw it at all since you
    will need to unscrew it during the trunk assembly.

-   **[Spine](https://github.com/poppy-project/Poppy-multiarticulated-torso/blob/master/doc/en/subassembly/spine_assembly_instructions.md)**

-   **[Chest](https://github.com/poppy-project/Poppy-multiarticulated-torso/blob/master/doc/en/subassembly/chest_assembly_instructions.md)**
    The video shows a HN07\_I101 in the prepared parts, but you don’t
    need it.

-   **[Trunk
    assembly](https://github.com/poppy-project/Poppy-multiarticulated-torso/blob/master/doc/en/5_DoFs_humanoid_spine.md)**
    You have to insert the nuts in the chest before mounting the double
    MX-28 part. You also have to put nuts in the abdomen before mounting
    the double MX-64 part.

    The abdomen part you have has a “Poppy” mark on the back, while the
    one on the video don’t. You also have holes to screw the
    SMPS2Dynamiel, instead of sticking it (use 2.5\*8mm screws).

    ![image](../img/screwed_SMPS.JPG)

### Assemble trunk and arms:

- Preparation: 5 min
- Assembly: 15-20 min

#### Requirements

![](../img/poppy_torso_assembly_BOM.jpg)

**Sub-assemblies:**
- Trunk
- Left arm
- Right arm

**3D printed parts:**
- Left shoulder
- right shoulder

**Cables:**
- 2x 3P 200mm

**Robotis parts:**
- 48x Bolts M2x3

**Motor configuration:**
- 1x Alimentation 12V
- 1x SMPS2Dynamixel
- 1x USB2Dynamixel or USB2AX
- A computer...


#### <a href="http://youtu.be/uDhLIS3vxM4" target="_blank">**VIDEO INSTRUCTIONS**</a>


[**<< Back to menu**](assemblyGuide.md)

[**Arms assembly >>**](arms_assembly.md)

[**Legs assembly >>**](legs_assembly.md)

[**Head assembly >>**](head_assembly.md)
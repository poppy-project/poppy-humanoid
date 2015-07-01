## Trunk

![image](img/parts_chest.JPG)\

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

    ![image](img/screwed_SMPS.JPG)

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

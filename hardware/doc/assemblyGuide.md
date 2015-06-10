---
author:
- 'Manon Cortial, Génération Robots'
title: Poppy Humanoid Robot Assembly Guide
---

![image](img/poppy-logo.png) ![image](img/GR-logo.png)

# Introduction

## The Poppy project

Poppy is an open hardware and open-source robotics project. It has been
designed to allow researchers and students to easily remove and replace
some parts of the body.

For example, different leg shapes have been tested on the Poppy Humanoid
robot to make the robot walk.

![image](img/humanoids2013_Experiments.png)

The Poppy humanoid robot is built using mainly MX-28 Dynamixel
servomotors, which are pretty powerful and may be harmful to your
fingers or materials.

So be very careful and put the robot in a free space while testing your
programs.

## About this documentation

This documentation contains some help and tips to build a Poppy Humanoid
robot. It does not replace the videos made by Inria, but complete and
sometimes corrects or updates them.

It contains a bit of context about Dynamixel servomotors and how to
assemble them (section \[dynamixel-hardware\]) and also how to set the
right parameters for them (section \[addressing-poppys-motors\]).

You will also find pictures of all the parts to help you name them
(section \[structural-parts\]), then assembly tips and links to the
assembly videos (section \[assembly-tips\]). As there is no video for
the head assembly, this doc contains a pretty complete guide for head
assembly (section \[head-assembly\]).

At the end, you will find a list of useful links (section
\[documentation-links\]) to help you find more information and help.

Please don’t hesitate to comment and correct this documentation on the
Poppy forum !


# Content

- [**Dynamixel Hardware >>**](dynamixel_hardware.md)
- [**Addressing Dynamixel >>**](addressing_dynamixel.md)
- [**Arms assembly >>**](arms_assembly.md)
- [**Trunk assembly >>**](trunk_assembly.md)
- [**Legs assembly >>**](legs_assembly.md)
- [**Head assembly >>**](head_assembly.md)


# Useful links {#documentation-links}

## Assembly instructions

[https://github.com/poppy-project/poppy-humanoid/blob/master/
hardware/doc/Poppy\_Humanoid\_assembly\_instructions.md](https://github.com/poppy-project/poppy-humanoid/blob/master/hardware/doc/Poppy_Humanoid_assembly_instructions.md)

Bill of Material:

<https://github.com/poppy-project/Poppy-lightweight-biped-legs/blob/master/doc/BOM.md>

## Forum and docs

Poppy project website: <https://www.poppy-project.org/>

Poppy project forum: <https://forum.poppy-project.org/>

herborist doc.: <http://poppy-project.github.io/pypot/herborist.html>

Dynamixel wizard doc.:

[http://support.robotis.com/en/software/roboplus/
dynamixel\_monitor/quickstart/dynamixel\_monitor\_connection.htm](http://support.robotis.com/en/software/roboplus/dynamixel_monitor/quickstart/dynamixel_monitor_connection.htm)

Bonjour software:

<https://support.apple.com/kb/DL999?locale=fr_FR&viewlocale=fr_FR>

STL files:

[https://github.com/poppy-project/poppy-humanoid/releases/download/
Official\_1.0\_Hardware\_release/STL\_3D\_printed\_parts.zip](https://github.com/poppy-project/poppy-humanoid/releases/download/Official_1.0_Hardware_release/STL_3D_printed_parts.zip)

## How to improve this guide?

You found an imprecision or an error in this guide? We need to correct
it!

If you master LaTeX and Github, get the tex file at
<https://github.com/HumaRobotics/poppy-examples/tree/master/doc> and do
a pull request.

Otherwise, go to the forum and point the problem in this topic:
<https://forum.poppy-project.org/t/quickstart-assembly-and-programming-plus-some-code-examples/1228>

Thanks in advance!

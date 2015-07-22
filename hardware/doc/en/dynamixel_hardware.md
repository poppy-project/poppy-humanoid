# Dynamixel hardware

The Poppy Humanoid robot is mainly built with [MX-28AT Dynamixel
servomotors](http://www.generationrobots.com/en/401858-servomotor-dynamixel-mx-28at.html)
(MX-28T are the previous version and can be used without any problem).
The other servomotors are MX-64T (bigger and stronger) and AX-12A
(smaller, used for the head).

Each Dynamixel servomotor embeds an electronic board allowing it to
receive different kind of orders (about goal, torque...) and communicate
with other Dynamixel servos. Therefore, you can chain up several
Dynamixel servomotors (each with a different ID) and command them all
from one end of the chain: each servomotor will pass the orders to the
next one.

![image](../img/daisy_link.JPG)

## Putting the Dynamixel horns to zero 

When you receive your Dynamixel servomotors, the horns are not mounted.
They are included in the packaging if the servo is packaged alone or
packaged separately for 6-pieces bulks (see next section to know what
horn goes to what servo).

When putting the controlled horn, be very careful to **put the dot on
the horn at the same point than the dot on the servo axis**. Once the
horn is put, it is most of the time **impossible to remove** ! This will
ensure that the zero position of the servo matches with the zero
position of the structure around.

![image](../img/zero.JPG) ![image](../img/zero2.JPG)

On the outside of the horn, you also have three dots indicating the
orientation. You should find the same three dots on structural parts, so
be sure to match them.

![image](../img/zero3.JPG)

## Horns of MX-28 and MX-64

On each Dynamixel servomotor apart from the AX-12A, you will have to
mount a horn to the motor axis. Most of the time, you will also have to
mount a free horn on the opposite side to provide better fixation points
for the structure parts.

To mount the main horn, put the plastic ring (white or black) and drive
the horn on the axis. **Be careful of the zero when putting the main
horn!** Then put thread locker on the big screw and screw it in the
middle.

![image](../img/MX28N.JPG)

Main horn mounted on a MX-28

For the free horn, first clip the ball bearing and the cap on the side
without shaft shoulder. Then put the horn on servomotor (with shaft
shoulder on servo side). Put thread locker on the big screw and screw
it. The horn should turn freely.

![image](../img/MX64I1.JPG) ![image](../img/MX64I2.JPG) ![image](../img/MX64I3.JPG)

Free horn mounted on a MX-64

Quick reminder of horn names and screw sizes:


| Servomotor | main horn | free horn | big horn screw | horn screws | case screws|
|------------| :-----------: | :-----------: | :----------------:| :-------------: | :-------------:|
|AX12-A |      none |       none      |    M3x10mm |           M2      |       M2
|  MX28   |   HN07-N101 |  HN07-I101   |   M2.5x8mm  |       M2x3mm    |    M2.5x6mm
|  MX64    |  HN05-N102  | HN05-I101  |     M3x8mm  |        M2.5x4mm   |    M2.5x6mm |


You need an allen wrench of size 1.5mm for M2 screws, 2mm for M2.5 screws
and 2.5mm for M3 screws. The longer M2 screws need a Phillips screwdriver.

## Putting the nuts

To attach structural parts on the body of the servomotors, you have to
first insert the nuts in their sites. This step may be quite painful if
you don’t have elfic fingers (there are less nuts to insert in the AT
servomotors than in the T version used for the videos).

Here’s my tip: take the nut using thin tweezers and bring it in the site
with the right orientation. Put the end of the tweezers in the hole to
ensure good alignment. Then use flat pincers to adjust the nut.

![image](../img/nuts1.JPG) ![image](../img/nuts2.JPG) ![image](../img/nuts3.JPG)

These nuts correspond to diameter 2.5mm screws, Allen wrench 2mm.

To build a full Poppy Humanoid robot, an electrical screwdriver is
strongly advised!

[**<< Back to menu**](assemblyGuide.md)
[**<< Addressing Dynamixel**](addressing_dynamixel.md)
# Adresser les servomoteurs Dynamixel 

Par défaut, tous les servomoteurs Dynamixel ont un ID égal à 1. Pour pouvoir utiliser plusieurs servomoteurs en série, chacun d'entre eux doit avoir un ID unique.

## Installation du driver pour l'USB2AX

USB2AX est le composant qui va connecter la tête de poppy Humanoid aux servomoteurs Dynamixel. Il peut également être utilisé pour contrôler les servomoteurs directement depuis votre ordinateur et c'est ce que nous allons faire pour adresser les moteur (leur assigner un ID).

Sous Linux, aucune installation n'est requise, mais vous devez ajouter votre utilisateur dans le groupe qui possède le port série. Selon la distribution c'est *dialout* ou *uucp*:

   sudo addgroup $USER dialout
   sudo addgroup $USER uucp

Autrement, le driver est accessible [ici](http://www.xevelabs.com/doku.php?id=product:usb2ax:quickstart).

N'oubliez pas d'alimenter vos moteurs (avec un SMPS2Dynamixel), sinon ils ne seront pas detectés !

## Installer le logiciel de scan

Vous pouvez utiliser l'un des deux logiciels suivants pour accéder aux registres des servomoteurs Dynamixel:

-   [Herborist](http://poppy-project.github.io/pypot/herborist.html): Outil créé par l'équipe du projet Poppy. 

-   [Dynamixel
    Wizard](http://support.robotis.com/en/software/roboplus/dynamixel_monitor/quickstart/dynamixel_monitor_connection.htm): Outil fourni par Robotis, fabriquant des Dynamixel (seulement pour Windows).

Herborist est intégré dans Pypot mais nécessite une librairie supplémentaire, PyQT4, pour l'interface graphique.

    sudo apt-get install python-qt4 python-numpy python-scipy python-pip
    sudo pip install pypot

Le logiciel est ensuite accessible directement depuis un terminal:

    herborist

![image](../img/herborist.png)

Connectez chaque moteur **un par un** à l'USB2AX et utilisez le bouton 'scan' dans Herborist ou Dynamixel Wizard pour le détecter. Si c'est un moteur neuf, il devrais avoir l'ID 1 et un baudrate à 57600bps, sauf les AX-12A qui ont déjà leur baudrate à 1000000. 

Mettez les paramètres suivants:

-   ID correspondant à la convention de nommage

-   Baudrate à 1 000 000 bps

-   Temps de réponse (Return delay time) à 0 ms à la place 0.5 ms

Dans Herborist, n'oubliez pas de cliquer sur le bouton 'Update EEPROM' pour que les changements soient pris en compte.

## Conventions de nommage

Si vous voulez que votre objet PoppyHumanoid corresponde à votre robot sans avoir à modifier le fichier de configuration, il faut vous conformer à la convention de nommage et d'adressage de Poppy Humanoid. Ainsi, dans vos programmes, quand vous utiliserez le nom d'un moteur, vous enverrez bien les ordres au moteur physique correspondant.

![image](../img/motor_naming_convention.jpg)


[**<< Retour au menu**](guideAssemblage.md)
[**<< Matériel Dynamixel**](materiel_dynamixel.md)



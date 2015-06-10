\documentclass[includefoot]{article}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{color}
\usepackage{wasysym}
\usepackage[utf8]{inputenc}
\usepackage{fancyhdr}

\pagestyle{fancy}
\fancyhf{}
\rfoot{\thepage}
\lfoot{\href{www.generationrobots.com}{www.generationrobots.com}}


\begin{document}

\title{Poppy Humanoid Robot Assembly Guide}
\author{Manon Cortial, Génération Robots}

\maketitle

  \includegraphics[height=0.22\textwidth]{img/poppy-logo} \hfill \includegraphics[height=0.22\textwidth]{img/GR-logo}

  \tableofcontents


\section{Introduction}

\subsection{The Poppy project}

Poppy is an open hardware and open-source robotics project. It has been designed to allow researchers and students to easily remove and replace some parts of the body. 

For example, different leg shapes have been tested on the Poppy Humanoid robot to make the robot walk.

 \begin{center}
  \includegraphics[width=0.6\textwidth]{img/humanoids2013_Experiments}
 \end{center}


\subsection{\textcolor{red}{Safety warning}}

The Poppy humanoid robot is built using mainly MX-28 Dynamixel servomotors, which are pretty powerful and may be harmful to your fingers or materials.

So be very careful and put the robot in a free space while testing your programs.

\subsection{About this documentation}

This documentation contains some help and tips to build a Poppy Humanoid robot. It does not replace the videos made by Inria, but complete and sometimes corrects or updates them.

It contains a bit of context about Dynamixel servomotors and how to assemble them (section \ref{dynamixel-hardware}) and also how to set the right parameters for them (section \ref{addressing-poppys-motors}).

You will also find pictures of all the parts to help you name them (section \ref{structural-parts}), then assembly tips and links to the assembly videos (section \ref{assembly-tips}). As there is no video for the head assembly, this doc contains a pretty complete guide for head assembly (section \ref{head-assembly}).

At the end, you will find a list of useful links (section \ref{documentation-links}) to help you find more information and help.

Please don't hesitate to comment and correct this documentation on the Poppy forum !

\section{Dynamixel hardware}
\label{dynamixel-hardware}

The Poppy Humanoid robot is mainly built with \href{http://www.generationrobots.com/en/401858-servomotor-dynamixel-mx-28at.html}{MX-28AT Dynamixel servomotors} (MX-28T are the previous version and can be used without any problem). The other servomotors are MX-64T (bigger and stronger) and AX-12A (smaller, used for the head).

Each Dynamixel servomotor embeds an electronic board allowing it to receive different kind of orders (about goal, torque...) and communicate with other Dynamixel servos. Therefore, you can chain up several Dynamixel servomotors (each with a different ID) and command them all from one end of the chain: each servomotor will pass the orders to the next one. 

 \begin{center}
  \includegraphics[width=0.6\textwidth]{img/daisy_link}
 \end{center}
 

\subsection{Putting the Dynamixel horns to zero}
\label{dynamixel-zero}

\textcolor{red}{\textbf{This step is critical to avoid damaging your Dynamixel servomotors !}}

When you receive your Dynamixel servomotors, the horns are not mounted. They are included in the packaging if the servo is packaged alone or packaged separately for 6-pieces bulks (see next section to know what horn goes to what servo).

When putting the controlled horn, be very careful to \textbf{put the dot on the horn at the same point than the dot on the servo axis}. Once the horn is put, it is most of the time \textbf{impossible to remove} ! This will ensure that the zero position of the servo matches with the zero position of the structure around.

 \begin{center}
  \includegraphics[height=0.5\textwidth]{img/zero}
  \includegraphics[height=0.5\textwidth]{img/zero2}
 \end{center}

On the outside of the horn, you also have three dots indicating the orientation. You should find the same three dots on structural parts, so be sure to match them.

 \begin{center}
  \includegraphics[width=0.6\textwidth]{img/zero3}
 \end{center}
\subsection{Horns of MX-28 and MX-64}

On each Dynamixel servomotor apart from the AX-12A, you will have to mount a horn to the motor axis. Most of the time, you will also have to mount a free horn on the opposite side to provide better fixation points for the structure parts.

To mount the main horn, put the plastic ring (white or black) and drive the horn on the axis. \textbf{Be careful of the zero when putting the main horn!} Then put thread locker on the big screw and screw it in the middle.


 \begin{center}
  \includegraphics[width=0.5\textwidth]{img/MX28N}

Main horn mounted on a MX-28
 \end{center} 
 
 For the free horn, first clip the ball bearing and the cap on the side without shaft shoulder. Then put the horn on servomotor (with shaft shoulder on servo side). Put thread locker on the big screw and screw it. The horn should turn freely.

 
  \begin{center}
  \includegraphics[height=0.3\textwidth]{img/MX64I1}
  \includegraphics[height=0.3\textwidth]{img/MX64I2}
  \includegraphics[height=0.3\textwidth]{img/MX64I3}

Free horn mounted on a MX-64
 \end{center}
 
Quick reminder of horn names and screw sizes:

\hspace{-6mm}\begin{tabular}{|c|c|c|c|c|c|}
\hline 
Servomotor & main horn & free horn & big horn screw & horn screws & case screws \\ 
\hline 
AX12-A & none & none & \diameter 3x10mm & \diameter 2 & \diameter 2\\ 
\hline 
MX28 & HN07-N101 & HN07-I101 & \diameter 2.5x8mm & \diameter 2x3mm & \diameter 2.5x6mm  \\ 
\hline 
MX64 & HN05-N102 & HN05-I101 & \diameter 3x8mm & \diameter 2.5x4mm & \diameter 2.5x6mm  \\ 
\hline 
\end{tabular} 

You need an allen wrench of size 1.5mm for \diameter 2 screws, 2mm for \diameter 2.5 screws and 2.5mm for \diameter 3 screws. The longer \diameter 2 screws need a Phillips screwdriver.

\subsection{Putting the nuts}

To attach structural parts on the body of the servomotors, you have to first insert the nuts in their sites. This step may be quite painful if you don't have elfic fingers (there are less nuts to insert in the AT servomotors than in the T version used for the videos).

Here's my tip: take the nut using thin tweezers and bring it in the site with the right orientation. Put the end of the tweezers in the hole to ensure good alignment. Then use flat pincers to adjust the nut.

 \begin{center}
  \includegraphics[width=0.55\textwidth]{img/nuts1}
  \includegraphics[width=0.55\textwidth]{img/nuts2}
  \includegraphics[width=0.55\textwidth]{img/nuts3}
 \end{center}
 
 These nuts correspond to diameter 2.5mm screws, Allen wrench 2mm.
 
 To build a full Poppy Humanoid robot, an electrical screwdriver is strongly advised!




\section{Addressing Dynamixel motors}
\label{addressing-poppys-motors}

By default, every Dynamixel servomotor has its ID set to 1. To use several servomotors in a serial way, each of them must have a unique ID.

\subsection{Installing the driver for USB2AX}

USB2AX is the device that will connect the Poppy Humanoid robot's head to the Dynamixel servomotors. It can also be used to control the servomotors directly from your computer and that's what we will do to address the motors.

On Linux, no installation is needed, but you must add yourself in the dialout group to have access to the USB port:
 \begin{verbatim}
sudo addgroup "username" dialout
\end{verbatim}

Otherwise, the driver is available \href{http://www.xevelabs.com/doku.php?id=product:usb2ax:quickstart}{here}.

Don't forget to power up your motors (using a SMPS2Dynamixel) otherwise they won't be detected !

\subsection{Installing the scanning software}

Use one of the two following software to access the Dynamixel servomotors registers:

\begin{itemize}
\item \href{http://poppy-project.github.io/pypot/herborist.html}{Herborist}: tool created by the Poppy Project team. 
\item \href{http://support.robotis.com/en/software/roboplus/dynamixel_monitor/quickstart/dynamixel\_monitor\_connection.htm}{Dynamixel Wizard}: windows-only tool provided by Robotis.
\end{itemize}

Herborist comes with the Pypot library, but needs the additional library PyQt4 for graphical interface.
\begin{verbatim}
sudo pip install pypot
sudo apt-get install python-qt4
\end{verbatim}

It should then be directly accessible for a terminal:
\begin{verbatim}
sudo herborist
\end{verbatim}
 \begin{center}
  \includegraphics[width=0.8\textwidth]{img/herborist}
 \end{center}
 
 Connect each motor \textbf{one by one} to the USB2AX and use the 'scan' button in Herborist or Dynamixel Wizard to detect it. If it's a new motor, it should have ID 1 and baudrate 57600bps, apart from AX-12A servos who already have a 1000000 baudrate.

You have to set:
\begin{itemize}
\item ID corresponding to the naming convention
\item Baudrate to 1 000 000 bps
\item Return delay time to 0 ms instead of 0.5 ms
\end{itemize}

In Herborist, don't forget to click on the 'Update EEPROM' button so the changes are taken in account.


\subsection{Naming conventions}

If you want your PoppyHumanoid object to correspond to your robot without having to modify the configuration file, you should stick to the Poppy Humanoid robot naming and addressing convention. This will ensure that, in your code, when you use a motor's name, you will really send orders to the corresponding physical motor.
\begin{center}
  \includegraphics[width=0.8\textwidth]{img/motor_naming_convention}
 \end{center}
 
 
 \section{Structural parts}
 \label{structural-parts}

 \begin{center}
  \includegraphics[width=0.9\textwidth]{img/parts_head}\\
  \vspace{1mm}
  \includegraphics[width=0.9\textwidth]{img/parts_electronics}\\
  \vspace{1mm}
  \includegraphics[width=0.9\textwidth]{img/parts_chest}\\
  \vspace{1mm}
  \includegraphics[width=0.9\textwidth]{img/parts_arms}\\
  \vspace{1mm}
  \includegraphics[width=0.9\textwidth]{img/parts_legs}
 \end{center}


\section{Assembly tips}
 \label{assembly-tips}




\subsection{Arms} 
 
\begin{itemize}
\item \textbf{\href{https://github.com/poppy-project/Poppy-basic-arms/blob/master/doc/subassemblies/right\_forearm\_assembly\_instructions.md}{Right}/\href{https://github.com/poppy-project/Poppy-basic-arms/blob/master/doc/subassemblies/left\_forearm\_assembly\_instructions.md}{Left} forearm} The hand design slightly changed from the videos, but the nuts and screws remain the same.
\begin{center}
  \includegraphics[width=0.8\textwidth]{img/hand_nut}
\end{center}
\item \textbf{\href{https://github.com/poppy-project/Poppy-basic-arms/blob/master/doc/subassemblies/right\_upper\_arm\_assembly.md}{Right}/\href{https://github.com/poppy-project/Poppy-basic-arms/blob/master/doc/subassemblies/left\_upper\_arm\_assembly.md}{Left} upper arm} Plug a 200mm cable in the unused plug before screwing the arm\_z motors (ids 43 and 53), because it will be really hard to plug once the motor is inside the structure part.
\item \textbf{\href{https://github.com/poppy-project/Poppy-basic-arms/blob/master/doc/subassemblies/right\_upper\_arm\_shoulder\_assembly.md}{Right}/\href{https://github.com/poppy-project/Poppy-basic-arms/blob/master/doc/subassemblies/left\_upper\_arm\_shoulder\_assembly.md}{Left} upper arm/shoulder}
\item \textbf{\href{https://github.com/poppy-project/Poppy-basic-arms/blob/master/doc/right\_arm\_assembly\_instructions.md}{Right}/\href{https://github.com/poppy-project/Poppy-basic-arms/blob/master/doc/left\_arm\_assembly\_instructions.md}{Left} arm assembly}
\item \textbf{\href{https://github.com/poppy-project/poppy-humanoid/blob/master/hardware/doc/Poppy\_Humanoid\_assembly\_instructions.md}{Trunk and arms assembly}} To distinguish between left and right shoulder parts, look at the three dots: the single dot should be down when the shoulder is in "zero" position (along the shoulder\_y motor).
\end{itemize}


Motors lists:

\begin{center}

\begin{tabular}{|c|c|c|c|}
\hline 
Sub-assembly name & Motor name & Type & ID \\ 
\hline 

Left upper arm/shoulder & l\_shoulder\_x & MX-28AT & 42 \\ 
\hline 
Left upper arm & l\_arm\_z & MX-28AT & 43 \\
\hline 
Left upper arm & l\_elbow\_y & MX-28AT & 44 \\
\hline 

\end{tabular} 
\end{center}

\begin{center}
\begin{tabular}{|c|c|c|c|}
\hline 
Sub-assembly name & Motor name & Type & ID \\ 
\hline 

Right upper arm/shoulder & r\_shoulder\_x & MX-28AT & 52 \\ 
\hline 
Right upper arm & r\_arm\_z & MX-28AT & 53 \\
\hline 
Right upper arm & r\_elbow\_y & MX-28AT & 54 \\
\hline 

\end{tabular} 
\end{center}


\subsection{Trunk} 
 
 \begin{itemize}
\item \textbf{\href{https://github.com/poppy-project/Robotis-library/blob/master/doc/en/double\_MX64\_assembly.md}{Double MX64}}
\item \textbf{\href{https://github.com/poppy-project/Robotis-library/blob/master/doc/en/double\_MX28\_assembly.md}{Double MX28}} Don't screw the i101-Set\_to\_ MX28\_link (the plastic part with a free horn on it) too tightly, or don't screw it at all since you will need to unscrew it during the trunk assembly.
\item \textbf{\href{https://github.com/poppy-project/Poppy-multiarticulated-torso/blob/master/doc/en/subassembly/spine\_assembly\_instructions.md}{Spine}}
\item \textbf{\href{https://github.com/poppy-project/Poppy-multiarticulated-torso/blob/master/doc/en/subassembly/chest\_assembly\_instructions.md}{Chest}} The video shows a HN07\_I101 in the prepared parts, but you don't need it.
\item \textbf{\href{https://github.com/poppy-project/Poppy-multiarticulated-torso/blob/master/doc/en/5\_DoFs\_humanoid\_spine.md}{Trunk assembly}} You have to insert the nuts in the chest before mounting the double MX-28 part. You also have to put nuts in the abdomen before mounting the double MX-64 part.

The abdomen part you have has a "Poppy" mark on the back, while the one on the video don't. You also have holes to screw the SMPS2Dynamiel, instead of sticking it (use 2.5*8mm screws).
\begin{center}
  \includegraphics[width=0.8\textwidth]{img/screwed_SMPS}
\end{center}
\end{itemize}


Motors list:

\begin{center}

\begin{tabular}{|c|c|c|c|}
\hline 
Sub-assembly name & Motor name & Type & ID \\ 
\hline 

Double MX64 & abs\_y & MX-64AT & 31 \\ 
\hline 
Double MX64 & abs\_x & MX-64AT & 32 \\
\hline 
Spine & abs\_z & MX-28AT & 33 \\
\hline 
Double MX28 & bust\_y & MX-28AT & 34 \\
\hline 
Double MX28 & bust\_x & MX-28AT & 35 \\
\hline 
Chest & head\_z & AX-12A & 36 \\ 
\hline 
Chest & l\_shoulder\_y & MX-28AT & 41 \\
\hline 
Chest & r\_shoulder\_y & MX-28AT & 51 \\
\hline 
\end{tabular} 
\end{center}

\subsection{Legs} 
 

There is only a video for left leg assembly. While assembling the right leg, be sure to put your motors symmetrical compared to the left leg. Also don't forget to change the motors IDs from 12-15 to 22-25.

\begin{itemize}
\item \textbf{\href{https://github.com/poppy-project/Poppy-lightweight-biped-legs/blob/master/doc/subassemblies/left\_hip\_assembly\_instructions.md}{Hip}}
\item \textbf{\href{https://github.com/poppy-project/Poppy-lightweight-biped-legs/blob/master/doc/subassemblies/left\_thigh\_assembly\_instructions.md}{Tight}}
\item \textbf{\href{https://github.com/poppy-project/Poppy-lightweight-biped-legs/blob/master/doc/subassemblies/left\_shin\_assembly\_instructions.md}{Shin}} If you received your Poppy kit from Generation Robots, you can use the custom 220mm cables instead of really short 200mm cables.
\item \textbf{\href{https://github.com/poppy-project/Poppy-lightweight-biped-legs/blob/master/doc/subassemblies/right\_leg\_assembly\_instructions.md}{Right}/\href{https://github.com/poppy-project/Poppy-lightweight-biped-legs/blob/master/doc/subassemblies/left\_leg\_assembly\_instructions.md}{Left} leg assembly}
\item \textbf{\href{https://github.com/poppy-project/Poppy-lightweight-biped-legs/blob/master/doc/subassemblies/pelvis\_assembly\_instructions.md}{Pelvis}} The videos shows \diameter 2x5mm screws. Use the \diameter 2x6mm screws that you can find in the Bolt-nut set BNS-10.
\item \textbf{\href{https://github.com/poppy-project/poppy-humanoid/blob/master/hardware/doc/Poppy\_Humanoid\_assembly\_instructions.md}{Torso and legs assembly}}
\end{itemize}


Motors lists:

\begin{center}

\begin{tabular}{|c|c|c|c|}
\hline 
Sub-assembly name & Motor name & Type & ID \\ 
\hline 
Pelvis & l\_hip\_x & MX-28AT & 11 \\ 
\hline 
Left hip & l\_hip\_z & MX-28AT & 12 \\ 
\hline 
Left hip & l\_hip\_y & MX-64AT & 13 \\ 
\hline 
Left thigh & l\_knee\_y & MX-28AT & 14 \\ 
\hline 
Left shin & l\_ankle\_y & MX-28AT & 15\\
\hline 
\end{tabular} 
\end{center}

\begin{center}

\begin{tabular}{|c|c|c|c|}
\hline 
Sub-assembly name & Motor name & Type & ID \\ 
\hline 
Pelvis & r\_hip\_x & MX-28AT & 21 \\ 
\hline 
Right hip & r\_hip\_z & MX-28AT & 22 \\ 
\hline 
Right hip & r\_hip\_y & MX-64AT & 23 \\ 
\hline 
Right thigh & r\_knee\_y & MX-28AT & 24 \\ 
\hline 
Right shin & r\_ankle\_y & MX-28AT & 25\\
\hline 
\end{tabular} 
\end{center}


\subsection{Head} 
 \label{head-assembly}


\begin{center}

\begin{tabular}{|c|c|c|c|}
\hline 
Sub-assembly name & Motor name & Type & ID \\ 
\hline 

Head & head\_y & AX-12A & 37 \\ 
\hline 
\end{tabular} 
\end{center}

\subsubsection{Setup of the Odroid board}


The Odroid is normally shipped with a eMMC module with Ubuntu 1.14 already flashed (it should have a red sticker on it). Simply plug it on the Odroid board and power it. After boot time, it should have the red light steady and the blue light flashing.

If you don't have a pre-flashed eMMC module, follow these instructions: \url{https://github.com/poppy-project/poppy_install}

%http://www.hardkernel.com/main/products/prdt_info.php?g_code=G138749987644
\vspace{3mm} Connect the Odroid board to your network using an ethernet cable. You have to access a wired network for initial setup (I tried link-local without success).

Windows users may wish to install the \href{https://support.apple.com/kb/DL999?locale=fr_FR&viewlocale=fr_FR}{Bonjour} software (the link is for the printer version, which does very well what we want it to do). Bonjour is installed by default on Linux and Mac. It is used to communicate with another device using its name instead of its IP.

You should get an answer if you type:

\begin{verbatim}
ping odroid.local
\end{verbatim}

Windows users now probably wish to install \href{http://www.putty.org/}{Putty} or any SSH client. Linux and Mac users have one installed by default. Then:

\begin{verbatim}
ssh odroid@odroid.local
\end{verbatim}

Password is odroid. Congratulations, you are now inside the Odroid!

Make sure the Odroid board has access to the internet and enter:

\begin{verbatim}
curl -L https://raw.githubusercontent.com/poppy-project/
poppy_install/master/poppy_setup.sh | sudo bash
\end{verbatim}

%Is it really usful to download matplot lib by default ??

Enter the odroid password. This command will download and run a script which will download and prepare installation. The board asks for a reboot:

\begin{verbatim}
sudo reboot
\end{verbatim}

You loose the SSH connection. The board has changed hostname and password, so wait for the blue light to flash regularly and connect with:

\begin{verbatim}
ssh poppy@poppy.local
\end{verbatim}

As you guessed, password is poppy. Installation process takes place automatically (and takes a while). When you see 'System install complete', do a Ctrl+C to finish. After a new reboot, your Odroid board is ready.

%sudo chmod -R a+rwx ~/src
%git clone https://github.com/HumaRobotics/poppy-examples.git



\subsubsection{Neck assembly}

The last servomotor is head\_y, a AX-12A. Set its ID to 37 and response time to 0 (baudrate is already at 1000000).


 \begin{center}
  \includegraphics[width=0.6\textwidth]{img/neck1}
 \end{center}
 
 Screw the neck to head\_z servo (\diameter 2x8mm screws). There are marks on the neck and on the servo to help you determine the orientation.
 
 
 \begin{center}
  \includegraphics[width=0.6\textwidth]{img/neck2}
 \end{center}
 
 Put \diameter 2 nuts in the servo case and attach it in the head\_back part.
 
  \begin{center}
  \includegraphics[width=0.6\textwidth]{img/neck3}
 \end{center}

  \begin{center}
  \includegraphics[width=0.6\textwidth]{img/neck4}\\
 \end{center}

Assemble the servo on the neck (\diameter 2 screws on the controlled side, the big screw on the other side). You again have marks on the neck and on the servo for orientation.

Connect head\_y to the dispatcher by passing the cable through the hole in the head.

Plug a 500mm cable from the pelvis SMPS2Dynamixel board to the back of the head. Attach a USB2AX at the end of this cable in the head.

Use a 140mm cable to connect the head\_y motor to another USB2AX.

\subsubsection{Camera and screen}

Attach the camera support to head\_front using \diameter 2.5x4mm screws. Put tape on the screws to avoid electrical interferences with the camera board.

\begin{center}
  \includegraphics[width=0.6\textwidth]{img/head_camera2}
 \end{center}

Attach the camera to its support using 3 \diameter 2x6mm screws.

\begin{center}
  \includegraphics[width=0.6\textwidth]{img/head_camera3}
 \end{center}

Put the screen and screen cover in the head. Attach the manga screen (or the fake one) with 2 \diameter 2.5x6mm screws.

\begin{center}
  \includegraphics[width=0.45\textwidth]{img/head_screen_cover}
  \includegraphics[width=0.45\textwidth]{img/head_screen}
 \end{center}

\subsubsection{Electronics}

If you don't have pre-soldered components, see: \url{https://github.com/poppy-project/Poppy-minimal-head-design/blob/master/doc/poppy_soldering.md}
%\url{https://github.com/poppy-project/Poppy-minimal-head-design/blob/master/doc/poppy_wiring.md}



Pass the Dynamixel connector of the Ubec through the hole in the head and connect it to the torso SMPS2Dynamixel.

\begin{center}
  \includegraphics[width=0.9\textwidth]{img/power_wiring}
 \end{center}


Attach both the other side of Ubec and the Odroid power cable to the audio amplifier. Be sure no to allow any short-circuit.

\begin{center}
  \includegraphics[width=0.9\textwidth]{img/head_ampli_power}
 \end{center}
 
 
Plug the audio jack. Wires order from left to right (when power terminal is farthest right): red-black-uncolored-white

\begin{center}
  \includegraphics[width=0.6\textwidth]{img/audio_amp_connection_zoom}
 \end{center}

\newpage

Put \diameter 2 nuts around the flowers openings then attach the speakers using \diameter 2 x3mm screws.

\begin{center}
  \includegraphics[width=0.6\textwidth]{img/head_speaker}
 \end{center}

Connect the speakers to audio ampli, left speaker black wire on Lout, Right ampli black wire on Rout.

%\begin{center}
 % \includegraphics[width=0.6\textwidth]{img/head_wiring1}
 %\end{center}
 \begin{center}
  \includegraphics[width=0.9\textwidth]{img/head_wiring2}
 \end{center}

Plug audio jack in Odroid, then use 2 \diameter 2.5x8mm screws to attach the Odroid board. Make sure the Ethernet connector is correctly placed in front of the corresponding hole.

  \begin{center}
  \includegraphics[width=0.6\textwidth]{img/head_odroid}
 \end{center}

Plug the power jack. On the hub, plug the camera and the two USB2AXs. Plug the wifi dongle and the Razor board if you have them. Push the hub above the Odroid.

  \begin{center}
  \includegraphics[width=0.6\textwidth]{img/head_final}
 \end{center}

Then close the head using 3 \diameter 2x8mm screws. %You may have to first blow some remaining powder out of the holes.
 

 
\section{Useful links}
\label{documentation-links}

\subsection{Assembly instructions}

\begin{flushright}
\href{https://github.com/poppy-project/poppy-humanoid/blob/master/hardware/doc/Poppy_Humanoid_assembly_instructions.md}{https://github.com/poppy-project/poppy-humanoid/blob/master/ hardware/doc/Poppy\_Humanoid\_assembly\_instructions.md}
\end{flushright}

Bill of Material:

\begin{flushright}
\href{https://github.com/poppy-project/Poppy-lightweight-biped-legs/blob/master/doc/BOM.md}{https://github.com/poppy-project/Poppy-lightweight-biped-legs/blob/master/doc/BOM.md}
\end{flushright}

\subsection{Forum and docs}

Poppy project website: \hfill \url{https://www.poppy-project.org/} 

Poppy project forum: \hfill \url{https://forum.poppy-project.org/} 

herborist doc.: \hfill
\href{http://poppy-project.github.io/pypot/herborist.html}{http://poppy-project.github.io/pypot/herborist.html}

Dynamixel wizard doc.:

\begin{flushright}
\href{http://support.robotis.com/en/software/roboplus/dynamixel_monitor/quickstart/dynamixel_monitor_connection.htm}{http://support.robotis.com/en/software/roboplus/ dynamixel\_monitor/quickstart/dynamixel\_monitor\_connection.htm}
\end{flushright}

Bonjour software:

\begin{flushright}
\href{https://support.apple.com/kb/DL999?locale=fr_FR&viewlocale=fr_FR}{https://support.apple.com/kb/DL999?locale=fr\_FR\&viewlocale=fr\_FR}
\end{flushright}

STL files:

\begin{flushright}
\href{https://github.com/poppy-project/poppy-humanoid/releases/download/Official_1.0_Hardware_release/STL_3D_printed_parts.zip}{https://github.com/poppy-project/poppy-humanoid/releases/download/ Official\_1.0\_Hardware\_release/STL\_3D\_printed\_parts.zip}
\end{flushright}

\subsection{How to improve this guide?}

You found an imprecision or an error in this guide? We need to correct it!

If you master LaTeX and Github, get the tex file at \href{https://github.com/HumaRobotics/poppy-examples/tree/master/doc}{https://github.com/HumaRobotics/poppy-examples/tree/master/doc} and do a pull request.

Otherwise, go to the forum and point the problem in this topic: \href{https://forum.poppy-project.org/t/quickstart-assembly-and-programming-plus-some-code-examples/1228}{https://forum.poppy-project.org/t/quickstart-assembly-and-programming-plus-some-code-examples/1228}

Thanks in advance!

\end{document}
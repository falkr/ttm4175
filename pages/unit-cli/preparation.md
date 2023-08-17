# The Linux Command Line Interface (CLI)

## Learning Goals

:goals: Goals for this week's lab

- Get to know the Linux Command Line Interface (CLI)
    - Understand its importance
    - Learn basic commands for 
        - Navigation
        - Remote access
        - Networking-related tasks
    - Understand basic virtualization principles


# General Overview

The preparations for this unit consist of three parts

1. **Practical**: 
    - Setting up the necessary programs to connect to the Virtual Machines (VM) that we'll use in this and upcoming labs, and 
    - Trying out the commands from readings and videos on your own machine
2. **Reading** up on background information about the command line and some basic functions
3. **Watching** a few videos showcasing the use of those basic commands


:tip:
You can complete these parts in any order you prefer, but we suggest setting up your own environment first and experimenting with the commands on your own machine as they come up in the videos and readings.



# 1) Practical 

## Setting up a Local CLI Environment on Your Own Machine

- If you're using **MacOS** or a **Linux** distribution, you can summon a CLI environment by launching the *Terminal* app or your distribution's equivalent thereof.
- For **Windows** users, we suggest setting up the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/install-manual) which will allow you to run a Linux command line on your Windows machine.
    - Follow steps 1-6 from the linked article and install a Linux distribution of your choice, for instance Ubuntu 20.04.
    - When launching the Ubuntu app for the first time, you'll be prompted to create a (local) user account. After picking a name and password of your choice, you'll be in a Linux CLI environment.
    - Future references to *opening a terminal* mean opening the Ubuntu app in your case.
    - Note: the home directory of your new user will be empty initially, but you can navigate to your regular Windows user folder by typing `cd /mnt/c/Users/yourusername`.



## Connecting to the Remote Lab Virtual Machine (VM)

To reduce the load on your personal machines and give all groups a consistent experience, you will connect to virtual machines that run in NTNU's [Skyhigh OpenStack cluster](https://www.ntnu.no/wiki/display/skyhigh). You can get a quick summary about what VMs are in the following video. The figure below shows a brief overview of components and connections.

---
type: youtube
video: yIVXjl4SwVo
---


---
type: figure
source: img/openstack-vms.png
---


We can connect to remote (virtual) machines either via <abbr title="Secure Shell">SSH</abbr> if we only want to use the command line, or with tools such as <abbr title="Virtual Network Computing">VNC</abbr> to also launch graphical applications.


:tip: You need to be in the NTNU network to connect to the VMs. This is automatically the case if you are on campus and using the *eduroam* WiFi. Otherwise, you can use the NTNU <abbr title="Virtual Private Network">VPN</abbr> [service](https://i.ntnu.no/wiki/-/wiki/Norsk/Installere+VPN) to connect to the NTNU network first.


### Verifying that an SSH Client is Installed

MacOS and nearly all desktop Linux distributions come with an SSH client preinstalled and hence require no further installation. If you followed the installation of WSL above, the Ubuntu environment will also provide you with an SSH client. You can verify the availability of an SSH client by opening a terminal and typing `ssh -V`. Below, you can find the expected output for different platforms. 

```bash
# WSL / Linux
stas@DESKTOP [~]
-> % ssh -V
OpenSSH_8.2p1 Ubuntu-4ubuntu0.9, OpenSSL 1.1.1f  31 Mar 2020

# On a Mac
stas@stas-mbp [~] 
-> % ssh -V
OpenSSH_9.0p1, LibreSSL 3.3.6
```


### Connecting via SSH

On the day of the lab, you will receive the following credentials that will allow you to connect to your team's VM: user name, password, and IP address of the VM.

If you want to connect using SSH, you can open a terminal and type in `ssh <user>@<ip>`, replacing `<user>` and `<ip>` with the corresponding data from your credentials. You will then be prompted to provide the password and proceed to a command line environment on the remote VM where you can execute commands. Afterwards, you can quit the session by writing `exit` or hitting `Ctrl+D` on your keyboard. The output of a short example session is provided below. Notice how the beginning of the command prompt changes to `netlab@netlab-linux:~$` after connecting, indicating that you are logged in as the user `netlab` on a host called `netlab-linux`.


```bash
stas@DESKTOP [~]
-> % ssh netlab@10.212.170.85
netlab@10.212.170.86's password:
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.4.0-156-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 [...]
netlab@netlab-linux:~$ ls
Desktop  Documents  Downloads  GNS3  Music  Pictures  Public  Templates  Videos
netlab@netlab-linux:~$ exit
logout
Connection to 10.212.170.85 closed.
stas@DESKTOP [~]
-> %
```


### Connecting via VNC

While the CLI environment will be sufficient to complete the first lab, we will start using some graphical programs from week 35 and will therefore connect to the remote VM's desktop using a VNC application. We will outline the use of [TigerVNC](https://tigervnc.org/) since it has implementations for all major platforms, but any VNC client should work. You can find the installer [here](https://sourceforge.net/projects/tigervnc/files/stable/1.13.1/) (`tigervnc64-1.13.1.exe` for Windows, `TigerVNC-1.13.1.dmg` for MacOS, `sudo apt install tigervnc-viewer` on Debian-based Linux distributions).


:tip:
You will receive the credentials for connecting to the VM later. For now, you can continue with reading / watching the material in Sections [2](#2-introduction-to-the-cli-and-documentation-of-important-command) and [3](#3-videos-on-basic-commands-for-interacting-with-files-navigation).


Once installed, you can launch the TigerVNC Viewer and connect to the remote VM by providing its IP address and password (once inside the VNC client and once within the VM). Finally, you should see the remote desktop as outlined in the screenshots below.


---
type: figure
source: img/tiger-vnc-001.png
---


---
type: figure
source: img/tiger-vnc-002.png
---


---
type: figure
source: img/tiger-vnc-003.png
---


---
type: figure
source: img/tiger-vnc-004.png
---


:tip:
If you experience performance issues using VNC, you can try connecting to your lab VM using the x2go software. A guide for doing so can be found [here](https://www.ntnu.no/wiki/download/attachments/272859791/ttm4200-openstack-guide.pdf?version=1&modificationDate=1669571371048&api=v2). The only difference is that in your case the user name will be `netlab` instead of `ttm4200`.


# 2) Introduction to the CLI and Documentation of Important Commands

- [A tutorial introduction to the Unix command line](https://www.learnenough.com/command-line-tutorial)
    - The **introduction of Chapter 1 along with Sections 1.1, 1.2, and 1.4** (boxes and exercises are optional at this point) provides a broad overview into the topic.
- [Commands for getting help](commands-help.html): how to use the `man` and `apropos` commands to get help and information directly on the command line.


# 3) Videos on Basic Commands for Interacting with Files (Navigation, Manipulation, Search)

An introductory series on basic commands you'll use in the command line environment.


- File system navigation and inspection (`cd`, `ls`, ..)
---
type: youtube
video: j6vKLJxAKfw
---


- File system manipulation (`cp`, `rm`, ..)
---
type: youtube
video: eoejHvAPDFs
---


- Search and match inside files using `grep`. **Note**: the first five minutes are sufficient at this stage.
---
type: youtube
video: VGgTmxXp7xQ
---


- Printing file contents using `cat`
---
type: youtube
video: EKWGioJTMkM
---


- Getting help with `man`
---
type: youtube
video: blFOgzwJbfE
---





# Additional Resources

- [Unix/Linux Command Reference](https://files.fosswire.com/2007/08/fwunixref.pdf): handy overview of many commonly used commands and options.
- [explainshell.com](https://explainshell.com/): online tool that parses a given command and provides details on the command itself as well as the provided options / flags / arguments.



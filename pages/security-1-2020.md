# Installing VirtualBox and Kali Linux

This first lab is intended to get you familiar with VirtualBox, where you will be adding our main hacking environment, namely Kali Linux, and a victim machine which is Windows 7. 

We assume that you have created a folder */courses/ttm4175/* on your machine, and that you have already downloaded the Windows 7 and Kali Linux OVA files (as instructed in the preparation for this lab).

## Naming conventions

+ Host machine: The physical machine that runs on the actual hardware of the machine, and on which the VirtualBox program is installed. In your case, the host machine would be whatever operating system you have installed on your PC/laptop. We will generally not be using the host machine for anything other than launching VirtualBox.

+ Virtual machine (VM): the machine(s) that run within the VirtualBox program. They do not run directly on the physical hardware of your machine, but rather on the simulated machine that VirtualBox provides for them.

:goals: 

In this lab you will learn to:

- Add and update Kali Linux VM
- Add Windows VM
- Use some commands for user management in Linux


# VirtualBox configuration

+ Open VirtualBox. Under File -> Preferences, Change the “Default Machine Folder” to */courses/ttm4175/*, which ensures that your virtual machines will be created in the */courses/ttm4175/* folder.


# Adding a Kali Linux VM to VirtualBox

+ Go to File -> Import Appliance. Click on the folder icon and browse to the Kali Linux OVA file, then click on Next.

+ In the "settings" screen, leave all settings at the default value. You can choose another name for the VM if you want, by clicking on the name and replacing it with the name of your choice (for example "Kali Linux"). 

+ Click on Import, and then on Agree on the system license agreement. 

+ When the installation is complete, go through the settings. If you see the expression "Invalid settings detected" at the bottom of the screen, hover the mouse over it to see what settings need to be adjusted.

+ Under Settings -> System -> Motherboard, allocate between 4000-5000 MB of memory (RAM). If the value is not within the green range that you see on the screen, then change to another valid value.

+ Start the machine, and login with username = kali, password = kali

## Configuring the keyboard settings for Kali Linux
+ Click on the Terminal Emulator

+ To change the keyboard settings to Norwegian, run the following command: `sudo dpkg-reconfigure keyboard-configuration`

+ Re-enter the password for kali

+ The "keyboard type" on the first screen will likely be correct ("Generic.."). Keep the selected value and press Enter. 

+ When prompted for the keyboard layout, scroll down (using the arrow key) to "Other", then select "Norwegian", then "Norwegian" again.

+ When asked about "Key to function as AltGr", "compose key" and "control+Alt+Backspace", keep the selected values and press Enter.

+ Exit the terminal and restart Kali Linux.

## Create a root user

You will now create a **root** superuser that you will use instead of the standard user account **kali**. Here are the instructions to do so:

+ Issue command `sudo su`

+ Enter the password for **kali** user account

+ Issue command `passwd root`

+ Enter a password of your choosing for the **root** account and retype that password.

+ At this point you can log out and log in again with the **root** account

## Update Kali Linux

+ In the terminal window, run the following commands:
```bash
apt-get clean && apt-get update -y

apt-get upgrade -y && apt-get dist-upgrade -y
```

+ When prompted about restarting services during package upgrades, select Yes. 

# Adding a Windows 7 VM to VirtualBox

Next, we will create a new VM containing Windows 7. This machine will be the “victim” computer throughout the most of this lab. 

+ Import the file Windows 7.ova into VirtualBox: from the main VirtualBox window click on “Import Appliance..”; select the Windows 7.ova file; then click “Import”. You can just leave all the settings as they are.

+ Boot it up and log in with user **Lab1** to try it out (this account has no password).

# Manage users in Linux

## Get a List of All Users using the /etc/passwd File

Local user information is stored in the /etc/passwd file. Each line in this file represents login information for one user. 

+ Start Kali Linux and log in with **root** username

+ Open the passwd file using cat: `cat /etc/passwd`. You will get all the users that are defined in Kali Linux.

Each line in the file has seven fields delimited by colons that contain the following information:
Username, Encrypted password *(x means that the password is stored in the /etc/shadow file)*, User ID number, User’s group ID number, Full name of the user (GECOS), User home directory and Login shell (defaults to /bin/bash).


## Display the username only 

Using either *awk* or *cut* commands, your task is to print only the first field containing the username.

:hint:

`awk -F: '{ print $1}' /etc/passwd`

`cut -d: -f1 /etc/passwd`

## Check whether a user exists in the Linux system

+ We can use the command *getent* to get a list of all Linux users: `getent passwd`

+ To check whether a user exists in Linux, you can simply filter the users’ list that we obtained by piping the list to the *grep* command `getent passwd | grep <username>`. 

If the user exists, the command above will print the user’s login information. If there is no output, it means that the user doesn’t exist. 

+ Check if the users **kali**, **mysql**, and **lab** exist.

## Create a user and add it to a group

+ Create a group **ttm4175** using the command `groupadd <groupname>`

+ Create a user **user1** using the command `useradd <username>`

+ Create a password for **user1** using the command `passwd <username>`

+ Add **user1** to the group **ttm4175** using the command `adduser <username> <groupname>`

+ Remove the account **user1** using the command `deluser <username>`

+ Remove the group **ttm4175** using the command `delgroup <groupname>`  





 
 

# Bypassing authentication in Windows and Linux

The purpose of this lab is to learn about techniques for bypassing authentication. This will be performed in both Windows and Linux. 

# Part1 - Bypassing the Windows log in

Scenario: you have come across a Windows 7 machine that is password protected and you do not know the password. Your task will be to bypass the authentication mechanisms of Windows in order to get access to the machine.

You will perform this task with the help of a technique called dual-booting. In a dual-booting system, two or more operating systems are installed side-by-side on the same physical hard disk, with each OS assigned to its own logical partition on the disk. We will use VirtualBox to simulate that we are running a dual-boot system with Windows 7 and Kali Linux installed on their own separate hard disks, but attached to the same machine. We need therefor to attach Windows 7 disk to the Kali Linux VM.

##  Attaching the Windows 7 disk to the Kali machine in VirtualBox

+ Start the Windows 7 machine in VirtualBox and verify that you cannot access the **Lab2** user account without having the password. Shut down the machine again.

+ Make sure that Windows 7 VM is turned off.

+ In VirtualBox, with the Kali Linux VM selected, click on “Settings” then “Storage”.

+ Click on the label “Controller SATA”, and then click on the icon next to it that reads “Add Hard Disk”.

+ Select *Windows7-disk1.vdi* file  (located in the folder */courses/ttm4175/Windows 7/*), and add it to the Kali machine.

> Note that the bootloader will still not have picked up that you have attached a new disk to the computer, so when you start up your (Kali Linux) machine it will not show Windows 7 in the boot selection screen. 
(Bootloader: a small program which is responsible for locating (and running) the actual operating system stored on the device.)
>
+ To fix this, once you are logged into your Kali Linux machine, open up a terminal and type 
` # update-grub`

+ Reboot Kali Linux and check that Windows 7 has been added to the bootloader screen.

## Mounting the Windows 7 partition within Kali

You are now ready to begin bypassing the Windows authentication from within Kali.

+ Make sure that Windows 7 is turned off and log in to Kali Linux.

+ start up a terminal and verify that the Windows 7 disk is successfully detected as a device from within Kali by using the utility program *fdisk*. *fdisk* lists information about all the disks and partitions attached to your machine.

` # fdisk -l `% ‘l’ is a lower-case ‘L’

+ To access the contents of the Windows disk you need to mount its file system inside Kali.
Hard drives are normally mounted under "/mnt". Make a folder called /windows under "/mnt" and mount the Windows 7 partition in it with the mount command.

:hint:

* Create folder to mount the Windows file system: `mkdir -p /mnt/windows`

* This will incorporate the Windows file system under the "/mnt/windows" folder in Kali:
`mount /dev/sdb2 /mnt/windows` <br/>
`ls /mnt/windows`


## Changing the user password

Our target here is to run Windows 7 normally. To accomplish this we will need to bypass the Windows log in screen. Since we do not know the users password we will simply have to change it!

By modifying some crucial system files in Windows from within Kali, we can give ourselves access to a command line prompt with administrator access the next time we boot up Windows 7.

+ Make sure that the Windows 7 virtual machine is turned off before continuing!

+ On your Kali Linux machine, with the Windows disk mounted, change into the “System32” directory of the Windows file system from within Kali:
`# cd /mnt/windows/Windows/System32`

“System32” folder contains many of the most important system files for the Windows operating system. What we need in particular is the system file *cmd.exe* , and also the on-screen-keyboard program *osk.exe*. This latter can be run before you have logged in. Even more interesting is that, programs that were executed before having logged in are run with administrator privileges!

    cmd.exe : controls the terminal in Windows
    osk.exe : allows you to type characters into Windows without having a keyboard

So what would happen if we were to swap out the *osk.exe* binary with the *cmd.exe* binary? 

+ Start by moving the real *osk.exe* executable to a backup file:

   `# mv osk.exe osk.exe.backup` 	% rename the file osk.exe to osk.exe.backup

+ Copy *cmd.exe* to *osk.exe* so that enabling the on-screen-keyboard will actually give us a command prompt instead:

    `# cp cmd.exe osk.exe` 	% overwrite the osk.exe binary with the cmd.exe binary

+ Now restart your machine and select Windows 7 in the boot menu. 
+ Choose to log in as user **Lab2**. Verify that you cannot log in without the password. 

+ Now enable the on-screen-keyboard by clicking the little symbol in the bottom left corner. What
happens?
**The on-screen-keyboard tricked into giving us a command line prompt – with administrator access!**

+ In the command prompt type:

     `C:\Windows\system32> whoami`

> The whoami command shows you the username and user privileges that the currently logged in user has. Our goal is to get normal access to the system, i.e. not mounting it within Kali. The good news is that, with your current administrator rights, this is quite easy!
>
+ Your task is now to change the password of user **Lab2** to a password of your choosing, allowing you to log in as normal.

:tip: 

There is a command line utility for Windows called `net user` which could potentially be useful. 
To get more information on how to use this command type `net user ?` in the command line window or look it up online.


### Reverting Changes

Before you continue to the next section you should revert the change you did to *osk.exe*. That is, delete the current *osk.exe* file and rename the backup file *osk.exe.backup* to *osk.exe* again. Since **Lab2** does not have administrator rights it cannot rename the file, hence it has to be done from within Kali Linux. 

- Reboot the machine
- Select _Kali Linux_ in the bootloader menu
- Mount the Windows 7 disk as you did previously
- Revert the changes.

```bash
mount /dev/sdb2 /mnt/windows
rm /mnt/windows/Windows/System32/osk.exe
mv /mnt/windows/Windows/System32/osk.exe.backup /mnt/windows/Windows/System32/osk.exe
```
- Return to your home folder `# cd ` and unmount the Windows partition from kali Linux `# umount /mnt/windows`.

# Part2 - Bypassing Linux authentication

In this section you will learn how to bypass the authentication mechanisms in Linux. To this end, we will add the Lubuntu VM (that you downloaded last week) which is going to be the victim machine.

## Importing Lubuntu into VirtualBox

+ Start by importing the Lubuntu machine into VirtualBox by clicking “File -> Import Appliance...” in the main window of VirtualBox. Find the file *Lubuntu.ova* in the folder */courses/ttm4175/* and click “Import” --you can leave all settings at the default. 

## Running Kali Live

In part 1, we assumed that both Windows 7 and Kali Linux were installed on the same system so we could access the contents of the Windows 7 disk through Kali. However, what can we do if Kali Linux is not installed on the machine? The answer is **live booting**. 

:tip: 

Live booting means to run an operating system directly from a CD-ROM or USB-drive without being installed to disk. 


We will test the live booting feature by running Kali directly from CD-ROM and use it to bypass the login screen of the Lubuntu machine. 

+ Start by downloading [Kali Linux (Live)](https://cdimage.kali.org/kali-2020.3/kali-linux-2020.3-live-amd64.iso) and save it in the folder */courses/ttm4175/*.

+ With the Lubuntu machine highlighted (and turned off), click on Settings -> Storage. 

+ We simulate that we are inserting a CD-ROM (containing Kali Live) into the machine by clicking on «Adds Optical drive» icon (next to the Controller:IDE label). Locate and add the Kali Linux Live file *kali-linux-2020.2-live-amd64.iso* on your host machine, and then click on “choose”. You will see now that Kali Linux is listed under the Controller:IDE. 

+ Now start your Lubuntu machine. It will choose to boot from the (virtual) CD-ROM containing Kali Linux instead of the (virtual) hard disk containing the Lubuntu operating system. 

+ Select the “Live (amd64)” boot option and press Enter. If it ever asks for a username or password, then the defaults are “kali” and “kali”, respectively.

## Clearing the login password on Linux with Kali Live

Similarly to what we did in part 1, we need first to mount the Lubuntu partition within the Kali Linux file system, then make some changes to the files responsible for handling login data like usernames and passwords.

+ Inside Kali create a mount point for Lubuntu and mount it. 


`# sudo mkdir -p /mnt/lubuntu`               %Since you are logged in with "kali" user which is not a superuser, then you need to use "sudo"

`# sudo fdisk -l` 				             % Find out which device contains Lubuntu

`# sudo mount /dev/sda1 /mnt/lubuntu`         % sda1 in our example -- could be different for you!

With the Lubuntu partition mounted inside of Kali, you can modify all its files as if they were normal files in Kali. 

+ In Lubuntu, there is a user **ttm4175** that is password-protected. Your task now is to find out what to modify and in which file so that, the next time you boot it up, you will not be required to enter a password to log in with the user **ttm4175**.

<button class="w3collapsible">Hint</button>
<div class="w3content">
On most Linux systems user credentials are stored in two files: passwd and shadow, both located in the */etc* folder. The easiest way to wipe the password is by changing the /etc/passwd file.

Open the passwd file `# sudo nano /mnt/lubuntu/etc/passwd`, scroll down to the entry of the **ttm4175** user, and remove the *x* that comes in the second place which indicates that the password is stored hashed in the shadow file. Press ctrl+ o to save the changes, and then ctrl+x to exit. 
</div>


+ Remove the (virtual) CD-ROM containing Kali, and start Lubuntu. Verify that you have successfully cleared the user’s password by logging in as user **ttm4175** in Lubuntu.

+ After you have bypassed the login screen of Lubuntu, pick a new password using the *passwd* command line utility.
That is, open a command line window from inside Lubuntu (click the Lubuntu icon in the bottom-left corner and go “System Tools -> UXTerm”) and issue the following command:
    >>`~$ passwd ttm4175`
   
+ Then enter your new password. 



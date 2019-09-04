# Installing Raspbian on a virtual Machine

This step-by-step tutorial is intended to give a quick overview on how to "have" a Raspberry Pi in your personal computer.
It uses Oracle's [Virtual Box](https://www.virtualbox.org/) as a basis for virtualisation but many other solutions [exist](https://en.wikipedia.org/wiki/Comparison_of_platform_virtualization_software).

After following these steps you should have a basic setup very similar to what we use in the labs\., with connectivity only to your PC.
The idea is to use this virtual machine (VM) in headless mode and use `ssh` to test commands and configurations.
There are many options to configure your VM but they will not be covered here.

A final note, you may experiment with more than one VM and create networks to test different networking tools and configuration we will talk about.
You may also try other Linux distributions if you are considering changing your operating system or having a dual boot setup in your PC.


# Downloading the software

## Download VirtualBox

Simply navigate to [virtualbox.org](https://www.virtualbox.org/) on your browser and download it.
Afterwards install it as you would install any other software in your computer.

---
type: figure
source: figures/vbox/01-download_vbox.png
caption: "Download VirtualBox from the website."
---

## Download Raspbian image

You can download the necessary image from <https://www.raspberrypi.org/downloads/raspberry-pi-desktop/>.
Save it until the installation is complete and you can delete it afterwards (you can duplicate VMs even without this image file).
We will use this image in the [next section](#creating-your-virtual-machine).

---
type: figure
source: figures/vbox/02-download_image.png
caption: "Download Raspbian image from the website."
---


# Creating your virtual machine

## New VM

:steps:
1. Start by pressing the "New" button as seen in the figure below.
This will open a dialog where you will setup the initial configurations of your VM.

---
type: figure
source: figures/vbox/03.1-virtualbox.png
caption: "Create a new VM."
---

:steps:
2. Now you need to choose a name for your VM.
3. The field _Machine Folder:_ corresponds to the folder where your VM will be stored.
4. For the _Type_ and _Version_ of your VM you should select "Linux" and "Debian (64-bit)" even though other options are also possible.
It should look something like the image below.

---
type: figure
source: figures/vbox/04-nameit.png
caption: "First dialog for VM creation."
---

:steps:
5. After pressing _Continue_ you need to select how much RAM your VM is allowed to use.
$512\,MB$ is the minimum amount of recommended memory but using $1024\,MB$ may be better.

---
type: figure
source: figures/vbox/05-ram.png
caption: "Select amount of available RAM."
---


:steps:
6. Now, after pressing _Continue_ again, you need to create your virtual hard disk.
Just press _Create_.

---
type: figure
source: figures/vbox/06-vdisk.png
caption: "Create a virtual disk."
---

:steps:
7. Afterwards press _Continue_ to select a common disk format (VDI)

---
type: figure
source: figures/vbox/07-diskimage.png
caption: "Select Virtual Disk Image type."
---

:steps:
8. Press _Continue_ again for selecting a dynamically allocated disk file (fixed size is also okay).

---
type: figure
source: figures/vbox/08-dynamic.png
caption: "Select storage approach on the physical hard disk."
---

:steps:
9. Finally, select the folder where you would like to save your hard disk and how large this file should be, followed by _Create_.
**Note:** make sure you choose a virtual disk with enough space (at least $8\,GB$) and that the folder you selected is located in a physical disk with enough storage space.

---
type: figure
source: figures/vbox/09-disksize.png
caption: "Select the virtual disk's location and size. Create the VM."
---

At this stage you should see a new virtual machine in VirtualBox.

---
type: figure
source: figures/vbox/10-newvm.png
caption: "A new VM called myrasp can now be seen"
---

## Installation boot

Before we start our new VM we need to add the installation medium (the Raspbian image file you downloaded earlier) and perform the installation.
The following steps will guide you through this process.

:steps:
1. Start by selecting the new VM and then click on the settings button.

---
type: figure
source: figures/vbox/10.1-newvm.png
caption: "Edit the settings for the new VM."
---

:steps:
2. In the dialog that opens click on the storage tab.

---
type: figure
source: figures/vbox/11.1-settings.png
caption: "Click on the storage tab to select the installation medium."
---

:steps:
3. Now in the controller IDE tree select the "Empty" line and click on the CD image highlighted in the figure below.
This will allow you to select the downloaded Raspbian image (named something like _2019-04-11-rpd-x86-stretch.iso_).

---
type: figure
source: figures/vbox/12.1-storage.png
caption: "Click on CD button and select the downloaded Rasbpian image."
---

:steps:
4. Still inside the settings menu you may want to select the display pane and scale the screen (it is typically quite small so scaling to 150\% can be helpful).
Note however that the screen resolution can be configured directly in Linux (e.g. during boot) but this way is easier.

---
type: figure
source: figures/vbox/13-display.png
caption: "Option to scale the VM screen."
---

:steps:
5. After pressing _OK_ you should see the selected _iso_ file as an optical drive of your VM.
6. Press the start button to initiate the boot process.

---
type: figure
source: figures/vbox/14.1-vmwiso-note.png
caption: "The downloaded image should be included as an optical drive for the first boot."
---

:steps:
7. After starting the VM you will see a boot menu as shown below. Select the _Install_ option with the arrow keys and press ENTER.

---
type: figure
source: figures/vbox/15-install.png
caption: "In this boot menu there are several options, the simplest is to just select _Install_."
---

:steps:
8. At this point you can select your keyboard (press 'n') for quickly moving into the Norwegian keyboard. Note that you can proceed with the default keyboard as long as you remember some keys are in slightly different places.

---
type: figure
source: figures/vbox/16-keyboard.png
caption: "An English keyboard layout is great for keys such as [, ], {, }, /, #, ~ and others but you can also just use a Norwegian layout."
---

:steps:
9. At this stage the disk needs to be partitioned to create the file system. Note that it **corresponds to the virtual disk** it will not affect your computer. Select _Guided - use entire disk_ and press Enter.
10. Press Enter again to choose the only available (virtual) disk.
11. Even though several partitions can be used, to separate files/folders with different purposes, using only one partition is simpler.
12. Confirm the created partitions (1 partition for your files and 1 partition for _swaping_ when you run out of RAM).
13. Finally select _Yes_ and press Enter to confirm the partition setup.

---
type: figure
source: figures/vbox/17-partitions.png
caption: "Use the entire disk for simplicity but feel free to try other settings."
---

---
type: figure
source: figures/vbox/18-partitions2.png
caption: "There is only one disk to select."
---

---
type: figure
source: figures/vbox/19-partitions3.png
caption: "It is simpler to have only one partition for your files."
---

---
type: figure
source: figures/vbox/20-partitions4.png
caption: "Confirm that the configured partitions are correct (note: the mount point '/' corresponding to the root of the file system tree)."
---

---
type: figure
source: figures/vbox/21-partitions5.png
caption: "Final confirmation before writing the partitions on the disk."
---

:steps:
14. After some time installing the necessary components you will have to complete the installation by installing a boot loader (GRUB).
Select _Yes_ and press Enter.

---
type: figure
source: figures/vbox/22-installgrub.png
caption: "GRUB is one of the most commonly used boot loaders in Linux."
---

:steps:
15. Now select where the boot loader should be installed (in our case it should be _/dev/sda_).

---
type: figure
source: figures/vbox/23-grublocation.png
caption: "sda corresponds to the virtual disk's location and many more can be found in other machines. This is similar to drive letters (e.g. C:, D:) in Windows."
---

:steps:
16. This is the final step of the installation. Just press _Continue_ and you don't need to worry about removing the installation media (VirtualBox does that for us)

---
type: figure
source: figures/vbox/24-finish.png
caption: "The installation is complete and the VM will reboot into a freshly installed system."
---

# First boot
 
:steps:
1. After the reboot you will something like the image below. You may notice the name _Debian_ which a very famous distribution upon which the Raspbian distribution is based.

---
type: figure
source: figures/vbox/25-grub.png
---

:steps:
2. The first time you start your machine you will have the opportunity to go through a quick set up but may also skip it by pressing _Cancel_. However, if you want to change your keyboard press _Next_ and skip only the check for updates (it is faster in the command line).

---
type: figure
source: figures/vbox/26.1-firstboot.png
caption: "Follow the set up only if you want to change keyboard/location."
---

:steps:
3. Before anything else, open a terminal and change your password with `passwd`.
3. Now we should update our system. In a terminal type `sudo apt update` followed by `sudo apt upgrade`.

---
type: figure
source: figures/vbox/27-aptupdate.png
---

---
type: figure
source: figures/vbox/28-aptupgrade.png
---

:steps:
5. To finalise the process and prepare the VM for TTM4175 shut it down and enter the VM settings.

---
type: figure
source: figures/vbox/29-shutdown.png
---

:steps:
6. In the _Network_ pane change your network adapter to be connected to you PC only. This will create a local area network between your PC and your VM, which will be perfect for our experiments and labs. Notice that this will also prevent access to the Internet.

---
type: figure
source: figures/vbox/30.1-hostonly.png
caption: "With host-only we isolate the VM from the Internet but can still access it through `ssh`"
---

:steps:
7. Start again your VM, check its IP address and from now on you can start using it in headless mode and save computing resources. Using `ssh` to access your VM will the easiest way to test some commands and will allow a straightforward copy+paste between your PC and the VM.


# Additional Steps

## Headless Start

To start in headless mode you need only to press the start button arrow to select other options as seen below.

---
type: figure
source: figures/vbox/31.1-headless.png
caption: "This option is perfect when using the VM only through `ssh`."
---

## Save Disk Space

To save some disk space you may remove some of the many applications bundled with Raspbian and which we will not need.
A suggestion is:

```bash
sudo apt-get remove --purge libreoffice* scratch* sonic-pi sense-emu-tools bluej geany geany-common greenfoot
sudo apt-get clean
sudo apt-get autoremove
```




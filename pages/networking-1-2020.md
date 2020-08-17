# Binary and IP Addresses

The overall goal of this lab\. is to consolidate knowledge on IP addressing and subnets.
This will be achieved using available networking tools in Linux to manage a simple Raspberry Pi network.


:goals: After this lab you will be able to:

- Understand and apply basic binary arithmetic
- Understand IP addresses and their organisation into subnets
- Create and configure Local Area Networks (LANs)
- Use basic Linux commands for managing:
    - IP addresses (IPv4 and IPv6)
    - IP subnets and masks


# Pre-requisites for today

Before continuing please check these two steps:

:steps:
1. Make sure you have at least 20GB of disk space.
2. Confirm that you've downloaded the new VM image ([link](
https://filesender.uninett.no/?s=download&token=a0ca6d46-2078-4984-a532-b68e3fd2cbaf)).



# Teamwork 2

First, we will start with a reflection on teamwork.

[Teamwork 2](teamwork-2.html)


# Importing and configuring the Ubuntu VM

:steps:
1. Start by importing the newly downloaded VM just like you did for the RaspberryPI.
2. After the import is completed (it will take a few minutes), configure the settings of the new VM according to your computer specifications (for example, my laptop has only 8GB RAM so I configured my VM with 4GB).
You shouldn't use all the resources from your host machine in your VM as it can make things become less responsive.
3. Inside the VM settings go to `Network->Adapter 2` and configure it to be attached to an "Internal Network" as shown in the figure below.
4. Add a second adapter to the RaspberryPI VM, attach it to the same "Internal Network".

---
type: figure
source: figures/vbox2020/settings-internalnetwork.png
caption: "The internal network connecting the two VMs"
---

:tip:
You can think of an "internal network" as a cable directly connecting VMs. This means they don't connect to the Internet or have any other features such as DHCP or NAT.

Another tip, if you want to access the Ubuntu VM through `ssh` (recommended) remember to add _port forwarding_ on adapter one and choose a different _Host port_ such as 2223.



# Lab\. Exercises

Please **read each exercise** entirely before starting to solve it.

Remember you should deliver a report after the networking module is finished.
It should include the main commands and configurations necessary to complete each exercise.
Do not forget to take notes while solving the exercises so you do not have to repeat them.

These exercises should be completed in teams.


## Quick overview of IP addresses

By now you've already seen that IP addresses are an important part of the Internet and computer networks in general.
Before looking into more complicated setups, complete the following tasks and remember to include them in your report.

:steps:
1. Start by finding the IP address of <ntnu.no>. For this you can use the command `host`.
2. Convert the found IP address to binary (you can use external tools!).
3. How many bytes does this IP address contain?
4. How many bits are there between each point (full stop) in the address 192.168.0.13?

:tip:
Start your report now and keep updating it as you go! It doesn't have to look pretty but if you keep everything now (screenshots, notes, ...) you don't have to repeat it later. 



## Networking two computers (VMs)

---
type: figure
source: figures/net/TTM4175-ex1-2020.png
caption: "Diagram of the topology to be created"
---

The main goal of this exercise is to create a simple network between the two VMs through a simple network configuration as if they were connected by an Ethernet cable.

Remember you can edit configurations by directly using the VMs or, instead by simply using `ssh` from your host machine where you can have one or more terminals per VM.


### Configuring the network interfaces



**---> On your RPi VM**

Try the following steps:

:steps:
1. Using the command `ip addr show dev eth1` find out your current IP address, if any, on 'eth1'
2. Type `ip addr help` to see all the available options
3. Let's now remove any unwanted address or routes on 'eth1' with the command:
```bash
ip addr flush dev eth1
```

:steps:
4. Add an IP address and respective mask to the interface 'eth1' using the command:
```bash
ip addr add <your_chosen_ip_here>/<chosen_mask> dev eth1
```
**Note:** you should avoid the subnet 10.0.2.0/24 as it already being used on 'eth0'.

:steps:
5. Using the command `ip a s eth1` (same as in step 1 but shorter) to verify your IP address, it should be the one you have just set.
6. Use the command `ip link set up dev eth1` to "turn on" the interface, in case it is down.



**---> On your Ubuntu VM**

Repeat the configurations above, paying attention to the different interface notation and assigning a new IP address:

:steps:
1. Remove any address/route on the interface 'enp0s8' (e-n-p-zero-s-eight).
2. Add a different IP address and mask to the interface 'enp0s8' such that it is in the same subnet as 'eth1' on the RPi.
3. Use the command `ip l s up dev enp0s8` to set the interface to "UP".
4. How many addresses does the chosen subnet contain? 

:tip:
Remember that one IP address can only be used by a single interface in the same network! It should be unique.

The size of the subnet depends on the number of bits used on the corresponding mask.


Spoiler alert! Before clicking the box below try to solve the exercise on your own but of course you are free to check it out.

<button class="w3collapsible">Hint (IP addresses)</button>
<div class="w3content">
You can use any private IP address in the ranges:

* 10.0.0.0/8
* 172.16.0.0/12
* 192.168.0.0/16

An example of a pair of IP addresses and masks could be "10.100.2.1/30" and "10.100.2.2/30".

**Remember:** you need to have "root" privileges in order to change/add an IP address. 
</div> 



### Verifying your configurations

After configuring the two VMs continue with the following steps:

:steps:
1. On one of the VMs use the command `ip route` to see the added route. Which one is the new entry?
2. Verify that both nodes have connectivity with the `ping` command. First from the RPi and afterwards from the Ubuntu machine.
3. Make sure you can connect to the RPi from the Ubuntu machine using `ssh`.
4. From one of the VMs `ping` <ntnu.no>. What's the main difference in behaviour that you can see?


Spoiler ahead...

<button class="w3collapsible">Hint (ping)</button>
<div class="w3content">
Use the command `ping` like this to generate only 4 ICMP messages.
```bash
ping -c4 <ip_address>
```
And note the round-trip **time** of each message...
</div>




## Experimenting with masks

The goal of this task is to get more comfortable with subnets and masks and see how they work in practice.
If you have questions about why something happens, or does not happen, feel free to ask!

**---> On your RPi VM**

:steps:
1. Change the IP address of 'eth1' to 10.10.10.30 using the mask 255.255.255.192 (first add a new address then delete the previous one).
2. Verify if you still have connectivity and discuss why or why not.



<button class="w3collapsible">Hint (troubleshooting)</button>
<div class="w3content">
You may lose connectivity at this point depending on the IP addresses you have previously chosen.
</div>


**---> On your Ubuntu VM**

Now, on your Ubuntu VM make the following changes:

:steps:
1. Change the IP address of 'enp0s8' to 10.10.10.5 using the mask 255.255.255.192 (first add a new address then delete the previous one).
2. Check for changes in connectivity between the two VMs. Can one VM still `ping` the other?
3. Using the same IP address change the mask to '/30'.
4. Check for changes in connectivity between the two VMs.
5. Using the same IP address, what is the smallest subnet size, and corresponding mask, that you can use to maintain connectivity between the two VMs? Why?

:tip:
**About the report** You don't have to include all the commands you needed to type, **it is enough to discuss/explain** the changes in connectivity and the choices you made.



## Static IP addresses

In order to permanently save your IP configuration, so that they are persistent even after a reboot, you need to save it.
However, this is done differently in different Linux systems.
Below you'll see how to do it in Raspbian and Ubuntu.

**---> On your RPi VM**

To save your settings you need to edit the "dhcpcd.conf" file in `/etc/` (don't forget to check if you have permissions).
Edit this file and reboot to check the networking configurations have remained.

:aside:
You don't need to reboot your RPi to apply these setting, it's enough to restart the networking service but you need to type a bit more(e.g. `sudo ip link set eth1 down && sudo ip link set eth1 up` **or** `service networking restart`).



Example configuration (change accordingly!):

```bash
interface eth1
static ip_address=192.168.100.102/24
static routers=192.168.100.101
```

**---> On your Ubuntu VM**

To save your settings you need to edit the "01-network-manager-all.yaml" file in `/etc/netplan`.
After editing you can apply your changes with the command `sudo netplan apply`:

Example configuration (change accordingly!):

```bash
network:
    version: 2
    renderer: networkd
    ethernets:
        enp0s3:
            dhcp4: yes
        enp0s8:
            dhcp4: no
            addresses:
                - 10.0.20.2/24
```




# Optional Exercises

## Introducing IPv6

Change the topology you created in [the previous exercise](#lab.-exercises) to use IPv6 addresses and try:

* the `ping` command
* remote access with `ssh`
* different subnets

<button class="w3collapsible">Hint</button>
<div class="w3content">
Note that some commands require additional arguments to handle IPv6 (check their documentation).
</div>


## More SSH

The goal of this exercise is to show you how `ssh` handles sessions.

:steps:
1. Using the internal network interface, connect both VMs have connectivity with each other, using the `ping` command.
2. Connect to the RPi from the Ubuntu VM using `ssh` with the option "-o ServerAliveInterval=5" and the remaining needed parameters.
3. In the RPi `ssh` session run the "Alive" command:


* `python -c $'import time\nwhile True: print("Alive!"); time.sleep(5)'`

:steps
4. Now, your RPi VM directly (on another terminal window), set the 'eth1' interface down (`ip l s eth1 down`) and wait for an error message on your `ssh` connection (it should take less than 1 min.).
5. After the error message, set 'eth1' up again, re-establish the `ssh` session and verify if the command is still running using the `ps` command.
6. Find a way to repeat the "Alive" command in the RPi making sure it is not interrupted if the connection fails (**this will require some research or check the hint below**).

:tip:
If a command such as `ps` outputs too much information you can use the Unix pipeline principles to manage the output.
For example `ps aux | grep desired_pattern`.


If you couldn't figure out step 6. above you can see a hint below.

<button class="w3collapsible">Hint (ssh)</button>
<div class="w3content">
To keep programs running even if there's a connection interruption you can use the commands `screen`, `tmux` or simply run them on the background.
</div> 

# Final Steps

### Learning Goals

In your double-team, reflect about what you learned today. Write a few sentences that capture (in your own words) what you learned and why it can be useful. Share these few sentences with everyone in the double-team. (You should use this text in the individual reflection below.)

:aside: <img src="figures/doubleteam.png" width="30"/>


### Individual Reflection

Fill out the <a href="https://forms.office.com/Pages/ResponsePage.aspx?id=cgahCS-CZ0SluluzdZZ8BSxiepoCd7lKk70IThBWqdJUQzJJUEVaQlBBMlFaSFBaTllITkcxRDEzNi4u" class="arrow">individual reflection survey</a>.


### The Combination Lock

Each team gets their own combination lock so you can store the box in the lockers in the lab. 

* The locks come opened and with the opening combination set.
* Take a picture of that combination in your phone, so you remember it.
* Do not attempt to change the code. (You do so by turning the locks opening 180 degrees and then setting them --- don't do that by accident.) 


### Cleaning Up

:todo:
- Put all hardware back into the box.
- Store the box in one of the lockers in the lab, using the combination lock.
- Connect all parts of the PC back to it (keyboard, mouse, monitor).
- Take out any trash. (Even if its not yours... thank you!)
- Put the chairs back to the table.

### Individual Exercises

We recommend that you take some time to consider if there are any parts of this unit that you want to repeat individually, at your own pace. If you decide to do so, you have several options:

- You have access to the hardware box at all times from the lockers. Just make sure everyone in your team knows where the box is, and put it back into the locker.
- Install a Raspberry Pi Image on a Virtual Box in your PC. With this, you always have a Raspberry Pi with you.
- Some of the Linux-related exercises also work on the Linux-PCs in the lab.

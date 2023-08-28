# Networking I - Binary, IP Addresses, Subnets, LAN Configuration

The overall goal of this lab is to consolidate knowledge on IP addressing and subnets.
This will be achieved using available networking tools in Linux to manage a simple Raspberry Pi network.


:goals: After this lab you will be able to

- Understand and apply basic binary arithmetic
- Understand IP addresses and their organisation into subnets
- Create and configure Local Area Networks (LANs)
- Use basic Linux commands for managing:
    - IP addresses (IPv4 and IPv6)
    - IP subnets and masks



# Launching GNS3 and Creating a Basic Network


In today's lab, we're going to use the [GNS3 network emulator](https://www.gns3.com/) which is already pre-installed on your VMs. This tool allows us to easily and visually create networks whose components we can configure by accessing their respective command line interface. After connecting to your VM, launch the `GNS3` program from the desktop and create a new empty project.


---
type: figure
source: img/gns-001.png
---


You can add various devices like network switches and hosts, as well as links between them from the menus on the left. After adding the devices, you can control their state using the controls at the top as outlined in the figure.


---
type: figure
source: img/gns-002.png
---


Try to create a minimal topology that consists of two dierctly connected hosts by dragging instances of the `ubuntu-host` onto the main panel, and then interconnecting their `eth0` interfaces by consecutively clicking on the `Add a link` button and the two hosts. The result should look as follows.


---
type: figure
source: img/gns-003.png
---


By starting all devices using the green button at the top, the respective containers are launched. Once they are running, you can access their terminal by double-clicking the respective device in the topology.

:tip:
If you close the terminal of a container, the container itself will turn off and you will have to turn it back on by right-clicking the device and pressing start. **Beware: containers are stateless by design, so restarting the container will also lead to a complete loss of any files and configuration changes on it.**


# Lab Exercises

Please **read each exercise** entirely before starting to solve it.

:report:
Remember you should deliver a report after the networking module is finished.
It should include the main commands and configurations necessary to complete each exercise.
Do not forget to take notes while solving the exercises so you do not have to repeat them.



## Quick Overview of IP Addresses

By now you've already seen that IP addresses are an important part of the Internet and computer networks in general.
Before looking into more complicated setups, complete the following tasks and remember to include them in your report.


1. Start by finding the IP address of `ntnu.no`. You can use the `host` command for this.
2. Convert the IP address you found to binary (you can use external tools!).
3. How many bytes does this IP address contain?
4. How many bits are there between each point (full stop) in the address 192.168.0.14?


:report:
Start your report now and keep updating it as you go! It doesn't have to look pretty but if you keep everything now (screenshots, notes, ...) you don't have to repeat it later. 



## Networking with Two Computers


The main goal of this exercise is to get familiar with basic network configuration commands using the simple two-host network topology we created earlier.


### Configuring the Network Interfaces


##### On ubuntu-host-1

Try the following steps


1. Using the command `ip addr show dev eth0` find out your current IP address, if any, on `eth0`
2. Type `ip addr help` to see all the available options
3. Let's now remove any unwanted address or routes on `eth0` with the command `ip addr flush dev eth0`
4. Add an IP address and respective mask to the interface `eth0` using the command `ip addr add <your_chosen_ip_here>/<chosen_mask> dev eth0`
5. Using the command `ip a s eth0` (same as in step 1 but shorter) to verify your IP address. It should be the one you have just set.
6. Use the command `ip link set up dev eth0` to "turn on" the interface, in case it is down.



##### On ubuntu-host-2

Repeat the configurations above, paying attention to the different interface notation and assigning a new IP address.

1. Remove any address/route on the interface `eth0`.
2. Add a different IP address and mask to the interface `eth0` such that it is in the same subnet as `eth0` on the first host.
3. Use the command `ip l s up dev eth0` to set the interface to "UP".
4. How many addresses does the subnet you chose contain? 


:tip:
Remember that one IP address can only be used by a single interface in the same network! It should be unique.



The size of the subnet depends on the number of bits used on the corresponding mask.


Spoiler alert! Before clicking the box below, try to solve the exercise on your own, but of course you are free to check it out.

---
type: hint
title: "Hint (IP addresses)"
---
You can use "any" private IP address in the ranges:

* 10.0.0.0/8
* 172.16.0.0/12
* 192.168.0.0/16

**Note:** you can't use the first nor the last IP address of a network/subnet. So, for example, for the network 10.12.1.0/24 you cannot use the addresses 10.12.1.0 nor 10.12.1.255 (remember that /24 corresponds to an 8 bit mask or 255.255.255.0).

An example of a pair of IP addresses and masks could be "10.100.2.1/30" and "10.100.2.2/30".

**Remember:** you need to have "root" privileges in order to change/add an IP address. For the containers in the GNS3 environment, this is always the case as indicated by the command prompt starting with the `#` sign as opposed to the `$` sign you see for instance as the netlab user on the host VM. 


### Verifying Your Configuration

After configuring the two hosts, continue with the following steps.


1. On one of the hosts, use the command `ip route` to see the routing table. What is the entry you see?
2. Verify that both nodes have connectivity with the `ping` command. First from ubuntu-host-1 and afterwards from ubuntu-host-2.
3. You can also capture packets that traverse your network using the Wireshark tool we've seen during the lecture. To do so, right-click the link, hit "start capture", make sure that "Start the capture visualization program" is checked, and confirm with "OK".
4. Run `ping` again and observe what kind of packets / messages are exchanged. Do some research to figure out the broad use of the involved protocols (few sentences in your report are sufficient).



## Experimenting with Masks

The goal of this task is to get more comfortable with subnets and masks and see how they work in practice.
If you have questions about why something happens, or does not happen, feel free to ask!



##### On ubuntu-host-1


1. Change the IP address of `eth0` to `10.10.10.30` using the mask `255.255.255.192`.
2. Verify that you still have connectivity and discuss why or why not.



---
type: hint
title: "Hint (troubleshooting)"
---
You may lose connectivity at this point depending on the IP addresses you have previously chosen.



##### On ubuntu-host-2

Make the following changes.


1. Change the IP address of `eth0` to `10.10.10.5` using the mask `255.255.255.192`.
2. Check for changes in connectivity between the two hosts. Can one still `ping` the other?
3. Using the same IP address, change the mask to `/30`.
4. Check for changes in connectivity between the two hosts.
5. Using the same IP address, what is the smallest subnet size, and corresponding mask, that you can use to maintain connectivity between the two hosts? Why?

:report:
You don't have to include *all* the commands you needed to type, **it is enough to discuss/explain** the changes in connectivity and the choices you made.



## Static IP addresses

In order to permanently save your IP configuration, so that they are persistent even after a reboot, you need to save it.
However, this is done differently in different Linux systems.
Below you'll see how to do it in Raspbian and Ubuntu.

**---> On your RPi VM**

To save your settings you need to edit the "dhcpcd.conf" file in `/etc/` (don't forget to check if you have permissions).
Edit this file and reboot to check the networking configurations have remained.

:aside:
You don't need to reboot your RPi to apply these settings, it's enough to restart the networking service but you need to type a bit more (e.g. `sudo ip link set eth1 down && sudo ip link set eth1 up` **or** `service networking restart`).



Example configuration (change accordingly!):

```yaml
interface eth1
static ip_address=192.168.100.102/24
static routers=192.168.100.101
```

**---> On your Ubuntu VM**

To save your settings you need to edit the "01-network-manager-all.yaml" file in `/etc/netplan`.
After editing you can apply your changes with the command `sudo netplan apply`:

Example configuration (change accordingly!):

```yaml
network:
    version: 2
    renderer: networkd
    ethernets:
        enp0s3:
            dhcp4: yes
            nameservers:
                addresses: [8.8.4.4,8.8.8.8]
        enp0s8:
            dhcp4: no
            addresses:
                - 10.0.20.2/24
```

:tip: Be careful with the indentation! Use spaces to align or copy-paste exactly as shown (change the addresses as needed).



# Optional Exercises

## Introducing IPv6

Change the topology you created in [the previous exercise](#lab.-exercises) to use IPv6 addresses and try:

* the `ping` command
* remote access with `ssh`
* different subnets

---
type: hint
title: "Hint"
---
Note that some commands require additional arguments to handle IPv6 (check their documentation).


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

---
type: hint
title: "Hint (ssh)"
---
To keep programs running even if there's a connection interruption you can use the commands `screen`, `tmux` or simply run them on the background.



# Networking in Linux

The overall goal of this lab\. is to consolidate knowledge on IP addressing and subnets.
This will be achieved using available networking tools in Linux to manage a simple Raspberry Pi network.


:goals: After this lab you will be able to:

- Understand IP addresses and their organisation into subnets
- Create and configure Local Area Networks (LANs)
- Use basic Linux commands for managing:
    - IP addresses (IPv4 and IPv6)
    - routes and routing tables


# Lab\. Exercises

Please **read each exercise** entirely before starting to solve it.

Remember you should deliver a report by the end of the semester.
It should include the main commands and configurations necessary to complete each exercise.
Do not forget to take notes while solving the exercises so you do not have to repeat them.

These exercises should be completed in teams.


## Networking two Raspberry Pis

---
type: figure
source: figures/net/TTM4175-ex1.png
caption: "Diagram of the topology to be created"
---


The main goal of this exercise is to create a simple network between two Raspberry Pi (rPi) devices through a simple Ethernet cable.

Initially you will have to connect one rPi at a time to keyboard and screen for configuring the necessary IP addresses and their masks.
Afterwards you can use `ssh` if you need to change anything.

### Configuring the network interfaces

Repeat these steps with each rPi, adjusting their addresses adequately.

1. Connect the keyboard, mouse and screen
2. Using the command `ip addr show dev eth0` find out your current IP address, if any, on 'eth0'
3. Type `ip addr help` to see all the available options
4. Add an IP address and respective mask to the interface 'eth0' using the command:

```bash
ip addr add <your_chosen_ip_here>/<chosen_mask> dev eth0
```

5. Using the command `ip a s eth0` (same as in step 2 but shorter) verify your IP address, it should be the one you have just set.

<button class="w3collapsible">Hint (IP addresses)</button>
<div class="w3content">
You can use any private IP address in the ranges:

* 10.0.0.0/8
* 172.16.0.0/12
* 192.168.0.0/16

An example of a pair of IP addresses and masks could be "10.100.2.1/30" and "10.100.2.2/30".

You need to have "root" privileges in order to change/add an IP address. 
</div> 


### Verifying your configurations

After configuring the two rPi connect them to each other using a single Ethernet cable.
Only one rPi needs to be connected to the keyboard/screen.

1. Use the command `ip route` to see the added route
2. Verify that both nodes have connectivity with the `ping` command
3. Make sure you can connect to the rPi without keyboard/screen using `ssh`

<button class="w3collapsible">Hint (ping)</button>
<div class="w3content">
Use the command `ping` like this to generate only 4 ICMP messages.

```bash
ping -c4 <ip_address>
```
</div>

<button class="w3collapsible">Hint (ssh)</button>
<div class="w3content">
The `ssh` service may not be running, check with `sudo systemctl status ssh`.
If it is not running use the `systemctl` command with _start_ and with  _enable_ if you want `ssh` to start from boot.
</div>

## Experimenting with masks

The goal of this task is to get more comfortable with subnets and masks.
Start by configuring the rPi **not connected** to keyboard/screen:

1. Change the IP address to 10.10.10.30 using the mask 255.255.255.192 (first add a new address then delete the previous one)
2. Verify if you still have connectivity and discuss why or why not.

<button class="w3collapsible">Hint (troubleshooting)</button>
<div class="w3content">
You may lose connectivity at this point depending on the IP address you have previously set on the rPi connected to the keyboard/screen.
</div>


Now, using the rPi **connected** to the keyboard/screen try the following:

1. Change the IP address to 10.10.10.4 using the mask 255.255.255.192 (first add a new address then delete the previous one)
2. Check for changes in connectivity between the two rPi
3. Using the same IP address change the mask to /30
4. Check for changes in connectivity between the two rPi
5. Using the same IP address, what is the smallest subnet size, and corresponding mask, that you can use to maintain connectivity between the two rPi? Why?

## Experimenting with routes

Using the rPi **connected** to the keyboard/screen try the following:

1. Remove the existing route with `ip route del <ip/mask> dev eth0`
2. Check for changes in connectivity between the two rPi
3. Add a new route with the command `ip route add` with a "/30" mask


## Static IP addresses

In order to permanently save IP configuration, so that they are persistent even after a reboot, you can edit the "dhcpcd.conf" file in `/etc/`.
Edit this file and reboot to check the networking configurations have remained.

Example configuration:

```bash
interface eth0
static ip_address=192.168.100.102/24
static routers=192.168.100.101
```

# Additional Exercises

## Introducing IPv6

Change the topology you created in [the previous exercise](#lab--exercises) to use IPv6 addresses and try:

* the `ping` command
* remote access with `ssh`
* different subnets

<button class="w3collapsible">Hint</button>
<div class="w3content">
Remember to change the addresses in the remote rPi first or simply add the IPv6 address without modifying the IPv4 addresses you had earlier, instead of replacing.

In addition note that some commands require additional arguments to handle IPv6 (check their documentation).
</div>

## More SSH

After configuring both devices, from the rPi with keyboard and screen, do the following:

1. Verify that both nodes have connectivity with the `ping` command
2. Connect to the other rPi using `ssh` with the option "-o ServerAliveInterval=5" and whatever else may be necessary
3. In the remote rPi run the "Alive" command
    * `python -c $'import time\nwhile True: print("Alive!"); time.sleep(5)'`
4. Before the previous command ends, remove the Ethernet cable from one of the rPi and wait for an error message (it should take less than 1 min.).
5. After the error message, reconnect the cable, re-establish the `ssh` session and verify if the command is still running using the `ps` command.
6. Repeat the "Alive" command in the remote rPi making sure it is not interrupted if the connection fails, and execute steps 4 and 5 again.

If a command such as `ps` outputs too much information you can use the Unix pipeline principles to manage the output.
For example `ps aux | grep desired_pattern`.

<button class="w3collapsible">Hint (ssh)</button>
<div class="w3content">
To keep programs running even if there's a connection interruption you can use the commands `screen`, `tmux` or simply run them on the background.
</div> 




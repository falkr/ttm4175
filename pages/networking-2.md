# Networking in Linux -- DNS and DHCP

The overall goal of this lab\. is to complement knowledge on IP, subnets and routing with DNS and DHCP.
This will be achieved using available tools and software in Linux to manage a simple Raspberry Pi network.


:goals: After this lab you will be able to:

- Understand how DNS works
- Understand how DHCP works
- Use Linux commands and software for:
    - retrieving DNS information
    - installing/configuring a local DHCP server


# Lab\. Exercises

Please **read each exercise** entirely before starting to solve it.

Remember you should deliver a report by the end of the semester.
It should include the main commands and configurations necessary to complete each exercise.
Do not forget to take notes while solving the exercises so you do not have to repeat them.

These exercises should be completed in teams.


## Preparation

1. Select one Raspberry Pi as your _router_. 
From now on this rPi will be always referred to as _router_ and the other one as _client_.
You may change their hostnames to avoid confusions.

<button class="w3collapsible">Hint (hostname)</button>
<div class="w3content">
Among other possibilities, the hostname can be changed by editing the files _hostname_ and _hosts_ in `/etc/`.

Do not forget to reboot after the changes.
</div> 

2. Connect the keyboard/screen to the _client_ and remove any static IP address configurations (in case there are any from last week).

3. Connect the keyboard/screen to the _router_ and connect it to the Internet (you can just disconnect the _client_) and install _tcpdump_, _dnsutils_, _whois_, _isc-dhcp-server_, _hostapd_ and optionally _vim_.
Some of this software will be used next week. 

## Experimenting with DNS

DNS can be used for many different purposes.
Today we will focus on only a few, using basic commands to retrieve information about NTNU's domain.

### The `whois` command

The `whois` command can be used to search for an object in a WHOIS database.
We can use it for example for searching for Domain Name or IP block registrations.

Try the following commands and reflect on their results:

1. `whois <your_rpi_ip_address>`
2. `whois ntnu.no`


### The `host` command

The simplest way to find common DNS information is to use the command `host`.
Try the following commands and reflect on their result:

1. `host 8.8.8.8`
2. `host ntnu.no`
3. `host -t TXT ntnu.no`
4. `host -t ANY ntnu.no`


### The `dig` command

This tool provides more information, and options, than the `host` command.
**Note:** the command `nslookup` is also very popular (and older), used for the same purpose.

Using `dig` your focus should be on the "ANSWER" section (carefully notice the options on the second step).
Try the following commands and reflect on their result:

1. `dig ntnu.no`
2. `dig ntnu.no +noall +answer`
3. `dig ntnu.no MX +noall +answer`
4. `dig ntnu.no ANY +noall +answer`
5. `dig ntnu.no +short`
6. `dig -x 129.241.160.102`



## Configure a DHCP server

Disconnect the _router_ from the Internet (remove the Ethernet cable, do **not** connect it to the client) and follow these steps:

1. Activate DHCP on the interface *eth0* on the *isc-dhcp-server* configuration file.
2. Configure the DHCP server properties in the *dhcpd.conf* file without forgetting:
- to declare this DHCP server as authoritative (the official DHCP server for a LAN);
- to specify a subnet and range;
- to provide the required DNS information;
- to specify the *router* Pi as the default router;
- to assign a fixed IP address to the _client_
3. *stop* and *disable* the service *dhcpcd.service*;
4. Make sure the *eth0* interface is *UP* and configured with an IP address within the subnet specified in the DHCP server;
5. *start* (and optionally *enable*) the *isc-dhcp-server.service*.

<button class="w3collapsible">Hint (config)</button>
<div class="w3content">
Note the difference between *dhcpcd.conf* and *dhcpd.conf*.
These files have different names, locations and purposes.

To find the location of these files, and of the *isc-dhcp-server* file you can use `find`.

Many configuration files include several examples for several different purposes, use/adapt the ones that suit your needs. 

</div>

<button class="w3collapsible">Hint (static)</button>
<div class="w3content">
An hardware address or hardware Ethernet can be easily found with the command `ip link`.

For this exercise you will have to retrieve this information from your _client_.

</div>

<button class="w3collapsible">Hint (DNS)</button>
<div class="w3content">
To "normally" use the Internet, in addition to a router for forwarding IP traffic, a client needs a DNS server to resolve names such as "ntnu.no".

Use the DNS servers 129.241.0.200, 129.241.0.201 and 8.8.8.8.

</div>


## Using DHCP (and seeing it)

After configuring the _router_ we want it to be able to give a DHCP offer to the client.
If everything is correct this will be automatic but we will monitor the process with the following steps:

1. On a terminal in the _router_ run the following command (and leave it running):

```bash
tcpdump -i eth0 -vvv -s 1500 'port 67 or port 68'
```

2. Connect the _client_ and the _router_ using a single Ethernet cable.
  - Check the messages sent in each direction
  - What happens?
3. Verify the network configurations on the _client_ (IP address, mask, DNS, routes).
**Note:** you should use `ssh`.

<button class="w3collapsible">Hint (ssh)</button>
<div class="w3content">
Remember your _client_ should have received the IP address you configured as a static address.

You can use the command `dhcpcd --dumplease eth0`.

</div>

## More DHCP

:aside: <img src="figures/doubleteam.png" width="30"/>


To test DHCP further join your double team and experiment with each other's _client_.

1. What address do the _clients_ receive?
2. Is the static IP address configuration working? Why or why not?


# Additional Exercise

Try the setup above using only IPv6. How does DHCP work? What is different?

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

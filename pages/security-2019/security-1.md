# Linux Security -- basics

In previous classes, you have already learned about IP addresses, subnetting, DHCP, NAT, DNS, and Wi-Fi.
Now you will learn and understand about cybersecurity.
The main aim of this lab is to make you understand basic security concepts.
To demonstrate the ideas we will use the Raspberry Pi, the Linux operating system, and available networking tools.

:goals: After this lab you will be able to:

- Understand how to create and manage a user account
- Create a secure password
- Create and configure remote access
  - Connect through Telnet via dynamic port
  - Connect through SSH through a dynamic port
- Use sniffing tools to see traffic (elemental analysis)


# Lab\. Exercises

Please **read each exercise** entirely before starting to solve it.

Remember you should deliver a report after the security module is finished.
It should include the main commands and configurations necessary to complete each exercise.
Do not forget to take notes while solving the exercises so you do not have to repeat them.

These exercises should be completed in teams.


## Preparation

1. Make sure both the Raspberry Pis are up and connected.
2. Connect keyboard/screen to the Raspberry Pi.
3. Based on previous class knowledge, configure an IP address on each device.


## Creating and managing user accounts

1. To see all the available users' list type `users` and see if the username "api" exists
2. Type `groups` to see all the groups list, see if the group name "sudo" exists
3. To create a user account, type `sudo adduser <username>`

<button class="w3collapsible">Hint</button>
<div class="w3content">
Do not forget to add your preferred password and skip the extra input fields by pressing "Enter".
</div>

4. Check the group of the current user with `groups <username>`
5. Use `groups` command to change the group of the username you created into sudo group
6. Remove the user account you created by typing `sudo deluser <username>`


## Creating a strong password

1. Change your current password by using a command passwd

<button class="w3collapsible">Hint</button>
<div class="w3content">
Stronger passwords contain upper and lower case letters, digits, special characters, and a minimum length of 8.
</div>


## Remote Access

### Part 1

1. Modify the file "etc/hosts.allow" to enable telnet access
2. Narrow down only to allow single IP access

<button class="w3collapsible">Hint</button>
<div class="w3content">
If `telnet` is not installed use `apt install telnetd`
</div>

3. Use `tcpdump` to sniff a password

<button class="w3collapsible">Hint</button>
<div class="w3content">
```bash
tcpdump -i eth0 -A src <ipaddress> or dst <ipaddress>
```
</div>

4. Relate the concept of security based on `tcpdump` results


### Part 2

1. In the previous class you have learned how to configure `ssh` but now try to change the port 22 to 220
2. See if the `ssh` connection is still working
3. Apply the same sniff mechanisms and check if you can see your password
4. Compare the difference between telnet and ssh. Which one is more secure? Justify your answers.


# Homework

Create two different user accounts and allow remote access only for a single user per machine.
The permitted user only accesses the system through SSH in port number 220.


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

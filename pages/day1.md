# Project Goal

For this week we have set a goal: *We want you to be able to create your own web server, running on a computer that you control and configure, and that serves your own website.* 
Each day we get a bit closer to that goal. 

---
type: figure
source: figures/teknostart/goals.png
caption: "Each day we try to reach a new goal. The final goal is to run our own website."
---

Of course, you learn much more than just serving your own website. On our way you will learn many useful things that will help you through the rest of this course, the rest of your studies and also later during your job:

:goals:
- You will be able to operate your own computer.
- You will get familiar with the most important commands to control the computer and the applications running on it.
- You will be able to operate a computer remotely.
- You will get some basic understanding of networking.

But you will also learn some more skills that will be useful:

- You will learn to work in teams.
- You will get used to English as instruction language.


# Day 1: The Raspberry Pi

Today we will start things off by letting you become familiar with the Raspberry Pi.

### Learning Goals for Today

:goals:
- Become familiar with the Raspberry Pi
- Connecting the Pi
- Changing the default password
- Logging in remotely via SSH


### New Linux Commands

- [ls](commands.html#ls) --- to list files and folders.
- [passwd](commands.html#passwd) --- to change passwords.
- [pwd](commands.html#pwd) --- to show in which directory you are.


# Teamwork 

We organized you in teams of **3 students** in this semester. 
This is a good number to work together behind a computer. It's enough to learn something from each other and work together, but not too many so it get's to hard to coordinate your work. 

The teams are **fixed over the semester** so that you get used to each other and develop a better team dynamic over time. 

During the beginning of the lab, when we do quizzes, for example, we join always two teams of three into a **double-team** of six students. The pairing of the teams is also the same each week. Team 1 is a double team with team 2, and team 3 with team 4, and so on. 

:aside: <img src="figures/doubleteam.png" width="30"/><br/>Tasks done as double team will be marked with this symbol.


We start with a task on teamwork.

---
type: button
url: teamwork-1.html
text: "Go to teamwork task"
---



# Starting the Raspberry Pi

For our project we use the [Raspberry Pi](https://www.raspberrypi.org). It's a mini-computer, so when something goes wrong the consequences are not severe. But although it is a small and cheap computer, you operate it just like most other servers. **The Raspberry Pi runs the same commands (programs) and operating system like "real" servers.** So learning how to operate a Raspberry Pi is the best exercise for operating also bigger machines later.

The following video provides an introduction, and shows how to operate the Pi:

---
type: youtube
video: wjWZhV1v3Pk
caption: "How to get started with the Raspberry Pi."
--- 

## Task: Connecting the Pi

With the knowledge from above, connect the Pi!

- Make sure the SD-card is inserted correctly
- Connect the Pi to the monitor in the lab using the HDMI cable
- Connect the Pi via USB to mouse and keyboard
- Connect the Pi with the Power supply
- _Do *not* connect the Ethernet cable_

Now, plug in the power supply. You should see that the Raspberry Pi boots up.

:tip: **Tip:** The Pi does not come with an on/off button. To switch it off, you _can_ simply unplug it from the power source. However, if the Pi is busy writing your files to the storage, you may end up with some errors. Therefore, to make sure all is fine, use the command `shutdown`, wait until the Pi has finished, and unplug the power then safely. 


# Logging In and Changing Passwords


## Logging In

By default, the Raspberry Pi is configured with a default user with the name `pi` and the password `raspberry`. 

Type first the username:

```bash
pi
```

Then, type the password, followed by the key `enter`:

```bash
raspberry
```

## Command Line

The Raspberry Pi will probably boot directly into a graphical user interface with windows. This looks a lot like Windows or macOS, and you can use it in a similar way. 
For many tasks related to system administration and programming it is useful to use the *command line*. 
This is especially the case when the computer is somewhere in a server room or data center far away and you want to log into it remotely. (We will do that later.)
Therefore, we are going to learn how to use the command line.

You can access the command line by opening the terminal application from the menu:

---
type: figure
source: figures/teknostart/rpi-terminal-1.png
---

---
type: figure
source: figures/teknostart/rpi-terminal-2.png
---




## Changing the Password

Everybody knows the default login. This is why we do not yet connect the Raspberry Pi to the network: Anyone on the internet could connect to your Pi with this default username and password, and do all sorts of stuff,like deleting files, copying information, but also using your Pi to attack other computers! And they even can change the password so that you cannot do anything anymore! We are not joking here, this *really* happens. 

Therefore we need to change the password before we connect the Pi to the network. For this, we use the command `passwd`. Type the command in the command line:

```bash
passwd
```

Select a password and share it with your team members. 




# Connecting to the Internet

After you have changed the default password, you can connect the Pi to the internet. 
Use the provided ethernet cable and plug the Pi into the Ethernet plug in the lab. 




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


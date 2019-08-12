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
- You will get familiar with the most important commands.
- You will learn to work in teams.
- You will get used to English as instruction language.

For our project we use the [Raspberry Pi](https://www.raspberrypi.org). It's a mini-computer, so when something goes wrong the consequences are not severe. But although it is a small and cheap computer, you operate it just like most other servers, since it runs the same commands. So learning how to operate a Raspberry Pi is the best exercise for operating also bigger machines later.



# Day 1: The Raspberry Pi

Today we will start things off by letting you become familiar with the Raspberry Pi.
We will use a combination of the topics you go through the first three days to set up our own webserver and website, so pay attention!


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


# Starting the Raspberry Pi

- Make sure the SD-card is inserted correctly
- Connect the Pi to the monitor in the lab using the HDMI cable
- Connect the Pi via USB to mouse and keyboard
- Connect the Pi with the Power supply
- _Do *not* connect the Ethernet cable_

Now, plug in the power supply. You should see that the Raspberry Pi boots up.



# Logging In and Changing the Password


## Logging In

By default, the Raspberry Pi is configured with a default user with the name `pi` and the password `raspberry`. 

Type first the username:

```bash
pi
```

Then, type the password, followed by enter:

```bash
raspberry
```

## Command Line

The Raspberry Pi will probably boot directly into a graphical user interface with windows. This looks a lot like Windows or macOS, and you can use it in a similar way. 
For many tasks related to system administration and programming it is useful to use the *command line*. 
This is especially the case when the computer is somewhere in a server room or data center far away and you want to log into it remotely. (We will do that later.)
Therefore, we are going to learn how to use the command line.




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




# Individual Reflection


* Fill out the <a href="https://forms.office.com/Pages/ResponsePage.aspx?id=cgahCS-CZ0SluluzdZZ8BSxiepoCd7lKk70IThBWqdJUQzJJUEVaQlBBMlFaSFBaTllITkcxRDEzNi4u" class="arrow">individual reflection survey</a>.




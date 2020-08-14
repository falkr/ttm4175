# Routing and Docker 

The overall goal of this lab\. is to complement knowledge on IP, subnets with some routing notions.
This will be achieved using the same VMs as last week and default Linux tools.

Today we will also learn more about Docker. With Docker we will be able to simulate a "mini-cloud" inside our Ubuntu VM. This can be a bit overwhelming at first but we will look at it slowly.

:aside:
**Note:** Running Docker inside a VM may seem strange to some of you but it allows us to keep a clean and consistent environment for all of us. There's nothing wrong with it and, for the sake of curiosity, did you know that you can run Docker inside Docker?

<p><a href="figures/net/docker-ception.jpg"><img src="figures/net/docker-ception.jpg" width="100px"></a>



:goals: After this lab you will be able to:

- Check the role of routing in networking
- Use `ip route` for managing routes
- Recognise the importance of _ports_ in networking
- Learn basic Docker principles:
    - Images and containers
    - The _Dockerfile_
    - Basic commands for managing containers



# Lab\. Exercises

Please **read each exercise** entirely before starting to solve it.

Remember you should deliver a report after the networking module is finished.
It should include the main commands and configurations necessary to complete each exercise.
Do not forget to take notes while solving the exercises so you do not have to repeat them.

These exercises should be completed in teams.

**NOT UP TO DATE FROM HERE ON**

## Preparation

:steps:
1. make sure there's connectivity between both VMs
2. ...


## Experimenting with routes

In your RPi VM try the following:

:steps:
1. Remove the existing route with `ip route del <ip/mask> dev eth1`.
2. Check for changes in connectivity between the two VMs.
3. Add a new route with the command `ip route add` with a "/30" mask.








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

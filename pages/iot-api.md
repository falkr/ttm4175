# APIs

**Goal:** Let’s create a more advanced alarm system that detects some movement (with the PIR sensor), takes a picture (with the USB webcam) and notifies you via Slack.

---
type: figure
source: figures/iot/alarm-system.png
---

For this task, we work again in Python. Altogether, this is a complex task; you need to coordinate many functions and APIs. Each step itself should not be too hard, but you need to put eveything together in the end. Therefore, try to build the application step by step, and try each function in isolation before putting everything together. Below is a list of steps. You don't have to do them in the given order.

:tips: Read first through all steps, and try to make a sequence diagram of the final application. The diagram should show a lifeline for your application, a lifeline for the PIR sensor, the camera, the cloudinary API and the Slack API. 

**Task:** Think through if you are using an approach that is more of an orchestration or an choreography. Which approach works here?

**Task:** Once you have the sequence diagram, work on each of the steps.

# Python 3.6

Unfortunately, the Slack API client needs Python 3.6, but the Raspberry Pi has Python version 3.5 by default. 
[Follow this description to update Python to version 3.6](rpi-python3-6.html).


# Step: Taking a Picture

Find a way to capture an image with a USB camera in Python. It’s a standard USB camera, and there should be code out there that does the job.


# Step: Uploading an Image to Slack

We created a step-by-step description to [send messages and images to Slack](iot-slack.html).


# Step: Sensing Movement

We collected some descriptions how to use the [passive infrared sensor to detect movement](iot-pir-sensor.html).

 

# Finally: Putting all Together

Once you have control over all of the individual steps above, put everything together to build the complete alarm system.  

**For the Report:** Document how it works in a series of screenshots and photos, for instance like in a comic strip. Also, take a video that shows how your system works. The video can (and should) be short, ca 1 or 2 minutes. You don't have to do a lot of editing, just show how the system works. We have added a section in Blackboard to deliver the video.

**Well done!**

## Optionally: Add More Functionality

If you have time and energy left, try to find other APIs on the web and extend your application with some more useful functionality. 


# Final Steps

### Learning Goals

Reflect about what you learned today. Write a few sentences that capture (in your own words) what you learned and why it can be useful. Share these few sentences with everyone in the team. (You should use this text in the individual reflection below.)


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


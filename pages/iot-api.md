**Goal:** Let’s create a more advanced alarm system that detects some movement (with the PIR sensor), takes a picture (with the USB webcam) and notifies you via Slack.

For this task, we work again in Python.

Altogether, this is a difficult and complex task; you need to coordinate many functions and APIs. Therefore, try to build the application step by step, and try each function in isolation before putting everything together.

Below is a list of steps. You don't have to do them in the given order.

**Task:** Read first through all steps, and try to make a sequence diagram of the final application. The diagram should show a lifeline for your application, a lifeline for the PIR sensor, the camera, the cloudinary API and the Slack API. 

**Task:** Think through if you are using an approach that is more of an orchestration or an choreography. Which approach works here?

**Task:** Once you have the sequence diagram, work on each of the steps.

### Step: Slack Message with Image

The Slack API allows you to display an image alongside your message. However, Slack expects that you send the URL of an image, not the image itself. (This may have changed, and there may be a way to also upload the image directly to Slack. You can select how to do this.)

Before you try to upload your own image from the webcam, you should test how the Slack API works and provide it with an image that is accessible on the internet by a url. (You can for instance use http://lorempixel.com for that.)

* Check the [messaging API of Slack.](https://api.slack.com/rtm) This tells you about how to add an image to a message.
* Slack also has an [SDK for Python.](https://slackapi.github.io/python-slackclient/) 


### Step: Taking a Picture

Find a way to capture an image with a USB camera in Python. It’s a standard USB camera, and there should be code out there that does the job.

### Step: Uploading an Image to Slack

This should work with the [SDK for Python.](https://slackapi.github.io/python-slackclient/)


### Alternative Step: Uploading an Image to Cloudinary

This is only necessary if you din't manage to upload an image to Slack. 
Since Slack expects the URL to an image and not the image itself, we need to upload the camera picture somewhere and make it accessible via an URL.

One way to achieve it is to use a hosting service for images, like [Cloudinary](cloudinary.com). It offers an API to uplpoad images, and retrieve a URL for them. Have a look at their [SDK for Python on Github](https://github.com/cloudinary/pycloudinary). (Tip: It seems you can install it again via *pip install cloudinary*.)

* Create an account at Cloudinary.
* Install the Python SDK.
* Upload an image and test if it is accessible in the URL via a browser.


### Step: Sensing Movement

Use the PIR sensor to detect movement, as in the first week. 

### Finally: Putting all Together

Once you have control over all of the individual steps above, put everything together to build the complete alarm system.  

**For the Report:** Document how it works in a series of screenshots and photos, for instance like in a comic strip. Also, take a video that shows how your system works. The video can (and should) be short, ca 1 or 2 minutes. You don't have to do a lot of editing, just show how the system works. We have added a section in Blackboard to deliver the video.

**Well done!**

### Optionally: Add More Functionality

If you have time and energy left, try to find other APIs on the web and extend your application with some more useful functionality. 
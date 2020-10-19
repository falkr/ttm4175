
# Programming IoT Devices

Goals for this week's lab:

- Program an IoT device (at least a simulation of it)
- How to use a simple API (interface)
- Create a simple program on a device



# Start with Visual Studio Code


Create a folder for this week's lab, like `ttm4175-iot`, and open this folder in VS Code.


# Install the Device Simulator Express


Install the device simulator express extension.

---
type: figure
source: figures/iot/dse-1.png
caption: "Installation of the Device Simulator Extension."
---

1. Click on the side bar for extensions.
2. Search for the *device simulator*.
3. Click *Install*.

This also installs other required Python extensions.

You can later check out the [documentation](https://code.visualstudio.com/docs/).

There is also a special tutorial for coding Python.
https://code.visualstudio.com/docs/python/python-tutorial


:aside: <a href=""><img width="100" src="figures/iot/podcast-python-dse.png"/></a><br/>
Device simulator was created by a couple of interns at Microsoft Garage. 
You can listen to them in a Podcast episode at [Talk Python To Me](https://overcast.fm/+F4RBtyfvE).




# Device Simulator Commands

VS Code has a [Command Palette](https://code.visualstudio.com/docs/getstarted/userinterface#_command-palette), which you can open using the following keyboard shortcuts:

- On Windows: `Ctr-Shift-P`
- On Mac: `Cmd-Shift-P`

For the device simulator, we will use two commands, one for **creating new files** and for **opening the simulator**.

---
type: figure
source: figures/iot/dse-2.png
caption: "Installation of the Device Simulator Extension."
---

When you run one of these commands, the device simulator asks you which device it should simulate. 
You can select between three different devices:

- The **BBC micro:bit**
- The **CLUE**
- The **Circuit Playground Express**

---
type: figure
source: figures/iot/dse-3.png
caption: "Commands ask you which device you want to simulate."
---


# Run a Test Program


Create a file `hei.py` with the following content:


```python
from microbit import display

while True:
	display.show("HEI!")
```


Open the device simulator with the command from above, and select the **micro:bit** as device. You should see the simulator to the right side of the editor, like this:

---
type: figure
source: figures/iot/dse-4.png
caption: "Commands ask you which device you want to simulate."
---


When you now click the start-button under the device, it should blink like this:


---
type: figure
source: figures/iot/hei-microbit.gif
caption: "The blinking display of the microbit."
---

:report: Remove the while-loop, so that `show()` is only executed once. What happens?


# Controlling the Device


The microbit has several electronic components that you can interact with. It's of course more fun to interact with the real device, but the simulator is doing a good job at providing access to most of the electronic components. (And the Python code is the same.)

To interact with the electronic components, we use a Python library. This is a set of Python code that provides an interface to the microbit. Such an interface is also called an **API**, or application programming interface.


### Buttons

The Microbit has two buttons, `A` and `B` which can be also pressed at the same time.

---
type: figure
source: figures/iot/dse-buttons.png
---
 
- [Examples from microbit.org](https://microbit.org/get-started/user-guide/python/#buttons)
- [button](https://microbit-micropython.readthedocs.io/en/v1.0.1/button.html)


### Display

The Mircobit has 9 LEDs that make up its main display. It can show text or simple images.

---
type: figure
source: figures/iot/dse-leds.png
---

* [display.show(...)](https://microbit-micropython.readthedocs.io/en/v1.0.1/display.html#microbit.display.show)
* [display.scoll(...)](https://microbit-micropython.readthedocs.io/en/v1.0.1/display.html#microbit.display.scroll)
* [display.clear()](https://microbit-micropython.readthedocs.io/en/v1.0.1/display.html#microbit.display.clear)
* [Display images](https://microbit-micropython.readthedocs.io/en/v1.0.1/image.html)


### Temperature

---
type: figure
source: figures/iot/dse-temperature.png
caption: "In the simulator, you imitate the temperature with a slider."
---

* [temperature()](https://microbit-micropython.readthedocs.io/en/v1.0.1/microbit.html?highlight=temperature#microbit.temperature)


### Light Sensor

The LEDs of the display may also give you an indication of the amount of light shining onto the device.

---
type: figure
source: figures/iot/dse-light-sensor.png
caption: "In the simulator, you imitate the light level with a slider."
---

* [display.read_light_level()](https://microbit-micropython.readthedocs.io/en/v1.0.1/display.html#microbit.display.read_light_level) 


### Accelerometer

An accelerometer measures the acceleration into different directions.
Combined it can also detect movements or gestures.

---
type: figure
source: figures/iot/dse-accelerometer.png
caption: "In the simulator, you imitate the acceleration with sliders in each dimension."
---

* [accelerometer.was_gesture('shake')](https://microbit-micropython.readthedocs.io/en/v1.0.1/accelerometer.html#microbit.accelerometer.was_gesture) Detect a gesture.
* [other functions](https://microbit-micropython.readthedocs.io/en/v1.0.1/accelerometer.html)
* [Examples from microbit.org](https://microbit.org/get-started/user-guide/python/#accelerometer-readings)
* [Examples from microbit.org](https://microbit.org/get-started/user-guide/python/#gestures)


### Other Functions

* [random.randint(a, b)](https://microbit-micropython.readthedocs.io/en/v1.0.1/random.html#random.randint) Generate a random integer `n` so that `a <= n <= b`

* [sleep(n)](https://microbit-micropython.readthedocs.io/en/v1.0.1/microbit.html?highlight=temperature#microbit.sleep) Sleep for n microseconds.



# Focus: Exploring an API

In the section above, we show you a couple of functions that you can use to control the Microbit. 
Whenever you do programming, exploring an API will be an important part of your work. 
There are several strategies, which you will also mix as you go along.

### Question 1: Which Functions Do I Need?

First you need to find out which functions there are at all, and how they are called. 

* Look at a tutorial. 
* Read a book.
* Take a course.
* Search on the web.

### Question 2: How Can I use these functions?

Once you first know which function you need to use, you need to figure out how to use it. This means:
* How do I use this function?
* Which parameters are there?
* What do the parameters do? 

These more detailed questions you can figure out in different ways:
* Looking at the source code of the library.
* Browsing an API documentation
* Tool Support `Shift-Space`


### Experience, Experience...

After some time, you will also become more experienced with APIs, and sometimes you can guess which functions there probably are and how they are most likely called. In that case, you can start typing and look in the auto-completion for something that matches. 



# Application Pattern


Some of the applications of an IoT device follow a very simple programming pattern, in which it waits for a condition to be true, and then does something. This is illustrated in the code skeleton below:


---
type: figure
source: figures/iot/iot-application-pattern.png
---


* The outer while loop keeps the device running. As soon as you reach the end, it starts again at the top of the loop.
* The if-statement checks for one or more conditions. It can for example read the temperature sensor, ask if a button was pressed or a gesture detected. 
* Depending on the detected case, the device can react with different actions, like showing something on the display.
* The sleep statement lets the device pause for a bit. It specifies a number of microseconds that the device does nothing and waits before it goes into the next iteration and starts again at the top of the while-loop. The sleep is not necessary for all cases, but can be useful when you show something on the display and keep it visible for some time. In a real device that is powered by a battery, sleeping also helps to preserve energy. (This is usually implemented with a different method than sleep as shown here, but the principle for the code is the same.)


# Import Statements

```python
from microbit import *
```

If you select this, then you import all the functions that the Microbit package declares. The benefit is that you don't need to worry about the import statements in your code. 
The downside is that someone reading your code does not already see at the top which functions you are going to use.

```python
from microbit import button_a
```

You can also explicitly import only those functions that you need.


# Application Examples

Let's combine the functions from above with the general application pattern to build some examples. In the following, we show you some of the ideas of the [Microbit documentation](https://microbit.org/get-started/user-guide/python/).

:task: Go through each of the application examples. Try to sketch a solution individually first, then together in your team. Try to make it run. Then compare your solution with the one given in the documentation.


## Nightlight

Detect that it is getting dark and turn on the display. 

* [Tutorial](https://microbit.org/projects/make-it-code-it/nightlight/?editor=python)


## Dice

Detect that the device was shaken, and print a random number.

* [Tutorial](https://microbit.org/projects/make-it-code-it/dice/?editor=python)


## Max-Min Thermometer

Measure the temperature regularly. When you press button A, show the minimum temperature. When you press button B, show the maximum temperature.

* [Tutorial](https://microbit.org/projects/make-it-code-it/max-min-thermometer/?editor=python)

**Idea for an extra function**: Reset the temperatures when both buttons are pressed.


# Create Your Own Application

Inspired by the examples, brainstorm around some ideas you could try out with the simulated device.

* Think individually for a few minutes.
* Present your idea —- no matter how good you think it is -- to the others. Collect all ideas, and be positive in this first round.
* Look at the collected suggestions. Which one do you want to build together? Maybe adjust suggestions, or combine ideas.

:task: Build your own application.

:report: Document your application with the help of a series of screen shots and a description. Explain your idea, show the code, and explain how it works.


# Optional Homework

Train with these tutorials also on your own. This is a fun way to learn more programming concepts.
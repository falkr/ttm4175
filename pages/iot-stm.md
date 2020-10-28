

# Lab: State Machines in IoT


### Overview of Tasks

We have created 5 tasks which all let you solve a slightly different problem related to state machines. 
The tasks are independent of each other, but the first one is the easiest to get started and the last one is maybe a bit challenging.

Here's an overview:

1. **Counter**: You run the example, just to check that all works, and explain the behavior in words.
2. **Shake Light**: Create a state machine diagram from code.
3. **Night Light**: Extend a state machine diagram, and extend its code.
4. **Switch Light**: You get the state machine diagram, but build all code on your own.
5. **Hand Sanitizer Station**: You create state machine diagram and code by yourself from a textual description.




# Counter

Goal: Get the state machine code running, to check that all works.


We have created the files for today's tasks, and you can download them from a Git repository as a zip-file. 

* Download the file <https://github.com/falkr/ttm4175-microbit-stms/archive/main.zip>.
* Unzip it, usually by double-clicking on it.
* Open the folder in VS Code.

:aside: [Git](https://git-scm.com) is a version control system. Usually you would clone a repository so you could make changes to it and send them back to me, but for this exercise you only need the files once, which is why you only download the repository as a simple zip-file.


You should see the following files:

* counter.py
* night.py
* sanitizer.py
* shake.py
* switch.py


All files are self-contained and can run independently of each other, that means, all contain the base state machine.


### Diagram for the Counter

---
type: figure
source: figures/statemachines/counter.svg
---

The counter is an electronic version of a hand counter, like the one they use on airplanes to count how many passengers are on board. Ours is made for very small planes --- it can only count to 10.

:task: Describe in words how you expect, by looking at the diagram, the counter will work. Include this description in your report.


### Run the Counter

Using the same commands as last week, run the file `counter.py` in the device simulator, and try out if the counter works as you have described. 





# Shake Light

Goal: Create a state machine diagram from given code.


Have a look at the code in file `shake.py`, and run it. (The code of the state machine is also included below.) 

```python
class ShakeLight(StateMachine):
    """Switch on the light if you shake the device
    and turn it off again after 2 seconds.
    """

    def initial_transition(self, timers):
        display.show(Image.SQUARE_SMALL)
        return "off"

    def transition(self, state, event, timers):
        if state == "off":
            if event == "shake":
                display.show(Image.SQUARE)
                timers.start("t1", 2000)
                return "on"
        elif state == "on":
            if event == "t1":
                display.show(Image.SQUARE_SMALL)
                return "off"
```

:task: Describe the behavior of the shake light in a few sentences.


:task: Draw a state machine that corresponds to the code. Make sure to include all necessary elements. 


# Night Light

Goal: Extend a given diagram to extends its functionality, and extend the corresponding code.


---
type: figure
source: figures/statemachines/stm-night-light-1.svg
---

Above you see the partial state machine of a night light, which depends on the light level, and switches on when it reaches > 100. 

Extend the state machine so that it also switches the light off again after the level goes under 80.

Add the code for the added functionality.


# Switch Light

Goal: Get the diagram, but build all code on your own.


---
type: figure
source: figures/statemachines/stm-switch-light.svg
---

Above is the diagram for a light that can be switched on and off. 

:task: Have a close look at the diagram, and describe what it does in words. 


:task: Build the entire code for the state machine. Use the code given in file `switch.py` as starter. (You only have to fill the content of the both transition functions.)


# Hand Sanitizer Station

Goal: Create diagram and code by yourself.

---
type: figure
source: figures/statemachines/dispenser.png
---

Create the state machine for a hand santizer. 
These machines, as you know, detect that someone puts their hand under the dispenser, then run a motor for 800 milliseconds to dispense some sanitizer. 

To avoid double-dispensing, the machine ignores a repeated dispensing for about 2 seconds, that means, you need to wait for 2 seconds before it dispenses another load. (Sometimes irritating if you want a double dose...)

Create such a state machine! 

* Try to sketch one on your own, each one individually for a few minutes. 
* Compare your solutions.
* Use the state machines to understand the function better. Do you all agree on what the system should _exactly_ do? 

Some hints:

* Assume that a detected hand is signalled by event `shake`. That means, if the shale event is detected, the dispenser should dispense a dose by switching on its motor.
* Instead of switching on a motor, just show an arrow pointing downwards (`Image.ARROW_S`) on the display.
* Make sure it does activate the dispenser (by showing the arrow) for the 800 milliseconds.
* Make sure it does not double dispense within 2 seconds after the first detected shake.


:tip: The state machine we came up with has three control states, which we called for `ready`, `dispensing` and `blocked`. The names do not matter, but may indicate what happens in them.


:task: Document the solution of your dispenser as detailed as possible, to explain to the reader how it works. Include a comic-like sequence of screenshots, too.

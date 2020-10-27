# Basis Code for State Machines

The code below is the basis code for all state machines.
Copy this code **before** the definition of your own state machines.


```python
from time import time
from microbit import button_a, button_b, accelerometer, display, sleep, Image

ON = Image.SQUARE
OFF = Image.SQUARE_SMALL


class StateMachine:
    """
    The following code segment defines a basis state machine.
    Leave this code as it is. (Or be careful what you do.)"""

    def __init__(self, timer_names=["t1", "t2", "t3"]):
        self.active = False
        self.state = "initial"
        self.timer_names = timer_names
        self.timers = {}

    def _ticks_ms(self):
        return int(round(time() * 1000))

    def initial_transition(self, timers):
        """Overwrite this method to define the initial transition.
        Must return the name of the first state."""
        return None

    def transition(self, state, event, timers):
        """Overwrite this method to define the transitions.

        `state` - the current state
        `event` - the triggering event
        `timers` - to start and stop timers

        Return the name of the next state,
        or None to stay in current state."""
        return None

    def start(self, name, timeout):
        """Start a timer.
        The name must be t1, t2 or t2.
        The timeout is given in milliseconds.
        """
        self.timers[name] = self._ticks_ms() + timeout

    def stop(self, name):
        """Stop a timer."""
        self.timers[name] = None

    def _detect_event(self):
        now = self._ticks_ms()
        for timer in self.timer_names:
            if (timer in self.timers) and (self.timers[timer] is not None):
                if self.timers[timer] < now:
                    self.timers[timer] = None
                    return timer
        if button_a.was_pressed():
            return "button_a"
        if button_b.was_pressed():
            return "button_b"
        if accelerometer.was_gesture("shake"):
            return "shake"
        return None

    def run(self):
        """Run the state machine."""
        self.active = True
        while self.active:
            if self.state == "initial":
                next_state = self.initial_transition(self)
                if next_state:
                    if next_state == "final":
                        self.active = False
                    self.state = next_state
            event = self._detect_event()
            if event is not None:
                next_state = self.transition(self.state, event, self)
                if next_state:
                    self.state = next_state
            sleep(100)
```




# Example 1: Shake Light

---
type: figure
source: figures/statemachines/stm-shake-light.svg
---


```python
class ShakeLight(StateMachine):
    """Switch on the light if you shake the device
    and turn it off again after 2 seconds.
    """

    def initial_transition(self, timers):
        display.show(OFF)
        return "off"

    def transition(self, state, event, timers):
        if state == "off":
            if event == "shake":
                display.show(ON)
                timers.start("t1", 2000)
                return "on"
        elif state == "on":
            if event == "t1":
                display.show(OFF)
                return "off"

stm = ShakeLight()
stm.run()
```



# Example 2: Night Light

---
type: figure
source: figures/statemachines/stm-night-light.svg
---

```python
class NightLight(StateMachine):
    """Periodically read the light level.
    If the light level is above 100, switch on the light.
    If it is below 80, switch the light off again.
    """

    def initial_transition(self, timers):
        display.show(OFF)
        timers.start("t1", 1000)
        return "off"

    def transition(self, state, event, timers):
        if state == "off":
            if event == "t1":
                if display.read_light_level() > 100:
                    display.show(ON)
                    timers.start("t1", 1000)
                    return "on"
                else:
                    timers.start("t1", 1000)
                    return "off"
        elif self.state == "on":
            if event == "t1":
                if display.read_light_level() < 80:
                    display.show(OFF)
                    timers.start("t1", 1000)
                    return "off"
                else:
                    timers.start("t1", 1000)
                    return "on"

stm = NightLight()
stm.run()
```


# Example 3: Switch Light

---
type: figure
source: figures/statemachines/stm-switch-light.svg
---

```python
class SwitchLight(StateMachine):
    """Switch between states off and on by pressing button A.

    The change between on and off only happens if button A is pressed
    twice quickly.

    State off is represented by a small square,
    state on with a big suqare.

    The transitional states between on and off are shown
    with arrows up and down.
    """

    def initial_transition(self, timers):
        display.show(OFF)
        return "off"

    def transition(self, state, event, timers):
        if state == "off":
            if event == "button_a":
                display.show(Image.ARROW_N)
                timers.start("t1", 300)
                return "almost_on"
        elif state == "almost_on":
            if event == "button_a":
                display.show(ON)
                return "on"
            elif event == "t1":
                display.show(OFF)
                return "off"
        elif state == "on":
            if event == "button_a":
                display.show(Image.ARROW_S)
                timers.start("t2", 300)
                return "almost_off"
        elif state == "almost_off":
            if event == "button_a":
                display.show(OFF)
                return "off"
            elif event == "t2":
                display.show(ON)
                return "on"

stm = SwitchLight()
stm.run()
```


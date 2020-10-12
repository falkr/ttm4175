


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
Currently, you can select between three different devices:

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


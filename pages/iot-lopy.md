# Getting Started with the LoPy



# Building the LoPy

The LoPy consists of several parts:

- The main board with the processor and the radio
- The expansion board, with LED, button and access to pins, USB, and power supply
- The antenna

We have version 2.1A of the expansion board and version `XX`of the LoPy.

Put together the parts carefully as shown in the picture below. Note that the LoPy fits both ways onto the expansion boards. Make sure the pins for `Vin` and `GND` align properly. With the version we have, this looks like this:

---
type: figure
source: figures/iot/lopy-expansion-2.png
---

Make sure you connect the antenna to the right antenna, close to the big white LED as shown above. We connect the antenna already now since using the radio without the antenna attached may damage the LoPy.

---
type: figure
source: figures/iot/lopy-antenna.png
---

---
type: figure
source: figures/iot/lopy-antenna-2.png
---

## Important Warning:

Don't shortcut the LoPy by putting it on a metallic surface, like a MacBook. That'll kill it.

---
type: figure
source: http://recipes.item.ntnu.no/wp-content/uploads/2017/11/lopy-vs-macbook-300x142.jpg
---

Also, don't activate the LoRaWan radio without the antenna connected.



# Updating the Firmware

**Goal:** You can connect the LoPy to your computer and have the latest firmware for the LoPy installed.

We now need to update the firmware on the LoPy, that is, the software that is installed on it.

:aside: _Firmware_ is software that takes care of hardware-related issues. It is hence somewhere between the hardware and the actual software, which is the application that we are going to write. Hence the name.


## Update Tool

Install the update tool, either for [Windows](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=win32&redirect=true) or [Mac](https://software.pycom.io/findupgrade?product=pycom-firmware-updater&type=all&platform=macos&redirect=true).

## For Expansion Board 2.0

(This is the board we have.)

1. Make sure the LoPy is **not** connected to your computer yet.
2. Connect a jumper cable between `G23` and `GND`
3. Reconnect the LoPy via USB to your computer, this puts the device in _firmware update mode_.
4. Run the Firmware Upgrade tool

---
type: figure
source: figures/iot/lopy-update.png
---

5. Unplug the LoPy
6. Remove the `G23` to `GND` jumper cable.
7. Reboot the device (button or power off then on).

:tip: If you are having any issues, make sure the TX and RX jumpers are present on your Expansion Board, as the jumpers sometimes come loose in the box during transport. Without these jumpers, the updater will fail.

:tip: If you succeeded updating the firmware, offer your help to other teams if they struggle, and offer to update their LoPy. (It is not important from which computer the LoPy gets updated.)


# Programming the LoPy

**Goal:** You can run Python code on the LoPy.

You can program the LoPy with a plugin that is called **Pymakr**, which you can use either with the editors Atom or Visual Studio Code. 

## Installing the Pymakr Plugin

1. Decide if you want to install [Atom](https://atom.io) or [Visiual Studio Code](https://code.visualstudio.com). (Both share the same code base, and for our lab, both work.)
2. Follow the instructions for installing the Pymakr plugin, depending on the ide either [Pymakr for Atom](https://docs.pycom.io/pymakr/installation/atom/) or [Pymakr for Visual Studio Code](https://docs.pycom.io/pymakr/installation/vscode/)
    - Only connect via USB and ignore the Telnet instructions.


## Create a New Project

- Create a new folder
- Open this folder as a new project.
- Create a new file `main.py`, and copy in the following code:


```python
import pycom
import time

pycom.heartbeat(False)

while True:
    pycom.rgbled(0xFF0000)  # Red
    time.sleep(1)
    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)
    pycom.rgbled(0x0000FF)  # Blue
    time.sleep(1)
```

- Go through the code line-by-line
- Explain to each other what the code does. (By now, your Python skills form the other course should be enough to understand what is going on here.)
- Find the `Run` command in the editor, and run the main file on the LoPy.

---
type: figure
source: figures/iot/lopy-run.png
---

Now you should see the LED of the LoPy changing its colors. 

Feel free to modify your program. Can you produce more exciting colors?



# Connecting to LoRa

**Goal:** You connect you LoPy to the LoRaWAN network.

## Get the MAC Address

The LoRa module has a MAC address, which we will use as the device ID when connecting to the LoRaWAN network. To find the MAC address, create a new project in the editor and run the following program:

```
from network import LoRa
import binascii
lora = LoRa(mode=LoRa.LORAWAN)
print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))
```

## Get the App EUI and App Key

- Go to MS Teams / TTM4175 / Files / LoPy Device IDs
- Write in your MAC address.
- Wait for the App EUI and the App Key to appear. (We are registering the device)


## Connecting to LoRaWAN

- Create a new project
- Create a main.py file with the content below
- Exchange the variables with `app_eui` and `app_key` with the correct values for you
- Run the program
- If you connect successfully, mark it with `ok` in the last column of the table on Teams


```python
from network import LoRa
import socket
import time
import ubinascii

# Initialise LoRa in LORAWAN mode.
# Europe = LoRa.EU868
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# create an OTAA authentication parameters
app_eui = ubinascii.unhexlify('70B3D57ED00XXXXXXX')
app_key = ubinascii.unhexlify('D822576F285B93AC10F87B4FXXXXXXXX')

# join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)

# send some data
s.send(bytes([0x01, 0x02, 0x03]))

# make the socket non-blocking
# (because if there's no data received it will block forever...)
s.setblocking(False)



# get any data received (if any...)
data = s.recv(64)
print(data)
```


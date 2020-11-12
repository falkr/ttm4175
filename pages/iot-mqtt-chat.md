# Chatting via MQTT

**Goal:** We want to use a simple Chat UI to create a chat system so that all teams can chat together. Our chat should then have the following features:

* Sends **messages**.
* Sends **delivery receipts**, so that the sender sees that a message has reached the device of the receiver.
* Sends **read receipts**, so that the sender knows when the message was visible in the user interface.
* Sends **typing hints**, so that chat partners see when the other side is starting to type a message.



## The Chat User Interface

The Chat UI is a Python class that shows the history of chat messages with each contact, and allows us to send messages. 
We interact with it in two ways:

* By function calls, when we want to change something in the UI. That means, we want to do something, and we cause an effect in the user interface. These are events that are **initiated outside** of our specific user interface instance.
* By callbacks, when the UI wants to inform us about something, like that the user clicked the "Send" button and wants to send a chat message. These are events that are initiated by our user working with the user interface, that means, **initiated inside** of the user interface.


## Chat UI Function Calls

Here a list of things that we want the user interface do when we ask it to.
This is done by function calls.

### Receiving Messages

When we receive a message, we tell the UI by calling the following function:

```python
gui.receive(sender, message, uuid)
```

The sender is the originator of the chat message, and message is the content of a message as a string. 
Each message is associated with a [UUID, a universally unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier).
This is a unique name, so that we later can associate delivery and read receipts with each message.


### Receiving Delivery Receipts

We can tell the UI that we received a delivery receipt by calling the following function:

```python
gui.receipt_delivered(sender, uuid)
```

The user interface will then add the suffix _(delivered)_ behind the message.


### Receiving Read Receipts

We can tell the UI that we received a read receipt by calling the following function:

```python
gui.receipt_read(sender, uuid)
```

The user interface will then add the suffix _(read)_ behind the message.


### Receiving Typing Hints

We can tell the UI that we received a typing indication with the following call:

```python
gui.typing(sender)
```

The user interface will then show _Team 1 is typing..._ right under the conversation list with that contact.


## Chat UI Callbacks

But what about actions that originate at the user interface? Like when the user clicked the _Send_ button --- then the user interface wants to call us, so that we can forward that chat message.


### Sending Messages

Messages are sent when the sender writes a message in the message field and clicks _Send_. 
The UI lets us know about this by calling the following function:

```python
def on_send(sender, receiver, message, uuid):
    # publish message via MQTT
```


### Read Receipts

When a message is read, the UI calls the following function. This happens whenever the chat history gets visible to the user.

```python
def on_read(sender, receiver, uuid):
    # publish read receipt via MQTT
```




### Typing Hints

Whenever we start typing, we send a typing hint to the chat contacts. 
The UI informs us about typing with the following function:

```python
def on_type(sender, receiver):
    # publish typing hint via MQTT
```





# Install the Chat UI



The UI is written with a libray that is called DearPyUI. You can install it as usual:

```bash
python -m pip install dearpyui
```

On windows, you may receive the following error message when you start the program:

```bash
>>> import dearpygui.*
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ImportError: DLL load failed: The specified module could not be found.
```

This is a known issue, [discussed here](https://github.com/hoffstadt/DearPyGui/issues/298). The solution is simple:

* Install **vc_redist.x64.exe** from <https://support.microsoft.com/en-gb/help/2977003/the-latest-supported-visual-c-downloads>. Then the program should run. 


### Chat UI Code

You can download a zip file with all source code for today's lab here: <https://github.com/falkr/ttm4175-chat/archive/main.zip>

Unzip it and open it in Visual Studio Code.





# Step 1: Test the UI

In this part, we only test how the user interface works, we are not yet sending any real messages between each other.
Your task will only be to test the user interface and describe how it works, so that you get an understanding for it.

This is the code to test the user interface. Place it in a file `test_chat_gui.py` in the same folder that you downloaded above, where also the file `chat_gui.py` is located.



```python
from chat_gui import ChatGui

# Change this to match your team!
my_id = "team1a"


def on_send(sender, receiver, message, uuid):
    print("Sending {} --> {} {}".format(sender, receiver, message[:5] + "..."))


def on_type(sender, receiver):
    print("Typing: {} --> {}".format(sender, receiver))


def on_read(sender, receiver, uuid):
    print("Read: {} --> {} {}".format(sender, receiver, uuid[:5] + "..."))


gui = ChatGui(my_id, on_send=on_send, on_type=on_type, on_read=on_read)

# We send in a fake message:
# gui.receive("x6", "Dette er en fake medling!", "absgdeff")

# We fake that chat partner x5 starts typing:
# gui.typing("x5")

gui.show()
```

:task: Change the value of the variable `my_id` to match your team name. The team names have the form `team1a`, 'team1b', ... `team12b`. The ids `x1` to `x6` are for testing and the student assistants.



### Testing Sending of Messages and Outgoing Typing Indicators

* Start writing a text, and have a look at the terminal in which you started the Python program. Which debug output do you get?
* Pause typing for 5 seconds, then type again. What happens?
* With some message in the message field, press the `Send` button. What happens in the UI and in the console?
* Type again some text, and press `Send To All` this time. What happens?


### Testing Receiving and Read Receipts

For this test, we need to fake that we receive a message, we do that by using the method `gui.receive()`, where we send in a message. **Activate this by uncommenting the line of code that sends a fake message.**

* Start the program. The UI window should show as before the conversation with the first team selected. 
* Observe the terminal again for any output messages.
* In the UI, switch to the conversation with `x6`. What happens in the output?


### Testing Incoming Typing Indicators

Our typing indicators behave a little bit different from other chat application, to make things a bit simpler for now.
Let's test them.
**Activate this by uncommenting the line of code that sends a fake typing indication.**

* Switch to the conversation with `x5`. What do you see in the user interface?
* Now switch to another conversation, then back to `x5`. What do you observe?





# Step 2: Chat Messages via MQTT


To send chat messages via MQTT between contacts, we need to agree on the content of the MQTT message and how we use our topics for publishing and subscribing.

**Topic:** We publish messages that carry a chat message to the topic `ttm4175/chat/<receiver>/message`. The `<receiver>` is the name of the contact we want to send the message to. So, if we want to send a chat message to team2a, that topic is `ttm4175/chat/team2a/message`

**Payload:** The payload should be a json-formatted string, with the following fields:

```json
{"sender": "team1a",
 "receiver": "team2a",
 "message": "Hei!",
 "uuid": "16fd2706"}
```

:task: Check carefully to which topic you should subscribe so that you can **receive** messages for your team name.



### Chatting via MQTT.Fx

Let us first chat by MQTT only, that means, without the Chat UI from above. 
We only want to use MQTT.Fx, and send and receive "raw" chat messages.

Install MQTT.Fx, as [explained in the preparation](prep-iot-mqtt.html#debugging-with-mqtt.fx).

Add our broker that runs on campus. It has the address `mqtt.item.ntnu.no` and uses the default port `1883`.

---
type: figure
source: figures/mqtt/mqtt-fx-broker-1.png
caption: "Open the broker configurations and add our MQTT broker."
---

---
type: figure
source: figures/mqtt/mqtt-fx-broker-2.png
caption: "Configuration for the broker."
---


In MQTT.Fx, connect to the broker. 


---
type: figure
source: figures/mqtt/mqtt-fx-broker-3.png
caption: "The green light indicates that you are connected to the broker."
---

On the _Subscribe_ tab, enter the topic you need to subscribe to (from the task above).

---
type: figure
source: figures/mqtt/mqtt-fx-broker-4.png
caption: "For each subscription you get an entry in the list to the left."
---

:task: Work together with another team. Make sure both teams have the correct topics, and send messages between each other. 

You can publish messages on the _Publish_ tab. Enter the payload in the text field below. It can already be the json-formatted content for a complete chat message. Note that you see received messages on the _Subscribe_ tab.

---
type: figure
source: figures/mqtt/mqtt-fx-broker-5.png
caption: "On the publish tab, you can send chat messages."
---



# Step 3: Connecting Chat GUI and MQTT

So far, this happened:

* In Step 1, we had a look at the chat user interface to get familiar with it, but we did not send any chat messages.
* In Step 2, we used MQTT and MQTT.Fx to send messages between each other, in some raw way, without a proper chat user interface.

Now we want to connect the chat user interface with MQTT, so that we can send and receive messages. We will not yet send receipts or typing indications.



### Code

The following code connects MQTT with that of the Chat UI:

```python
from chat_gui import ChatGui
import paho.mqtt.client as mqtt
import json

# TODO change this to your ID
my_id = "team1a"


# Called by MQTT client when we are connected
def on_connect(mqttc, obj, flags, rc):
    print("Connected: " + str(rc))


# Called by the MQTT client for every message we receive
def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    try:
        data = json.loads(msg.payload)
    except json.JSONDecodeError as e:
        print("The payload is not valid json!")
        print(e)
        return
    if msg.topic.endswith("message"):
        gui.receive(data["sender"], data["message"], data["uuid"])
    else:
        print("Unknown topic: {}".format(msg.topic))


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.connect("mqtt.item.ntnu.no", 1883)
mqttc.loop_start()
mqttc.subscribe("ttm4175/chat/{}/#".format(my_id))


# Called by the Chat UI when we want to send a message
def on_send(sender, receiver, message, uuid):
    print("Sending {} --> {} {}".format(sender, receiver, message[:5] + "..."))
    payload_dict = {
        "sender": sender,
        "receiver": receiver,
        "message": message,
        "uuid": uuid,
    }
    payload_json = json.dumps(payload_dict)
    mqttc.publish("ttm4175/chat/{}/message".format(receiver), payload=payload_json)


# Called by the Chat UI when we start typing to somebody
def on_type(sender, receiver):
    print("Typing: {} --> {}".format(sender, receiver))


# Called by the Chat UI when we have read a message
def on_read(sender, receiver, uuid):
    print("Read: {} --> {} {}".format(sender, receiver, uuid[:5] + "..."))


gui = ChatGui(my_id, on_send=on_send, on_type=on_type, on_read=on_read)
gui.show()
```


Let's look at some details here:

The following line defines a string for a topic. The `format()` function replaces the contained pair of curly braces `{}` with the value of variable `my_id`.  

```python
"ttm4175/chat/{}/#".format(my_id)
```

### Send a Message via MQTT.Fx




# Connecting Chat GUI and MQTT, Step 2

By now, basic sending of messages should work, but we do not yet send delivery receipts, read receipts, typing indications.
Let's look at the MQTT message payloads and topics that we are going to use for those:


### Delivery Receipts


When a message is delivered to a client, that means, received via MQTT, we acknowledge its delivery by publishing an MQTT message to the topic: `ttm4175/chat/<receiver>/delivered`

```json
{"sender": "team1",
 "receiver": "team2",
 "status": "delivered",
 "uuid": "16fd2706"}
```

The original sender receives this delivery receipt and feed is back to the UI, so that it can add a delivery receipt to the message. Note that the sender field is here the sender of the delivery receipt.



### Read Receipts

Read receipts are sent to topic `ttm4175/chat/<receiver>/read`.

```json
{"sender": "team1",
 "receiver": "team2",
 "status": "read",
 "uuid": "16fd2706"}
```

### Typing Indications

Typing indications are sent to topic `ttm4175/chat/<receiver>/typing`.

```json
{"sender": "team1",
 "receiver": "team2",
 "status": "typing"}
```


:task: Check from the code to which topic we subscribe. Why can we manage by just subscribing to a single topic?
What would be an alternative?







# Chatting Together





# Task

Create a sequence diagram between 

* The sender starts typing, and takes 20 seconds to type a message.
* The sender sends the message, which then arrives at the receiver.
* The user on the receiver side eventually reads the message.


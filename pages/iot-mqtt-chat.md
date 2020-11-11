# Chatting via MQTT

**Goal:** We want to use a simple Chat UI to create a chat system so that all teams can chat together. Our chat should then have the following features:

* Sends **messages**.
* Sends **delivery receipts**, so that the sender sees that a message has reached the device of the receiver.
* Sends **read receipts**, so that the sender knows when the message was visible in the user interface.
* Sends **typing hints**, so that chat partners see when the other side is starting to type a message.


## Chat UI Function Calls

The Chat UI is a Python class. We interact with it in two ways:

* By function calls, when we want to change something in the UI.
* By callbacks, when the UI wants to inform us about something.


### Receiving Messages

When we receive a message, we tell the UI by calling the following function:

```python
gui.receive(sender, message, uuid)
```

Each message is associated with a [UUID, a universally unique identifier](https://en.wikipedia.org/wiki/Universally_unique_identifier). This is a unique name, so that we later can associate delivery and read receipts with each message.


### Receiving Delivery Receipts

We can tell the UI that we received a delivery receipt by calling the following function:

```python
gui.receipt_delivered(sender, uuid)
```


### Receiving Read Receipts

We can tell the UI that we received a read receipt by calling the following function:

```python
gui.receipt_read(sender, uuid)
```


### Receiving Typing Hints

We can tell the UI that we received a typing indication with the following call:

```python
gui.typing(sender)
```

## Chat UI Callbacks


### Sending Messages

Messages are sent when the sender writes a message in the message field and clicks `Send`. 
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

In this function, we send the read receipt to the originator of the message:



The originator of the message the forwards the read receipt into the UI so that it can add the read receipt to the message.



### Typing Hints

Whenever we start typing, we send a typing hint to the chat partner. The UI informs us about typing with the following function:

```python
def on_type(sender, receiver):
    # publish typing hint via MQTT
```

We forward this typing hint by publishing the following MQTT message:





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





# Test the UI

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

:task: Change the value of the variable `my_id` to match your team name.


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




# Connecting Chat GUI and MQTT, Step 1

Now we connect the chat UI with the MQTT client, so that we can send and receive chat messages. (We will not yet send receipts or typing indications.)



### Messages

topic: `ttm4175/chat/<receiver>/message`

```json
{"sender": "team1",
 "receiver": "team2",
 "message": "Hei!",
 "uuid": "16fd2706"}
```

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
mqttc.subscribe("ttm4175/chat/{}/#".format("team1a"))


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



# Connecting Chat GUI and MQTT, Step 2

By now, basic sending of messages should work, but we do not yet send delivery receipts, read receipts, typing indications.
Let's look at the MQTT message payloads and topics that we are going to use for those:


### Delivery Receipts


When a message is delivered to a client, that means, received via MQTT, we acknowledge its delivery by publishing an MQTT message:

topic: `ttm4175/chat/<receiver>/delivered`

```json
{"sender": "team1",
 "receiver": "team2",
 "status": "delivered",
 "uuid": "16fd2706"}
```

The original sender receives this delivery receipt and feed is back to the UI, so that it can add a delivery receipt to the message. Note that the sender field is here the sender of the delivery receipt.



### Read Receipts

topic: `ttm4175/chat/<receiver>/read`

```json
{"sender": "team1",
 "receiver": "team2",
 "status": "read",
 "uuid": "16fd2706"}
```

### Typing Indications

topic: `ttm4175/chat/<receiver>/typing`

```json
{"sender": "team1",
 "receiver": "team2",
 "status": "typing"}
```


To which topic do we need to subscribe?


### Adjust your ID

### Send a Message via MQTT.Fx



# Chatting Together





# Task

Create a sequence diagram between 

* The sender starts typing, and takes 20 seconds to type a message.
* The sender sends the message, which then arrives at the receiver.
* The user on the receiver side eventually reads the message.


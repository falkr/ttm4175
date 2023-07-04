# Debugging With MQTTX


MQTTX is a tool useful during development. Using MQTTX is
simple, but because we have now talked about brokers, clients,
publishers and subscribers, you may lose track and wonder what
MQTTX does: Think of it as a testing and helper tool for MQTT.
Essentially, MQTTX is a MQTT client, and connects to an
MQTT broker, subscribe to topics and send messages to topics.
You can subscribe to topics and hence listen to everything that happens in the system. You can also send messages manually for testing. 


:task: Install [MQTTX](https://mqttx.app) already before the lecture.


---
type: figure
source: figures/mqtt/mqttx-1.png
---


## Connecting to a Broker


1. Start MQTTX
2. Add a connection by clicking on the `+` button. Enter the address `mqtt20.iik.ntnu.no` as hostname. Protocol `mqtt://` is already set by default, and our port should be `1883`. As name you can use the same as the hostname.
3. Click on `Connect`

You should get a green "Connected" message. If not, our broker might be down (contact me then) or you are not connected to the internet. 

---
type: figure
source: figures/mqtt/mqttx-3.png
---


## Publishing a Message

Once you are connected to a broker, and the broker is selected in the list to the left, you can publish a message to a topic using the interface in the lower right corner.

1. Write the topic in the field with the grey label `Topic`
2. Optionally select the QoS level. 
3. In the text field below the topic you can write the payload of the message, and MQTTX gives you the possibility to show it as Plaintext or JSON (these two options are most suitable for us).
4. Click the send symbol on the lower right corner.



## Subscribing to a Topic

1. Once you are connected, click on `+ New Subscription`
2. Enter the topic. Include wildcards `+` and `#` as you need.
3. Set the QoS (default is 0)
4. Click on `Confirm`

You should now be subscribed to a topic. You can test this by sending a message as described above to that topic. You should then see that you have both sent and received that message in the conversation window.

---
type: figure
source: figures/mqtt/mqttx-2.png
---


:task: Subscribe to a topic and then publish a message to that topic, so that you can see that it is sent back to you like in the screenshot above. 

## Observing Communication

Because MQTT uses the publish-subscribe pattern, the MQTTX can simply subscribe
to any topics that are interesting in your application and you can see
which messages are sent to these topics, without disturbing the
communication in the system. 
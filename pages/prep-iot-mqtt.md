# MQTT

This week, you will learn how to communicate by using a protocol that is
called **MQTT**. Like HTTP, it is usually executed on top of TCP/IP, but
you will notice that this protocol is **very different from HTTP**, in many
respects. That's one of the reasons why we look at it. Once you have
understood HTTP and MQTT, you have covered a lot of mechanisms,
properties, patterns and architectures that are used in communication
protocols.

## Learning Goals

:goals: After this week, you will be able to:

- Run and operate your own MQTT broker.
- Create an MQTT client in Python.
- Publish and receive messages, including data payload.
- Select proper quality-of-service levels.
- Design MQTT topics for applications.


# Background: Hacking Ferries

If you want, have a look at this TEDx Talk by Andy Stanford Clark, who is one of the inventors of MQTT. 
The talk is not so much about the MQTT protocol itself, but you'll get some context and background that may help you learn more in the following.

---
type: youtube
video: s9nrm8q5eGg
start: 30
---


# MQTT

MQTT is often used in situations where events should be sent from many
sensors and broadcast to several applications. IBM and others for
instance use MQTT so that IoT devices can send updates into their cloud services.
When Facebook introduced their standalone Messenger application, they
also relied on MQTT to push messages to the clients.

:aside: Read the article [Building Facebook Messenger](https://www.facebook.com/notes/facebook-engineering/building-facebook-messenger/10150259350998920)


MQTT is simple to work with, and the following are my top
5 reasons for using MQTT:

1. **MQTT is simple to debug.** You can have extra clients during development that observe all communication. You can also manually send messages. This makes debugging much easier.
2. **You only need to handle a single IP address.** That is the address of the broker. All other addressing happens indirectly via topics.
3. **Application startup is simple.** You have to start the MQTT broker first, but clients can then connect in any order. The MQTT broker can also be hosted on a server and be always-on.
4. **MQTT works also behind a NAT.** This means you can push a message from any location to a computer that is connected to your router at home. Only the broker needs to be accessible.
5. **MQTT is bi-directional by default.** Any client can send messages to any other client, at any time. You are not restricted to a client-server structure where only the client can initiate interactions.

# Broker Architecture

MQTT is a protocol that is based on the **client-broker** topology. As a
repetition, remember first the client-server architecture, as we have it
for instance in HTTP:

## Client-Server

**Client-server:** The client knows the address of the server. The server gets to know
the client only after the client makes initial contact. Since only
the client knows the address of the server initially, it is only the
clients that can make the first contact and take initiative. In the
world wide web, servers can host web sites and are contacted by
browsers (the clients.) This is an example where there are many
clients and only few servers, and where servers are optimized to
server many clients. But there are also protocols in which the
server is on a tiny sensor device, and "serves" the values of the
sensor to any client that are interested in them.

### Problems with Client-Server

Assume again a home automation system, in which a
controller adjusts the heater (on/off) based on the temperature reported
by several sensors that are distributed in the room. With HTTP, the two
communication parts were client and servers, and the client can send
data to the server or request data via the request-response pattern. We
have hence two possibilities, depending on how we assign the roles of
client and server:

-   **HTTP, sensors act as clients:** The sensors are HTTP clients and
    repeatedly send their temperature measurements to the heater, which
    is acts as an HTTP server.

-   **HTTP, sensors act as servers:** Vice-versa, we can think of a
    solution where each temperature sensor is a HTTP server, and the
    heater acts as a client. The heater makes requests to each sensor
    and asks for the current temperature, and then adjusts the heater
    based on all of the responses.

Assume now that not only the heater module is interested in the
temperature, but also the controller for the window blinds. (If it gets
very warm during the summer, it could move down the blinds to keep the
sun down.) With the above solutions, what would that look like?

-   If the sensors should be the clients, then we now have to update all
    the sensor logic so that they not only send their measurements to
    the heater, but also the blind controller. Even worse, since all
    transmission cost energy, we roughly doubled the energy consumption
    of the sensor nodes, since the communication doubled. This makes
    that the batteries only last half as long!

-   If the sensors act as HTTP servers and we introduce the blind
    controller, they don't have to change their code. They just answer
    now double as many requests; the ones from the heater and the ones
    from the blind controller. For the battery life, this is equally bad
    as the solution above.

The problem with the above scenario is that we used a direct
communication between the sensors and the control units, as shown in the figure below.
Each sensor (in red) is connected to each controller. 

---
type: figure
source: figures/iot/mqtt-without-broker.svg
caption: "This architecture connects each sensor with each client, which is not suitable."
---

## New: Client-Broker

Now imagine a system where the components are more separate from each other, and do not communicate directly with
each other. We can achieve this by introducing a component that
decouples the sensors and the controllers. We call that component a
**broker**, shown in the figure below:

---
type: figure
source: figures/iot/mqtt-with-broker.svg
caption: "This architecture introduces a broker, and sensors only connect to this broker."
---

**Client-broker:** A message broker is a server that distributes messages. 
Clients communicate with the server and send messages to the broker, which then get distributed to those clients that are interested in the events.


The broker is a generic component, which means that it is not specific
for any application and that you can use the same broker for many
different applications. 
You hence don't need to write your own broker,
but can use an existing one and just configure it. There are several
MQTT brokers available. The one we are going to use is called
**Mosquitto**.


# Message Pattern: Publish-Subscribe

With the new architecture of a broker also comes a new message pattern that is suitable for this architecture. It is called **publish-subscribe**.

-   The **publish** part is very simple: Whenever a client (here a
    sensor) makes an observation, it sends a message to the broker. We
    also say that the client *publishes* a message, or that the client
    acts as a publisher.

-   The **subscribe** part works as follows: Clients that are interested
    in a certain information *subscribe* to the broker. Whenever another
    client publishes that information, the broker forwards this message
    to all clients that have subscribed.

A minimal interaction looks as follows:

---
type: figure
source: figures/iot/mqtt-basic.svg
---

In MQTT, clients can be publishers or subscribers, or both. There can be
any number of subscribers and any number of publishers in a system.
Because of the publish-subscribe pattern, the subscribers do not have to
know about the publishers, and the publishers do not have to know of the
subscribers. They only have to know the address of the MQTT broker and
connect to it.

For our home automation system, this enables an elegant and efficient
solution: The sensors at as publishing clients that send their
measurements to the broker. The controllers act as subscriber clients
that subscribe to the broker for temperature updates. Once the broker
receives the temperature updates, it forwards them to the controllers.
When adding a new controller, it can just be a new subscriber that
subscribes to the broker, but the communication and the behavior of the
sensors does not change. Also, each sensor sends every measurement only
once (to the broker), which helps to save energy.

Below you see an example with two subscribers. Only subscriber 2
receives the first published message. Subscriber 1 only receives it
after it also subscribes.

---
type: figure
source: figures/iot/mqtt-publish-subscribe.svg
---


# Topics

Topics are used to define which information a subscriber is interested
in, and match it with the information publishers provide. Usually,
subscribers are not interested in all messages that all publishers send.
Subscribers therefore only subscribe to specific topics, which depend on
the application. The topics are organized in a hierarchy, separated by a
slash ("/"). The following is an example for topics that an application
for home automation can use:

    house/garage/lights/l1
    house/garage/lights/l2
    house/garage/sensors/pi1
    house/garage/doors/d1

The light *l1* for instance subscribes to the topic
`house/garage/lights/l1` so that it can receive messages that switch it
on or off. The passive infrared sensor *pi1* publishes messages to the
topic `house/garage/sensors/pi1` every time it detects a movement.

Topics are hence useful to structure the communication of an application. They are a mechanism that combines some aspect of addressing with that of message names. Central to the concept of topics is that several clients can listen to the same topic.

## Example Application

An application to switch on the lights whenever a movement is detected
can work like this: (In pseudo code)

    subscribe to house/garage/sensors/pi1
    whenever an MQTT message arrives at house/garage/sensors/pi1:
        send a message 
            to house/garage/lights/l1 with payload "on"
        
        after some time, send a message
            to house/garage/lights/l1 with payload "off"
			
## Topic Subscription Wildcards

When subscribing, topics can include wildcards, which make it possible for a client to
subscribe to several topics with a single pattern:

-   The "+" is used as a wildcard for a single level
-   The "\#" is used as a wildcard for several levels. It must only be
    placed at the end of a topic pattern.

Examples:

-   To receive all messages sent within the house, a subscriber can
    subscribe to `house/#`
-   To receive all messages for lights in any zone (garage or kitchen),
    a subscriber can subscribe to `house/+/lights/+`
	

**Exercise:** A publisher sends a message to the topic `a/b/c/d`. Which
of the following 15 subscription topics will receive this message? (Check the boxes when you think a subscriber with the subscription topic will receive the message. Hints are at the bottom of this page, but do it for yourself first.)

<div>
<table class="table table-sm">
<caption style=""></caption>
<thead>
<tr class="row-1">
<th></th><th>Subscription Topic</th><th>Receive a/b/c/d ?</th>
</tr>
</thead>
<tbody class="row-hover">
<tr class="row-1">
<td class="column-1">1</td><td class="column-2">#</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-2">
<td class="column-1">2</td><td class="column-2">+/+/+</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-3">
<td class="column-1">3</td><td class="column-2">+/+/+/+</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-4">
<td class="column-1">4</td><td class="column-2">+/b/c/#</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-5">
<td class="column-1">5</td><td class="column-2">+/b/c/d</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-6">
<td class="column-1">6</td><td class="column-2">a/#</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-7">
<td class="column-1">7</td><td class="column-2">a/+/+/d</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-8">
<td class="column-1">8</td><td class="column-2">a/+/c/d</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-9">
<td class="column-1">9</td><td class="column-2">a/b/#</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-10">
<td class="column-1">10</td><td class="column-2">a/b/c</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-11">
<td class="column-1">11</td><td class="column-2">a/b/c/#</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-12">
<td class="column-1">12</td><td class="column-2">a/b/c/d/#</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-13">
<td class="column-1">13</td><td class="column-2">a/b/c/d</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-14">
<td class="column-1">14</td><td class="column-2">b/+/c/d</td><td><input type="checkbox" class="form-check-input"></td></tr>
<tr class="row-15">
<td class="column-1">15</td><td class="column-2">a/b/c/d/+</td><td><input type="checkbox" class="form-check-input"></td></tr>
</tbody>
</table>
</div>







# Quality of Service

Messages can be sent with three different quality-of-service (QoS)
flags, which determine how much effort the broker and the clients spend
on sending them:

-   QoS=0 is also called *At most once*. The message can get lost, and
    there will be no attempts to resend it.

-   QoS=1 is also called *At least once*. This means that the message
    will be eventually received, but that several copies of the message
    may appear due to duplication. The receiver has to detect any such
    duplicates.

-   QoS=2 is also called *Exactly once*. This guarantees the delivery
    and avoids any duplication.

**You may ask:** *If QoS=2 is available, why would one ever use any of
the lower QoS levels?*

The answer is that the highest quality of service is also more expensive
with regards to transmission effort. To send a single QoS=2 message,
several messages on the underlying channel are necessary. Therefore, an
application should always choose the lowest QoS level it can work with.

Below you see the diagrams that show how many control packages are
involved to just send a single MQTT message, using QoS = 0.

---
type: figure
source: figures/iot/mqtt-qos-0.svg
---


For QoS=2, the protocol uses more control messages to transport a single MQTT message.
This shows that there are more control messages involved the higher the QoS level is. 
This also means that it is more expensive for the network to transport MQTT messages with higher QoS level, as it uses more resources.

---
type: figure
source: figures/iot/mqtt-qos-2.svg
---


# MQTT Clients in Python

There are libraries to use MQTT in a variety of programming languages.
For Python, there is a library for an MQTT client called *Paho*. As
usual, you install it via pip, using 

```bash
pip install paho-mqtt
```


The code for a client that subscribes to a topic looks like this:

```python
import paho.mqtt.client as mqtt

def on_connect(mqttc, obj, flags, rc):
    print("Connected: " + str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mqttc, obj, mid):
    print("Published: " + str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
mqttc.connect('localhost', 1883)
mqttc.loop_start()
```



The code above is in its structure similar to the one we used when
creating our own HTTP server. We connect to an MQTT broker using its address (or `localhost` when it’s on the same computer). 
The default port for MQTT is 1883.

After the client is created in `mqttc = mqtt.Client()`, we register a number of callback functions. 
These functions are called by the client whenever one of the events happens, that means, after we are connected, received a message, subscribed to a topic  or published a message. We can use them to trigger other behavior.


## MQTT Publisher Client

The following code is used to publish a message:

```python
mqttc.publish('a/b/c/d')
```

We can also specify which qos level we want, and add some payload (content) to the message:

```python
mqttc.publish('a/b/c/d', payload='Content of the message', qos=2)
```


# Debugging With MQTT.Fx

---
type: figure
source: figures/iot/mqtt-fx.png
---


MQTT.FX is a tool useful during development. Using MQTT.FX is
simple, but because we have now talked about brokers, clients,
publishers and subscribers, you may lose track and wonder what this
MQTT.FX does: Think of it as a debugger for MQTT, and you can use it
like Wireshark. Essentially, MQTT.FX is a MQTT client, and can as such connect to an
MQTT broker, subscribe to topics and send messages to topics.
You can subscribe to topics and hence listen to everything that happens in the system. You can also send messages manually for testing. 
Once the system is programmed, you don't need MQTT.FX anymore.

:aside: You can save some time during the lab if you [install MQTT.FX](https://mqttfx.jensd.de) on your own laptop already now.


---
type: figure
source: figures/iot/mqtt-fx-publish.png
---


## Publishing Messages

Imagine you created an MQTT client that runs a certain action when
it receives a message, but you are not done with the component that
should send the message. To test at least the component that should
receive the message, you can use MQTT.FX to publish a message with that
content to the topic, and the component under test will behave as if the
message was sent in the final system.

---
type: figure
source: figures/iot/mqtt-fx-subscribe.png
---


## Observing Communication

Because MQTT uses the publish-subscribe pattern, it can simply subscribe
to any topics that are interesting in your application and you can see
which messages are sent to these topics, without disturbing the
communication in the system. To achieve the same in HTTP, for instance,
you need a tool like Wireshark.


:hint: 
<div>
<table class="table table-sm">
<caption style=""></caption>
<thead>
<tr class="row-1">
<th></th><th>Subscription Topic</th><th>Receive a/b/c/d ?</th>
</tr>
</thead>
<tbody class="row-hover">
<tr class="row-1">
<td class="column-1">1</td><td class="column-2">#</td><td>Yes!</td></tr>
<tr class="row-2">
<td class="column-1">2</td><td class="column-2">+/+/+</td><td>No! We only subscribe to topics that include 3 levels.</td></tr>
<tr class="row-3">
<td class="column-1">3</td><td class="column-2">+/+/+/+</td><td>Yes!</td></tr>
<tr class="row-4">
<td class="column-1">4</td><td class="column-2">+/b/c/#</td><td>Yes!</td></tr>
<tr class="row-5">
<td class="column-1">5</td><td class="column-2">+/b/c/d</td><td>Yes!</td></tr>
<tr class="row-6">
<td class="column-1">6</td><td class="column-2">a/#</td><td>Yes!</td></tr>
<tr class="row-7">
<td class="column-1">7</td><td class="column-2">a/+/+/d</td><td>Yes!</td></tr>
<tr class="row-8">
<td class="column-1">8</td><td class="column-2">a/+/c/d</td><td>Yes!</td></tr>
<tr class="row-9">
<td class="column-1">9</td><td class="column-2">a/b/#</td><td>Yes!</td></tr>
<tr class="row-10">
<td class="column-1">10</td><td class="column-2">a/b/c</td><td>No! The publishing topic also includes a 'd', which does not match, even at the end.</td></tr>
<tr class="row-11">
<td class="column-1">11</td><td class="column-2">a/b/c/#</td><td>Yes!</td></tr>
<tr class="row-12">
<td class="column-1">12</td><td class="column-2">a/b/c/d/#</td><td>Yes!</td></tr>
<tr class="row-13">
<td class="column-1">13</td><td class="column-2">a/b/c/d</td><td>Yes!</td></tr>
<tr class="row-14">
<td class="column-1">14</td><td class="column-2">b/+/c/d</td><td>No! The first b of the subscription topic does not match the first a of the publishing topic.</td></tr>
<tr class="row-15">
<td class="column-1">15</td><td class="column-2">a/b/c/d/+</td><td>No! The last plus implies that there should be another level for the topic, after the d/.</td></tr>
</tbody>
</table>
</div>
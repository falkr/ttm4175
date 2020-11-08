## Question 1

:rat:Which message pattern describes the communication in MQTT best?

1. Publish-subscribe
2. Single-message
3. Request-response
4. Observer

## Question 2

:rat:To receive a message, a client has to:

1. connect to a server and make a request
2. subscribe to another client
3. connect to a broker, subscribe to a topic
4. connect to a broker, publish a message

## Question 3

:rat:Which statement is true?

1. Clients can subscribe to messages or publish topics.
2. Only the broker can publish messages.
3. Clients send responses directly to other clients.
4. Any client can publish messages.

## Question 4

:rat:Assume a message with a topic "T" and QoS=0 is sent to the broker. What happens next?

1. Nothing, because of Qos=0.
2. The broker forwards the message to all clients that subscribed to topic "T".
3. The broker forwards the message to at most one client that subscribed to topic "T".
4. The broker forwards the message to the client that most recently subscribed to topic "T".

## Question 5

:rat:The terms "at most once", "at least once", "exactly once" refer to...

1. ...the number of clients that will receive a message when several subscribe to the same topic.
2. ...how many clients are allowed to subscribe to a topic.
3. ...how often a client can send a message with the same payload.
4. ...to the delivery of the messages - how hard will the clients and broker try to deliver a message.

## Question 6

:rat:Which roles does the programm MQTT.Fx have?

1. It is a efficient MQTT server.
2. It is a combined MQTT and HTTP client.
3. It is a normal MQTT client, but with a general user interface.
4. It is just a powerful MQTT broker.

## Question 7

:rat:What do HTTP and MQTT in common?

1. Both protocols use client-server architecture.
2. Both protocols use topics.
3. Both protocols can run on top of TCP.
4. Both protocols are based on the request-response pattern.

## Question 8

:rat:Why is is a good idea to place the code for a subscription into the function that is called when the connection was established successfully?

1. We automatically subscribe to the topic again in case of a reconnection.
2. We subscribe immediately after a connect, without using a timeout.
3. It is the only way to subscribe to several topics at once.
4. The above statement is false, there is no such callback function.

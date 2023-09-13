# Networking III - Routing and DNS

At this point, you can already set up simple network configurations.
This week, we will continue exploring networking commands - in particular those for routing - and we will set up a basic [Domain Name System (DNS)](https://en.wikipedia.org/wiki/Domain_Name_System) and web server.


## Learning Goals

:goals: After this lab you will be able to

- Recognise the role of routing in networking
- Use `ip route` for managing routes
- Retrieve basic DNS information
- Deploy simple network services


# Routing

This video was previously included as optional material. However, now we want to focus more on routing so you should (re-)watch it.

---
type: youtube
video: AkxqkoxErRk
---


Additionally, **read from Section 4.1 up to and including _Control Plane: The Traditional Approach_, on pages 334 to 337.**


# DNS

Even though each website and server we connect to on the Internet has one or more IP addresses, we mostly remember them by their name (e.g., *ntnu.no* or *google.com*).
DNS enables this and much more!
To learn more, **read from Section 2.4 to 2.4.2, on pages 152 to 161.**


# Web Server

[This page](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server) was already an optional reading from last week.
This week however it's important that you fully understand its contents (you already meet the prerequisites indicated on top of the page but, if not, follow the provided links and read more about the basic principles).


# Optional Material

## Docker Compose

Earlier we saw how to build images and run containers from them, one by one.
Beyond that, there are ways to handle multiple images and containers, as well as the dependencies between them.

Docker Compose is a tool that allows us to manage several containers based on a simple configuration file ('docker-compose.yml').

The following video provides a nice explanation of what can be done and of the potential of using _compose_ in a complex environment.

---
type: youtube
video: Qw9zlE3t8Ko
---


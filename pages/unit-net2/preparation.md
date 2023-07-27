# Networking II - Ports, Layers, Client-Server Architecture, Web Servers

## Learning Goals

:goals: After this lab you will be able to

- Recognise the importance of _ports_ in networking
- Understand how computer networking is organized into protocol layers
- Get familiar with the popular client-server architecture for network-based services and see it in action in the context of a web server
- 

# Layers and Docker

The overall goal of this lab is to complement knowledge on IP, subnets with some routing notions.
This will be achieved using the same VMs as last week and default Linux tools.

Today we will also learn more about Docker. With Docker we will be able to simulate a "mini-cloud" inside our Ubuntu VM. This can be a bit overwhelming at first but we will look at it slowly.


# How do computers communicate (part 2)

## Protocol Layers

To better understand how computer networking is organised you should **read section 1.5.1 from page 75 to page 81** of the book.
Again, if you read the entire first chapter, this is already covered.

Optionally you can also read section 1.5.2 to get a better overview of how information is handled through different layers (encapsulated).


## Ports

We saw that IP address are useful for identifying a machine/server's location, or address.
We also mentioned that in each address we can have several services or applications, with their respective ports or doors to reach them.
To learn more about this you should **read sections 2.1.1 and 2.1.2, in pages 116 to 121.**


# Servers

In our next lab you will use the Raspberry Pi VM as a client and the Ubuntu VM (containers) and a server.
To better understand what a server is watch the following videos.

This first video is extremely simple but explains the most basic concept.

---
type: youtube
video: SwLdKeC8scE
---

This one goes into significantly more detail.
You need only to **watch the first 3 min\.** but the rest of the video is also interesting (and provides generally useful information).

---
type: youtube
video: UjCDWCeHCzY
---



# Optional Materials

## Web Servers

As an **optional reading** you can check this website about [webservers](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_web_server)

## Docker

You already worked with Virtual Machines, which can virtualise the hardware of an entire computer and run multiple operating systems.
However, there are other alternatives to fully virtualising an entire machine.
Docker is one of these alternatives, that uses containerisation for offering different virtualisation possibilities.
Check the video below for an introduction on Docker's approach.

---
type: youtube
video: TvnZTi_gaNc
---

To read more about the difference between Virtual Machines and Containers you can read this [blog post](https://www.backblaze.com/blog/vm-vs-containers/).


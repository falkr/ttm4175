# Networking II - Ports, Layers, Client-Server Architecture, Web Servers

The overall goal of this lab is to complement your knowledge on IP and subnets by bringing applications into the picture and allowing you to see the notions of ports and layers in a concrete example.
This will be achieved using the same GNS3-based environment as last week.

Additionally, we will learn more about Docker. Docker is the tool that is used to provision the invididual hosts in out GNS3 environment, but has many use cases beyond that.


## Learning Goals

:goals: After this lab, you will be able to

- Recognise the importance of _ports_ in networking
- Learn basic Docker principles
    - Images and containers
    - The _Dockerfile_
    - Basic commands for managing containers


# Lab Exercises

Please **read each exercise** entirely before starting to solve it.

Remember that you should deliver a report after the networking module is finished.
It should include the main commands and configurations necessary to complete each exercise.
Do not forget to take notes while solving the exercises so you do not have to repeat them.

These exercises should be completed in teams.


# Web Server, Ports, HTTP

## Initializing the Environment


We will use the same topology as last week, using one host as client and one as server. To get started, **close any running instances of GNS3 and launch it again**. You can load your project from last time or re-create the two-host topology according to [last week's instructions](/unit-net1/teamwork.html#launching-gns3-and-creating-a-basic-network).


:tip:
Since the underlying Docker images that are used for the hosts have been updated, it is necessary to restart GNS3 for the changes to take effect.


As last week, set compatible IP addresses on the interfaces of the two hosts, for instance `10.0.0.1/24` and `10.0.0.2/24`.
Before you continue, make sure that the two hosts can reach each other by using `ping`.



## Running a Web Server


1. As mentioned before, one host will take the role of the client and one that of the server. On the server (`ubuntu-host-2` with IP `10.0.0.2`), navigate to the `/var/www` folder and inspect its contents.


2. You can run a simple Python-based HTTP server in your current working directory by issuing the command `python3 -m http.server 80`. This will instruct python to run the `http.server` module with `80` as its first argument, indicating which port the HTTP server should listen to. 80 is the standard port number for HTTP. You can learn more about commonly used port numbers [here](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers).


:tip:
You can use the combination `Ctrl-C` to stop the server application and regain control of the console.



## Interacting with the Web Server


3. With the server application running, we can access the content it serves. Instead of using a browser, we can use command line tools like `curl` to connect to the server and download HTML pages or other files that are offered. 


4. From the host (`ubuntu-host-1` if you're following the same naming and addressing scheme), try `curl 10.0.0.2`. Observe the output and relate it to the content you saw in step 1. Investigate how you can download the file `example.html`.


5. On `ubuntu-host-2`, stop the server application, rename `example.html` to `index.html`, and restart the server application. Re-run the `curl` commands from the client from the previous step and discuss the differences in the output. What happens if you try requesting a page that does not exist?


## Capturing HTTP Traffic


6. Following the [instructions from last week](/unit-net1/teamwork.html#verifying-your-configuration), start a traffic capture on the link between the client and the server.


7. With Wireshark open, run the previous `curl` commands again and discuss the HTTP traffic that appears.

    - What kind of information is exchanged between client and server in the HTTP messages in each direction?
    - Click on an HTTP packet and check the detailed view in the lower half of the Wireshark window. Taking a look at these details, what can you tell about the protocol stack that is used here? Refer back to chapter 1.5.1 in the book and map the protocols you find to the different layers.
    - Compare how the traffic changes when you request `example.html` and `lipsum.txt`. What could be the reason?


---
type: hint
title: "Hint"
---
Compare the size of the two files and recall what we discussed about packets.



## Changing Ports


8. Going back to the server, stop the application and re-run it using a different port. For instance, `python3 -m http.server 8000`. How does this change the output at the client trying to `curl`? Find out how to point `curl` to a specific port, e.g., by consulting its [manual](https://curl.se/docs/manual.html).







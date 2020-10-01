# Layers and Docker 

The overall goal of this lab\. is to complement knowledge on IP, subnets with some routing notions.
This will be achieved using the same VMs as last week and default Linux tools.

Today we will also learn more about Docker. With Docker we will be able to simulate a "mini-cloud" inside our Ubuntu VM. This can be a bit overwhelming at first but we will look at it slowly.

:aside:
**Note:** Running Docker inside a VM may seem strange to some of you but it allows us to keep a clean and consistent environment for all of us. There's nothing wrong with it and, for the sake of curiosity, did you know that you can run Docker inside Docker?

<p><a href="figures/net/docker-ception.jpg"><img src="figures/net/docker-ception.jpg" width="100px"></a>



## Learning Goals

:goals: After this lab you will be able to:

- Recognise the importance of _ports_ in networking
- Learn basic Docker principles:
    - Images and containers
    - The _Dockerfile_
    - Basic commands for managing containers



# Lab\. Exercises

Please **read each exercise** entirely before starting to solve it.

Remember you should deliver a report after the networking module is finished.
It should include the main commands and configurations necessary to complete each exercise.
Do not forget to take notes while solving the exercises so you do not have to repeat them.

These exercises should be completed in teams.


## Preparation

:steps:
1. Make sure there's connectivity between both VMs (you should have configured static IP address in the previous lab.).
2. Test if your Ubuntu VM has Internet connectivity.
3. Test if your RPi VM has Internet connectivity.
4. Make sure you've got enough free disk space for your VM (at least 3GB).


## Experimenting with routes

Today we won't see all the network layers in action but we will look into layer-3 routing.
Later in this lab\. we will move to the application layer, which is higher in the networking stack.

Now, **on your RPi VM** try the following:

:steps:
1. Check the current routes associated to 'eth1'
2. Remove the existing route with `ip route del <ip/mask> dev eth1`.
3. Check for changes in connectivity between the two VMs with the `ping` command first from the RPi and afterwards from Ubuntu. Is there any difference?
4. Install the program "tcpdump" with the command `sudo apt install tcpdump` (when asked, type Y or yes to install)

:tip:
`tcpdump` dumps all the received/sent network traffic (i.e. prints all the traffic)


:steps:
5. Now, on your RPi run the command `sudo tcpdump -i eth1` and try to `ping` from the Ubuntu VM. Register what happens.
6. **Repeat step 4** but this time run `tcpdump` **on Ubuntu** and for the correct interface connected to the internal network. Is there a difference? If so, why?
7. **On your RPi**, add a new route with the command `ip route add` with the smallest subnet size possible (don't forget to include this in your **report**).
8. Make sure you have re-established the connectivity between the two VMs.


---
type: hint
title: Hint on tcpdump
---
In this exercise it's important to remember/understand that a `ping` consists of two messages.
One on the way out, and another returning one.

In our exercise the Ubuntu VM has a route (a path) to reach our RPi, which means that its messages will be sent to their destination.
On the other hand, the RPi VM **does not** have a route for reaching Ubuntu (even if the "cable is connected").
This should be visible when using `tcpdump`, which will get packets on the RPi but not on Ubuntu.




## Docker

### Introduction

We will start with a few basic steps, if you have any issues please ask for help!
It's important that you understand well these steps before moving forward.

**---> On your Ubuntu VM**

:steps:
1. On your Ubuntu VM find out what kind of operating system you're emulating.
2. In Docker's hub <https://hub.docker.com/> search for the same operating system.
3. You should have found at least one *Docker Official Image*, which is important to take into account! Don't use images you don't trust.
4. Now enter the following in your terminal:

```bash
docker pull ubuntu
``` 

:aside:
The `pull` command retrieves the image from Docker Hub into your local repository.
This allows you to use the image to create containers multiple times, without having to download it again (unless it needs to be updated).


:warning:
At this stage, if you get an _Error response from daemon_ edit your network configurations in "/etc/netplan/01-network-manager-all.yaml" to include _nameservers_ below, followed by the command `sudo netplan apply` to apply the changes.
```yaml
enp0s3:
    dhcp4: yes
    nameservers:
        addresses: [8.8.4.4,8.8.8.8]
...
```


:steps:
5. You can see all locally available Docker images by typing:

```bash
docker images
``` 

:steps:
6. Now let's build and run a container from the Ubuntu image using:

```bash 
docker run -dit --name my-ubuntu-container ubuntu
``` 
:aside:
The `run` command will build an instance of the Ubuntu image.
This instance is what we call a container.
We can build several containers that originate from the same image.
This is similar to the VM Images that we used earlier, that can be used to build several different VMs, but uses a different technology (for a better explanation check the video on the [optional materials section](prep-networking-2-2020.html#optional-materials)).

If the container is created correctly, you should see its container identifier (container ID), which we will use to manage it.


:steps:
7. Using the generated ID, "enter" the new Ubuntu container using the following command, which will run a shell inside it:

```bash
docker exec -it <containerID> bash
``` 

:tip:
It's enough to use only part of the Container ID, as long as it is unique.


:steps:
8. Compare the version of your container's Ubuntu with the one from your VM using the command below inside the container and inside the VM:

```bash
cat /etc/os-release
``` 

:tip:
The goal of this last step is to verify the power of using containers.
The Docker image we pulled was used as the basis for our container and, as we shall see later, it is possible to run different Linux distributions in our containers, even if the main host is Ubuntu.


:steps:
9. To exit your container you can just enter "exit", type `Ctrl+d` or type `Ctrl+p Ctrl+q` (the latter detaches from a container even if wasn't started in _detach mode_).
10. To list all running containers you can use the command `docker ps`. Try it.
11. You can stop running containers with `docker stop <containerID/name>`. Stop your Ubuntu container.


:tip
After stopping the container you will no longer be able to "enter" it.
If you try the _exec_ command again it will fail.


:steps:
12. Now, list all running containers again to see the difference.
13. What happens if you try `docker ps -a`?
14. To remove a container you can use the command `docker rm <containerID/name>`.
15. Try again the command `docker ps -a`. Did anything change?

:tip:
To learn more about Docker commands, apart from using `man` and `--help` you can also check our [List of Commands](commands.html#docker-commands) and [this support document](material/ttm4200-lab1-support-document-2020.pdf), created by a couple of your KOMTEK colleagues for TTM4200 (next Spring!).



### More on Docker

Now we'll use Docker to setup a Web Server in our VM without having to change it.
This is very useful in many contexts, even for you throughout your degree.
For example, if you need to use a specific software for a given course, instead of installing on your own machine, you can just create a container with all the necessary software and run it when needed!

:aside:
For making things simpler, in this part of the lab\. we need to run the Ubuntu VM with graphics support (_Normal start_).
It can be done without but it needs some extra (non-included) steps.


Back to the lab\.!

Instead of pulling a generic Docker image, we are going to create our own Docker image, defined using a 'Dockerfile'.
This file contains a set of instructions, necessary to create a Docker image.
To do so just follow these steps:

:steps:
1. Download [this zip file](material/lab2-docker.zip) with a basic container configuration.
2. `unzip` the downloaded file and navigate to the folder './lab2/webserver/'.
3. Inside this folder you will fine a simple 'Dockerfile' with comments created by two KOMTEK colleagues. Read through the file and comments to see how it works.
4. Now you can build your own image based on this 'Dockerfile' with the command:

```bash 
docker build -t webserver .
``` 

:steps:
5. List all available Docker images to see the new image. How many new images do you see? Why?
6. Create a container based on the image you just built and register its ID (you can also retrieve it later).
7. Enter your new container and find its IP address.
8. Open a browser inside your Ubuntu VM and enter the IP address of your container. What did you see? Take a screenshot and include it in your report.
9. Stop and remove all running containers (can you find a way of doing it with a single command? Search online!).

:tip:
If you have issues with your browser ask for help from a TA.


---
type: hint
title: Hint about managing containers
---
To create a container you want to use the command `docker run` with the necessary/correct options.

To find container IDs you want to use the command `docker ps` (`-a` optional).




# Optional Exercises

## Two servers, same IP address?

*You can run this exercise without graphics support on your Ubuntu VM.*

**Intro:** A Web Server can be run in the same machine to support multiple websites.
This is typically done by analysing the website's name (DNS) and replying with the correct page.
However, more than one Web Server in the same machine means we would have to use port 80 or 443 more than once, which we can't!
In the upcoming tasks you will see how we can get around this limitation.

:aside:
By convention Web Server bind port 80 for HTTP and port 443 for HTTPS.
These default ports are used in many networking services, for saving us time in having to specify a port for each standard service.
For example, SSH uses port 22 by default (that's why we used it when we set port forwarding, remember?).


:steps:
1. Inside the unzipped folder navigate to './lab2/webserver-1/'.
2. What is the main difference from the 'Dockerfile' in this folder compared to the one used earlier (in the folder 'webserver')? Discuss this in your report.
3. Build an image based on the included 'Dockerfile', name this image "webserver-1".
4. Repeat step 1 and 2 for 'webserver-2' and name the image accordingly.
5. Run the commands below and look at them carefully. Note the `-p` option. What does it do? 

```bash
docker run -d --name serverNr1 -p 8080:80 webserver-1
docker run -d --name serverNr2 -p 8081:80 webserver-2
``` 

:steps:
6. On your RPi VM (_Normal start_), open the web browser and type the IP address of your Ubuntu VM followed by ":8080" to specify the desired port and enter it (e.g. 10.0.20.2:8080). What did you see?
7. Repeat the previous step using port 8081 instead. What's the difference?
8. In your report make an illustration of what you think happened, including the RPi and Ubuntu VM, the link between them and the containers, as well as some arrows to represent the webpage request (e.g. with IP and port number as labels). You can use the figure below as inspiration.
9. Stop and remove all the containers.
10. Remove all Docker images.

---
type: figure
source: figures/net/lab3-topo.png
caption: Simple illustration of the setup we will have in lab 3. Can be used **as inspiration** to illustrate lab 2.
---








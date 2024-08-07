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


We will use the same topology as last week, using one host as client and one as server. To get started, **close any running instances of GNS3 and launch it again**. You can load your project from last time or re-create the two-host topology according to [last week's instructions](../unit-net1/teamwork.html#launching-gns3-and-creating-a-basic-network).


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


6. Following the [instructions from last week](../unit-net1/teamwork.html#verifying-your-configuration), start a traffic capture on the link between the client and the server.


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



# Docker


For this second part, you can quit GNS3 and open a terminal directly on your VM. The CLI prompt should say `netlab@netlab-linux:~$ `.


## Basics


In Docker, we distinguish between *images* and *containers* (also called *instances*). Images are the pre-built templates or snapshots that package all the software that is required for the intended use case. The use case can be a fresh install of a specific Linux distribution, a pre-installed and pre-configured service (web server, mail server, database, ..), or more. For this, an image can include code and configuration files, runtimes and libraries, as well as other dependencies. Based on such an image, we can launch one or multiple running containers that execute the environment defined in the image.


1. To check which images are available on your machine, you can run `docker images`. How many images are listed in your case?

2. You can create an instance based on the `ubuntu` image by running 
```bash
docker run -dit --name my-ubuntu-container ubuntu
```

The output should give you a long ID which is used to uniquely identify that specific instance. For easier reference, we also provided a more memorable name, `my-ubuntu-container`.

:tip:
You can learn more about the options of docker run in the [documentation](https://docs.docker.com/engine/reference/run/). For now, it is enough to know that `docker run -dit` instantiates a container in the background, and allows us to attach to its console later on.


3. You can confirm that the instance has been created using `docker ps` (process status). The output contains the ID, base image name, and other high-level information about your running container instances. Following step 2, you can also launch additional instances from the same image and confirm their presence using `docker ps`.

:tip:
If you create multiple containers and explicitly provide a name, make sure that the name is unique to avoid errors.


4. With the containers running, you can attach to them via 
```bash
docker exec -it <containerID> bash
```
Your prompt should change from `netlab@netlab-linux:~$ ` to `root@fa00f8e10813:/# `, indicating that you are now logged in as root on the container with the respective ID. Create some files or folders inside the container.
 
:tip:
In this case, the `containerID` can be either the ID from the outputs in the previous step (the first few characters are enough as long as they are enough to uniquely identify your container), or the name you chose when running the container.


5. Try running `cat /etc/os-release` inside your container, then `exit` back to your netlab VM and run the same command to compare the operating system versions. What can you observe?

---
type: hint
title: "Hint"
---
This step illustrates some of the power of using containers.
The Docker image we used as the basis for our container uses a different version of the same operating system and, as we shall see later, it is even possible to run different Linux distributions in our containers, regardless of the main host's distribution.


6. To clean up, you can stop and remove containers using `docker stop <containerID>` followed by `docker rm <containerID>`.

7. Re-create one of the containers according to step 2. What happened to the files/folders you created in step 4? Discuss how this relates to the concepts of images and containers.


## Building Our Own Image


We can also define our own image to create containers which run our desired software. As an example, we will create the web server from the fist part of today's lab. To this end, we will use the `ubuntu` image as a starting point and extend it to fit our needs. The Docker way of doing this involves a *Dockerfile* which you can think of as a recipe for building images.


1. Download an exemplary Dockerfile project with the command below. `wget` is similar to the `curl` command you used earlier, but in its default behavior downloads the file rather than displaying its content.

```bash
wget https://folk.ntnu.no/stanisll/2023/ttm4175/ttm4175-webserver.zip
```

2. Extract the zip archive using `unzip ttm4175-webserver.zip` and navigate into the newly created `ttm4175-webserver` folder.

3. Read through the commented `Dockerfile` and try to understand what it does. You do not need to execute the commands in that file.

:tip:
You can refer to the [Dockerfile manual](https://docs.docker.com/engine/reference/builder/) if you want to learn more about the different Dockerfile-specific instructions like `FROM`, `RUN`, and `EXPOSE`. For more information about the apt software package manager, you can use `man apt`.


4. Extend the Dockerfile to not only copy the `example.html` file, but also `lipsum.txt`. You can use the `nano` editor for this.

5. To build an image based on the Dockerfile, execute `docker build -t ttm4175-webserver .` (don't forget the dot). This will instruct docker to scan the current directory (`.`) for a Dockerfile and build an image called `ttm4175-webserver`.

6. Confirm that the build was successful by checking `docker images`. Then launch an instance of the `ttm4175-webserver` and attach to it (cf. steps 2 and 4 in the Docker basics part).

7. Within the container, 
    - Find out its IP address using tools you already know and note it in your report.
    - Navigate to the `/var/www` directory and confirm that the files you specified in the `COPY` part of the Dockerfile are present.
    - As in the web server exercise, launch a web server on port 80.
    - Open a web browser in your VM (not on your laptop) and navigate to the IP address of the container. What do you see? Take a screenshot and include it in your report.

8. Stop and remove all running containers. Can you find a way of doing it with a single command? Search online!

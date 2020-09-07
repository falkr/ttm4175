# Web servers and DNS

The overall goal of this lab\. is to complement knowledge on IP and subnets with some routing notions for setting up our own DNS and Web servers.
This will be achieved using the same VMs as last week and default Linux tools.


## Learning Goals

:goals: After this lab you will be able to:

- Recognise the role of routing in networking
- Use `ip route` for managing routes
- Retrieve basic DNS information
- Deploy simple network services


# Lab\. Exercises

Please **read each exercise** entirely before starting to solve it.

Remember you should deliver a report after the networking module is finished.
It should include the main commands and configurations necessary to complete each exercise.
Do not forget to take notes while solving the exercises so you do not have to repeat them.

These exercises should be completed in teams.


## Preparation

:steps:
1. Make sure there's connectivity between both VMs (you should have configured static IP address in the previous labs.).
2. Test if your Ubuntu VM has Internet connectivity.
3. Make sure you've got enough free disk space for your VM (at least 3GB).


**Note:** If you have problems with lack of memory/RAM in your computer consider this:

* You can complete this entire lab\. without the RPi VM (except for the optional part);
* You can run the Ubuntu VM in headless mode and connect to it via `ssh`;
* Instead of retrieving web pages with a "normal browser" you can use the command `wget` (or a text-based browser such as Lynx).


# A simple network with services

---
type: figure
source: figures/net/lab3-topo.png
caption: Network to be created with docker-compose.
---

**--> In your Ubuntu VM**

:steps:
1. Download [this zip file](material/lab3-compose.zip) with the necessary container configuration files.
2. `unzip` the downloaded file and inside the 'lab3' folder edit the 'docker-compose.yml' file.
3. Read through the file and see how we configured 3 containers and their networks, matching the figure above.
4. In the webserver's configuration section edit the IP address to match the topology above (line 51, replace the text "-----Fyll inn her ------" with the correct IP address). Save and exit the file.
5. Now you can start your topology with the command below. Afterwards list all running containers (discuss what happened in your report).

```bash
docker-compose up -d --build
``` 

:tip:
The first time you run `docker-compose` it will take a few minutes to build the images (approx. 5 min. or less).
Use that time to carefully read the next steps.



## Configuring simple routing

In this part of the lab\. your objective is to guarantee you can route packets from your host to the containers.
Notice that we have a router in our topology that connects two different subnets.
We will need to configure this router container ('router0') so that packets are correctly forwarded.

**--> In your Ubuntu VM**

:steps:
1. First, we should check our current routing table in the host machine (use: `ip route list `).
2. You should see that the host has direct routes to the subnets '10.241.1.0/29' and '10.168.1.0/29', via the devices "br-\*". Include this in your report (a screenshot with a highlight is enough).
3. Since we don't want the host to directly access all the containers --- it should go via 'router0' --- run the following command:
```bash
sudo ip route del 10.241.1.0/29
```

:steps:
4. Verify that you have connectivity with '10.168.1.2' and not with '10.241.1.2'. Briefly explain why in your report.
5. Now we need to add a new route such that traffic for the network '10.20.1.0/29' is forwarded via 'router0' (i.e. via '10.168.1.2').

---
type: hint
title: Adding routes
---
Remember the command `ip route add`.


:steps:
6. Now verify that packet forwarding is enabled (i.e. "= 1") with the command:
```bash
sysctl net.ipv4.conf.all.forwarding
```

:steps:
6. From your host machine make sure you can `ping` the web server using its address and include a screenshot on your report.


## Using our DNS server (container)

As you can probably guess, our DNS container contains a running DNS server which will support our proposed network.
Follow the steps below but don't forget to explore the provided configurations to learn some more.

**--> In your Ubuntu VM**

:steps:
1. Open a web browser and try to retrieve the web site 'www.ttm4175.com'. What happens and why?
2. Edit the file '/etc/resolv.conf' and change the "nameserver" to '10.241.1.2' (or add a new entry above). This will tell the system to make DNS requests to this address first, which corresponds to our DNS container.
3. Repeat step 1. What happens and why?
4. Find out what other domain names your DNS container resolves and include them, and their corresponding addresses, in your report (e.g. 'mail.ttm4175.com' resolves to '10.241.1.3').


---
type: hint
title: Finding DNS server configurations
---
If you explore the Docker configuration of the DNS container (in the 'dnsserver/config_files' folder) you will find all the details you need.
You can also check inside the actual container you built, where the configuration files have been placed.


:tip:
To make nameserver changes permanent use the _netplan_ configuration like you did last week.



## Exploring our Web server (container)

**--> In your Ubuntu VM**

:steps:
1. Go into your web server container ('webserver'). How did you do it?
2. Navigate to '/etc/nginx/sites-available' and open the file 'default'.
3. In this file find the *root* directory where the web server pages are stored, namely the 'index.html' file, and include it in your report.
4. In your host machine, open the web browser and visit the site 'www.ttm4175.com'.
5. Now, back in your web server container edit the file 'index.html' (be creative!!) and save it when you finish.
6. Return to your web browser, refresh the page (it should look different), take a screenshot and include it in your report.

---
type: hint
title: Working inside your containers
---
Remember that you can go inside your running containers with the command `docker exec -it <name> /bin/bash`.
Alternatively, you can also use `ssh` to enter your container.

And don't forget the [useful commands page](./commands.html).



## Final task

In your report describe what happens in the network when you open the page 'www.ttm4175.com'.
You can just explain, step by step, the requests and answers from the browser to the servers and back.
This should include the IP addresses of each server (don't forget DNS).

If you want, you can also include screenshots (e.g. `tcpdump`) and you can also start/stop containers by hand to see how they affect the overall process (e.g. stop the DNS server).

Finally, you can stop all the containers and remove the networks with the command:
```bash
docker-compose down
```

:tip:
If you want to restart your network but haven't changed the setup you can simply run `docker-compose up -d`, without the `--build` flag, and it will be much faster than the first time!



# Optional Exercises

## Routing from the RPi to the Docker services

**--> In your RPi VM**

:steps:
1. Can you `ping` the container 'router0'? Why or why not?
2. How does your routing table look like? Do you need to add or remove any entry?
3. **After having IP connectivity**, attempt to open or `ping` the web server using the hostname 'www.ttm4175.com'. What happens? Why? How can you fix it?



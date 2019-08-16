# Day 3: Exploring IP, SSH/SCP and HTML

Today we will explore the world of HTML, the marking language used to build every website on the World Wide Web.
In order to this we will also briefly look into IP addresses and the Secure Shell (SSH).

### Learning Goals

:goals:
- Become familiar with HTML
- Understand IP addressing
- Learn how to use SSH and SCP

### New Linux Commands

- [passwd](commands.html#passwd) --- to change passwords.
- [ls](commands.html#ls) --- to list files and folders.
- [ip](ip.html#ip) --- show / manipulate routing, network devices, interfaces and tunnels.
- [ssh](ssh.html#ssh) --- remote login program.
- [scp](scp.html#scp) --- remote file copy program.
- [ping](ping.html#ping) --- send ICMP *ECHO_REQUEST* to network hosts.
- [curl](curl.html#curl) --- transfer a URL.
- [aplay](aplay.html#aplay) --- command-line sound player for ALSA.


# Finding your IP address and checking for connectivity

In a terminal of your Raspberry Pi you can easily find its IP address by using the command `ip`.
Try and type the following command:

```bash
ip address
```

This command shows you all the existing IP addresses associated with your Raspberry PI.
These addresses are fundamental for connecting computers and other devices to each other and the Internet.
Each network card (e.g. wireless card) is called an _interface_ and it may have one or more IP addresses.
A typical IP(v4) address at NTNU looks something like `129.241.200.112/24.`

Write down the address and mask of the interface `eth0`.


# Testing Internet Connectivity

By default, the Linux distribution we are using has a running service, or daemon, that automatically configures network interfaces whenever a new link is found.
This service is called `dhcpcd` and runs a networking protocol called DHCP.
You will learn more about this later in the course.

DHCP is also used to automatically configure the routes that are used to reach the Internet.
You can find any route installed in your Raspberry Pi by typing the following command:

```bash
ip route
```

You should see a *default route* via the IP address 129.241.200.1, which corresponds to a router at NTNU responsible for forwarding our packets to and from the Internet.

To see if we can send something back and forth between two computers, we can use the command `ping`. 
It does exactly what it sounds like... It sends a "ping" message to the other computer, which then answers. 

---
type: youtube
video: jr0JaXfKj68
---

Try pinging that router with the command `ping`:

```bash
ping 129.241.200.1
```

You can also use the same command to `ping` other online machines such as the server hosting the website from the European Space Agency at *www.esa.int*.
Can you see any significant difference from the previous `ping` command?

```bash
ping www.esa.int
```


# Remote Access to a Computer

It is possible to remotely access a Linux system, and manage it, using different tools.
One of the most popular ones, due to its simplicity, security and lightweight is the Secure Shell, typically referred to as `ssh`.

This service needs to be enabled **in your Raspberry Pi** with the following commands:

```bash
sudo systemctl enable ssh
sudo systemctl start ssh
```

Now, **from your desktop** you can access your Raspberry Pi using the IP address you found earlier and the command `ssh` as such:

```bash
ssh ip@<your_ip_address>
```

**Note:** a warning message should appear the first time you connect since the certificates being used have never been exchanged before.
It is okay to say "yes" and then type in your password.

Now that you are remotely controlling your Raspberry IP issue the following command to download a simple *wave* file:

```bash
curl https://ttm4175.iik.ntnu.no/onesmall.wav -O
```

And play it!

```bash
aplay onesmall.wav
```

# Nano/ Vim (Or Leafpad)

Here it will be described what what Vim (Or Leafpad) is, and how to use it. 


# Setting things up

Here it will be described where they can find and HTML template file which they will edit to see their work in action. They will also learn about `xdg-open` to open their *.html* files.


# Making a website

Here it will be purposed things to put in their HTML file (lists, headers, boxes, buttons etc). They can play around with this. Opening their file in a browser will hopefully give them and understanding of what HTML is.




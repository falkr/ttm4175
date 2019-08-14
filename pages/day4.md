# Day 4: Apache Web Server

These last two days we are going to create our own web site and set up a web server on the Raspberry Pi. The web server we will use is called _Apache_.

### Learning Goals for Today

:goals:
- Install a new program (Apache) on Linux
- Get an overview of how a webserver can be used to host your own websites.

### New Linux Commands

- [sudo](commands.html#sudo) --- execute a program as super user.
- [apt](commands.html#apt) --- install new programs.
- [systemctl](commands.html#systemctl) --- control system services.


### Apache and Webserver 

:factbox: *Web Server:* A web server is like a restaurant host. When you arrive in a restaurant, the host greets you, checks your booking information and takes you to your table. Similar to the restaurant host, the web server checks for the web page you have requested and fetches it for your viewing pleasure. However, A web server is not just your host but also your server. Once it has found the web page you requested, it also serves you the web page.

:factbox: *Apache:* Apache is the most widely used web server software. Developed and maintained by Apache Software Foundation, Apache is an open source software available for free. It runs on 67% of all webservers in the world. It is fast, reliable, and secure. It can be highly customized to meet the needs of many different environments by using extensions and modules.
 
 To install Apache and start our own server, there are a few steps we need to go through.a

# Step 1: Installing Apache

Our operating system on the Raspberry Pi does not come with Apache built into it, so we will have to download and install Apache. 
The `apt` packet manager makes this easy for us --- it's like an app store, but for Linux.

First, we need to update the list of available software:

```bash
sudo apt update
```

Then we install Apache:

```bash
sudo apt install apache2
```


# Step 2: Starting Apache

Now that we have Apache installed, we need to start the *service*, i.e the program.

:factobox: *What is a service?* A service is just another word for _application_ or program. However, a service is a program that should run all the time. 

`systemctl` is a piece of software that can be used to start, stop and check the current status of any service running on a Linux system.

Let's start the service:

```bash
systemctl start apache2
```

List of useful `systemctl` commands:

- `systemctl status apache2` --- *checks the current status of apache2*
- `systemctl start apache2` --- *starts the service*
- `systemctl stop apache2` --- *stops the service*
- `systemctl restart apache2` --- *restarts the service*


# Step 3: Testing the Server

Apache is set up and is running. This means we go ahead and check if the service works and edit our home page. 

First, we would like to check wether our Apache server is working as expected. The Apache server runs on port 80 by default, so in order to check whether the service is running, we have to check this port specifically.

**Check that Apache works as expected:**
1. Find your IP-address
2. Type the IP-address in your browser, and specify port number 80. i.e *http://192.168.10.19:80*
3. If the Apache test-page pops up, the server is running as expected. (link to apache test-page)
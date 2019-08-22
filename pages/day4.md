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


# Being Super User

Some commands or programs require special permissions to run, usually because they affect more than one user or handle critical resources, or are related to the security of the system.
As the user `pi`, you _have_ all these permissions, but to protect you from doing something stupid, you need to prove to the system that you are allowed to execute these specific commands or programs. For that, the command `sudo` exists, which stands for _"**s**uper **u**ser **do**"_. SOmtimes you just add this in front of another command that you want to execute with special rights. 

```bash
sudo <important command...>
```

Think of it as when your parents told you to say "Please!"



# Apache and Webserver 

:factbox: *Web Server:* A web server is like a restaurant host. When you arrive in a restaurant, the host greets you, checks your booking information and takes you to your table. Similar to the restaurant host, the web server checks for the web page you have requested and fetches it for your viewing pleasure. However, A web server is not just your host but also your server. Once it has found the web page you requested, it also serves you the web page.

:factbox: *Apache:* Apache is the most widely used web server software. Developed and maintained by Apache Software Foundation, Apache is an open source software available for free. It runs on 67% of all webservers in the world. It is fast, reliable, and secure. It can be highly customized to meet the needs of many different environments by using extensions and modules.
 


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


# Step 4: Our own Website

It is now time to create our own website.

## Editing the content of the website

The default folder from where Apache gets the content for the website is `/var/www/html`. By default, only one file resides here, the Apache test page. By default, Apache looks for a file named `index.html`, which currently only stores the content of the testpage. 

We can go ahead and remove this file:
1. `~$ cd /var/www/html` *Navigates to the folder*
2. `~$ rm index.html` *Removes the file*

If you go back to your website and hit refresh, you will see that instead of loading the test page, an error message will pop up. Since we deleted the file, Apache has nothing to give us on our website. 

## Creating a new site

We now want to create our new website.

First, create the file `index.html`:
 
```bash
touch index.html
```

Then, edit the file with leafpad:

```bash
leafpad index.html
```

Write HTML code here to personalize your web page. Start with the template below, or find a template online.

```html
<html>
    <head>
        <title></title>
    </head>
    <body>
        <h1> This my webpage </h1>
        <h3>Quote of the day:</h3>
        <p><i>Never trust a computer you can't throw out the window</i></p>
        <p><i>- Steve Wozniak</i></p>
    </body>
</html>
```

:aside: <i class="fas fa-language"></i> _Template_ betyr _mal_ på norsk. 



## Editing Your Website 

You can now edit the website as you want. Try to go to each others webpages by typing in their IP-address and port in the URL on the same format as earlier.


# Final Steps

### Learning Goals

In your double-team, reflect about what you learned today. Write a few sentences that capture (in your own words) what you learned and why it can be useful. Share these few sentences with everyone in the double-team. (You should use this text in the individual reflection below.)

:aside: <img src="figures/doubleteam.png" width="30"/>


### Individual Reflection

Fill out the <a href="https://forms.office.com/Pages/ResponsePage.aspx?id=cgahCS-CZ0SluluzdZZ8BSxiepoCd7lKk70IThBWqdJUQzJJUEVaQlBBMlFaSFBaTllITkcxRDEzNi4u" class="arrow">individual reflection survey</a>.


### Cleaning Up

:todo:
- Put all hardware back into the box.
- Store the box in one of the lockers in the lab, using the combination lock.
- Connect all parts of the PC back to it (keyboard, mouse, monitor).
- Take out any trash. (Even if its not yours... thank you!)
- Put the chairs back to the table.

### Individual Exercises

We recommend that you take some time to consider if there are any parts of this unit that you want to repeat individually, at your own pace. If you decide to do so, you have several options:

- You have access to the hardware box at all times from the lockers. Just make sure everyone in your team knows where the box is, and put it back into the locker.
- Install a Raspberry Pi Image on a Virtual Box in your PC. With this, you always have a Raspberry Pi with you.
- Some of the Linux-related exercises also work on the Linux-PCs in the lab.
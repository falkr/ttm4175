# Day 4 & 5: Apache

These last two days we are going to createe our own web site and set up a web server on the Raspberry Pi. The web server we will use is called Apache.

## Learning Goals

:goals:
- Become even more familiar with the Raspberry Pi
- get an overview of how a webserver can be used to host your own websites.

### Apache and webserver 

Apache is the most widely used web server software. Developed and maintained by Apache Software Foundation, Apache is an open source software available for free. It runs on 67% of all webservers in the world. It is fast, reliable, and secure. It can be highly customized to meet the needs of many different environments by using extensions and modules.

 So what is a web server? A web server is like a restaurant host. When you arrive in a restaurant, the host greets you, checks your booking information and takes you to your table. Similar to the restaurant host, the web server checks for the web page you have requested and fetches it for your viewing pleasure. However, A web server is not just your host but also your server. Once it has found the web page you requested, it also serves you the web page.
 
 To install Apache and start our own server, there are a few steps we need to go through.a

# Step 1: Installing Apache

Our operating system on the Raspberry Pi does not come with Apache built into it, so we will have to download and install Apache. The `apt` packet manager makes this easy for us.

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

`systemctl` is a piece of software that can be used to start, stop and check the current status of any service running on a Linux system.

Let's start the service:

```bash
systemctl start apache2
```

List of useful `systemctl` commands:

- `~$ systemctl status apache2` --- *checks the current status of apache2*
- `~$ systemctl start apache2` --- *starts the service*
- `~$ systemctl stop apache2` --- *stops the service*
- `~$ systemctl restart apache2` --- *restarts the service*


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
2. `~$ rm index.html`*Removes the file*

If you go back to your website and hit refresh, you will see that instead of loading the test page, an error message will pop up. Since we deleted the file, Apache has nothing to give us on our website. 

## Creating a new site

We now want to create our new website.

First, create the file `index.html`:
 
```bash
touch index.html
```

Then, edit the file with leafpad: (which editor?)

```bash
leafpad index.html
```

Write HTML code here to personalize your web page. Start with the template below, or find a template online.


### What is HTML?
Firstly, HTML is short for "HyperText Markup Language". That may sound scary, but it simply means it is a language for describing web-pages using ordinary text. HTML is not a complex programming language.

Every web page is actually a HTML file. Each HTML file is just a plain-text file, but with a .html file extension instead of .txt, and is made up of many HTML tags as well as the content for a web page.
A web site will often contain many html files that link to each other. You can edit HTML files with your favourite editor.
### HTML Template


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



# Final steps

 You can now edit the website as you want. Try to go to each others webpages by typing in their IP-address and port in the URL on the same format as earlier.


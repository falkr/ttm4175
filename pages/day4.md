# Day 4 & 5: Apache

To set up an apache web server there are a few stepts that we need to go through.

# Learning goals

- The goal of this lab is to become even more familiar with the Raspberry Pi and get an overview how how a webserver can be used to host your own websites.

### Step 1: Installing Apache

Our operating system on the Raspberry Pi does not come with Apache built into it, so we will have to download and install Apache. The `apt` packet manager makes this easy for us.

`~$ sudo apt update` *Updates our repository (catalog) of software availale*
`~$ sudo apt install apache2` *Installs Apache*

### Step 2: Starting Apache
Now that we have Apache installed, we need to start the *service*, i.e the program.

`systemctl` is a piece of software that can be used to start, stop and check the current status of any service running on a Linux system.

`~$ systemctl start apache2` *Starts the service*


List of useful `systemctl` commands:
- `~$ systemctl status apache2` *Checks the current status of apache2*
- `~$ systemctl start apache2` *Starts the service*
- `~$ systemctl stop apache2` *Stops the service*
- `~$ systemctl restart apache2` *Restarts the service*

### Step 3: Test you server, and start coding

Apache is set up and is running. This means we go ahead and check if the service works and edit our home page. 

First, we would like to check wheter our Apache server is working as expected: The Apache server runs on port 80 by default, so in order to check wheter the service is running, we have to check this port specifically.

**Check that Apache works as expected:**
1. Find your IP-address
2. Type the IP-address in your browser, and specify port number 80. i.e *http://192.168.10.19:80*
3. If the Apache test-page pops up, the server is running as expected. (link to apache test-page)

It is now time to create our own site.

**Editing the content of the website:**

The default folder from where Apache gets the content for the website is `/var/www/html`. By the default, only one file resides here, the Apache test page. By default, Apache looks for a file named `index.html`, which currently only stores the content of the test page. 

We can go ahead and remove this file:
1. `~$ cd /var/www/html` *Navigates to the folder*
2. `~$ rm index.html`*Removes the file*

If you go back to your website and refresh the site, you will see that instead of loading the test page, an error message will pop up. Since we deleted the file, Apache has nothing to give us on our website. 

**Creating a new site:**

We now want to create our new website.

First, create the file `index.html`:
1. `~$ touch index.html` *Creates a file called 'index.html'*

And then edit the file with Vim:

1. `~$ vim index.html` *Edits the file with Vim*
2. Write HTML code here to personalize your web page, or find a template online.



**HTML template:**
`<h1> This my webpage </h1>`
`<body>`
   ` <h3>Quote of the day:</h3>`
    `<p><i>Never trust a computer you cant throw out the window</i></p> `
     `<p><i>- Steve Wozniak</i></p> `
 `</body> `


 ### Final steps

 You can now edit the website as you want, and try to go to eachothers websites by typing in their IP-address and port in the URL on the same format as earlier.

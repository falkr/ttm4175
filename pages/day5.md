# Day 5: Our own Web Site

These last two days we are going to create our own web site and set up a web server on the Raspberry Pi. The web server we will use is called _Apache_.

### Learning Goals for Today

:goals:
- Become even more familiar with the Raspberry Pi
- get an overview of how a webserver can be used to host your own websites.


# Step 1: Our own Website

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


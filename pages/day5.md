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



# Editing Your Website 

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
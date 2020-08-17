# Useful Commands

Below you find a list of the commands we used in this course.
We recommend that you learn these by heart --- it makes your work with computers so much more easy.
We promise you will use them often.

Apart from this list of useful commands, we also have collected more information about [how to find information on more commands](commands-help.html).


# Useful Shortcuts

While you type commands and argumets, you can use some useful shortcuts. There are many, but here are some you should know:

* `Ctrl-C` This cancels whatever you currently write, and you get again an empty command line without executing any command.
* `Tab` Pressing the tab key tries to auto-complete the word you are currently writing. This may be for instance a command or a file name. If there are more than one option, nothing will be completed, but if you press tab twice, you will see a list of options.
* `Ctr-R` lets you search in the commands you executed before. Just press `Ctrl-R` and type a part of the command you remember, and you'll get an offer ot matches.

There are also shortcuts to move the curser:

* `Ctrl-a`  Move cursor to beginning of line
* `Ctrl-e`  Move cursor to end of line
* `Ctrl-b`  Move cursor back one word
* `Ctrl-f`  Move cursor forward one word
* `Ctrl-w`  Cut the last word
* `Ctrl-k`  Cut everything after the cursor
* `Ctrl-y`  Paste the last thing to be cut
* `Ctrl-_`  Undo  

These are just a few. You can find more by reading the pages for the shell, by typing `man bash`, or just searching on the internet.


# cat

Concatenate files, but the command also prints a file's content.

# cd


Moving into a directory:

```bash 
cd <path-to-directory>
```

Moving one directory up:

```bash
cd ..
```

Moving in the home directory:

```bash
cd ~
```


# cp

Copy files. 

```bash
cd file.txt file_copy.txt 
```

# curl

Download a file from the internet. 

```bash
curl https://www.ntnu.no/o/ntnu-theme/images/logo_ntnu.svg
```

# grep

Search for a 

# mkdir

Create a directory.


# mv

Move a file

```bash
mv <from_path> <to_path>
```


# rm

Delete a file.

# echo

# info

# ls

# passwd

Changes the password


# sudo

# systemctl

# touch

Create a file.

# ip

Configure network interfaces and routes

Examples:

Verify address and mask from an interface:
```bash
ip address show dev (interface)
```

Add address to an interface:
```bash
ip addr add (ip-address/subnetmask) dev (interface)
```bash

Delete an address from an interface:
```bash
ip addr del (ip-address/subnetmask) dev (interface) 
```

Similar commands can be used for managing routes.



# host

DNS lookup utility

```
host www.ntnu.no
```



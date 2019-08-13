# Introduction to Linux {#lesson1}
## Exercises

Connect your Raspberry PI to the monitor and keyboard but **do not** connect the mouse nor the network/ethernet cable.
Finally, connect the power cable (micro-USB) to your Pi.

These exercises should be completed in teams.

### Exercise 1 --- First boot

First boot and basics.

1. Type on your keyboard the keys `Ctrl+Alt+F2` (i.e. press `Ctrl`, `Alt` and `F2` simultaneously).

> Your display should now show a black and white command line interface, a terminal or virtual console, with a login screen.

2. Log in using "pi" as the username (type and press `enter`) and the password "reactive4115".

> Password inputs in Linux are usually "silent" (i.e. don't worry if you don't see your password being typed in!).

-----------------

Welcome to `bash`! One of the most famous Linux shells, an interactive terminal where we can run multiple commands or programs.
A **Unix** shell is a user interface (usually interactive) to interpret commands and give instructions to the operating system using **GNU** or other software.
It can also be seen as a programming language but we won't be looking at that.
The `bash` is the Bourne Again Shell, an evolution from `sh` or the **Bourne Shell** (from Stephen Bourne) and there are several others (e.g. `zsh` is a very popular choice too).

-----------------

3. Print "Hello World!" in your terminal by typing the command `echo 'Hello World!'` followed by the `enter` key.

> All commands should be followed by the `enter` or carriage return key.

```
$ echo 'Hello World!' # Note: use single quotes
Hello World!
$
```

4. Alternate between terminals using `Alt+F3` (F4, F5, ...)  or `Alt+Left/Right arrows` and login again.

> Linux is a multitasking/multiuser operating system which means that it allows several processes and users to work simultaneously.
>
> **Challenge:** enter the command `sleep 60`, notice how the terminal is occupied, type `Ctrl+z` to move it to the background and `fg` to bring it back to the foreground (you can use this with any command and alternatively you may cancel the `sleep` command with `Ctrl+c`).

5. Logout from one of the terminals using the commands `logout`, `exit` or by pressing `Ctrl+d`.
6. Linux is case sensitive, meaning that the command `echo` cannot be typed as `Echo`. What happens if you enter the command `Echo`?
```
$ Echo 'wrong...'
bash: Echo: command not found
$
```
7. When typing a command, `bash` (the shell we are using), allows saving time with shortcuts such as the `Tab` key to auto-complete and with `Ctrl+a/e` commands and move in the command line. Type `ec+Tab`. What happens?
```
$ ec+Tab
$ echo
``` 
8. Press the `up` key one or more times. What happens?

> With this shortcut you can press the `enter` key to confirm your command and `Ctrl+c` to cancel.

9. Press `Ctrl+r` followed by "Hello" and `enter`. What happens?

> Press `Ctrl+r` multiple times to find other matches, `enter` to confirm, `Ctrl+c` to cancel and the arrow keys to edit.

```
$ (reverse-i-search)`Hello': echo 'Hello World!'
Hello World!
```
10. An important aspect of GNU/Linux is the availability of documentation for all (or almost all) installed commands. Type `man bash`, scroll through using the arrow or space keys, pay attention to the **definitions and reserved words**, leave by pressing `q`.

> **Challenge:** A command similar to `man` but with typically much more detail is `info`, learn how to use it with `info info`.

11. Almost all commands in Linux support the argument "\-\-help" or the option "-h" for a very brief explanation. Try `bash --help`.

> Arguments and options are additional keywords given to commands.

----------------

To sum-up, the simplicity of Unix systems, or the **Unix philosophy**, aims at systems composed of programs that:

1) are simple and elegant (do one thing and do it well);
2) work together;
3) use universal interfaces (e.g. text).

----------------

### Exercise 2 --- File Operations

1. In a new terminal log in again with the user `pi`.
2. List all the files in the current directory by issuing the `ls` command.
```
$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  python_games  Templates  Videos
$
```

3. Find additional options for the command `ls` (use `--help` or `man ls`).
```
$ ls --help
...
$ man ls
$
```
4. Identify the current working directory using the command `pwd`.

> In Linux files and directories are organised in a hierarchy, or in a tree, and the root of the tree is represented by **'/'**.
> This tree is actually a way of representing a disk or disk partitions from a computer, and we can have several ones (typically found in `/dev/`, such as `/dev/sdb`), *mounted* in our system.

``` {.unix .numberLines}
$ pwd
/home/pi/
$
```
5. Change your current directory by using the `cd` command and check your new working directory again with `pwd` (e.g. `cd Desktop`).
```
$ cd Desktop
$ pwd
/home/pi/Desktop
$
```
6. Return to the previous directory using `cd ..`

> If we use `ls -a` we'll see *all* existing files and folders, even the hidden ones, as well as the `..` which corresponds to the parent folder, or the folder that contains our current location (the `.` is our current location).

7. Enter the command `cd notworking`. What happens?
``` {.numberLines}
$ cd notworking
-bash: cd: notworking: No such file or directory
$
```
8. Enter the command `cd ..`, repeat the `pwd` command, what's the result?
``` {.numberLines}
$ cd ..
$ pwd
/home/
$
```
9. Enter the command `ls`. What do you see?
``` {.numberLines}
$ ls
pi
$
```
10. Enter the command `cd`. What's your current directory?

> Users have a home folder, which generically corresponds to their root, and they can easily navigate there with the shortcut `~`.

```




``` {.numberLines}
$ cd
$ pwd
/home/pi/
$
```
11. Enter the command `cd ../../`. What's your current directory?
``` {.numberLines}
$ cd ../../
$ pwd
/
$
```
12. Enter the command `cd root`. What's the result? Why?
``` {.numberLines}
$ cd root
-bash: cd: root: Permission denied
$
```
13. Enter the command `cd ~`. What's you current directory?
``` {.numberLines}
$ cd ~
/home/pi/
$
```

14. Create a new directory, or folder, called "test" with the command `mkdir test`. Change your working directory to this folder.
```
$ mkdir test
$ cd test
$
```

15. Create two empty files with the command `touch` (e.g. `touch file1`) and verify with `ls`.
```
$ touch file1
$ touch file2
$ ls
file1  file2
$
```

16. Remove one of the files by issuing the command `rm` and then verify again.

> **Note:** the file has been effectively deleted (or unlinked to be precise), there's no trash or recycle bin, so take care or use the option "-i" to enable confirmation before deletion.

```
$ rm file1
$ ls
file2
$
```

17. Go to the parent directory (i.e. the previous folder), confirm your location (you should see the "test" folder you created).
```
$ cd ..
$ pwd
/home/pi
$ ls
... Templates  test  Videos
$
```

18. Attempt to delete the "test" folder with `rmdir test` (remember we still have a file inside this folder). What happens?
```
$ rmdir test
rmdir: failed to remove 'test': Directory not empty
$
```

19. Delete the "test" folder by first removing the remaining file with `rm ./test/file2` and then using `rmdir`.

> **Note:** if we are sure that we want to delete everything inside a directory we can use the command `rm -r` but it's dangerous because it removes everything inside that folder. Moreover, if by mistake we delete system files/folders we may end up with a destroyed system.

```
$ rm ./test/file2
$ rmdir test
$
```
20. Create a new file named "notaudio.mp3"
```
$ touch notaudio.mp3"
```
21. Create a copy of the new file in the folder "Music" using the name "na_copy.mp3", by typing the following command `cp notaudio.mp3 ./Music/na_copy.mp3`. Verify that it is created in the right folder with the right name.
```
$ cp notaudio.mp3 Music/na_copy.mp3
$ ls Music/
na_copy.mp3
$
```
22. Move the file "notaudio.mp3" to the "Music" folder using the command `mv`.

> When moving or copying files, if we only specify the destination and omit the name, the origin name of a file/directory will be used (if a different path is used).

```
$ mv notaudio.mp3 Music/
$
```

23. Rename the file "na_copy.mp3" to "notaudio2.mp3" also by using the command `mv`.

> **Hint 1:** Don't forget to use the `Tab` key to speed up your typing.
>
> **Hint 2:** `cp` and `mv` can also use the option '-i', which is helpful for avoiding overwriting already existing files in the destination target (similar to the `rm` command for confirmation).

```
$ cd Mu+Tab
$ mv -i na+Tab not+Tab (and add 2 to the name)
$ cd ..
$
```
### Exercise 3 --- Viewing and editing files

View the content of files in the terminal and/or edit them.

1. Print the output of the system's log, which is stored in "/var/log/messages", using the command `cat`.

> Due to the importance of this file, its contents can also be seen by simply issuing the command `dmesg`.
> To scroll up and down we can use `Shift+pgup` and `Shift+pgdown`.
>
> An alternative to `cat` is `nl`, if we want to see line numbers in the output.

```
$ cat /var/log/messages
...
$
```

2. To determine how many lines a file has the command `wc` can be used. How many lines does your log have?
```
$ wc -l /var/log/messages
1099    #approx
$
```

3. To print the first or last few lines of a file the commands `head` and `tail` can be used respectively. How many lines do you see?
```
$ head /var/log/messages        #or tail
...     #10 lines is the default
$
```

4. Open the log file with the viewer `less` and find the available options by pressing `h`. How do you exit the viewer?
```
$ less /var/log/messages        #q to exit
$
```

5. Inside `less` search for the line in the log file that contains the text "Linux version". What's the line number and Linux version?

> **Hint:** Use `less -N` and its search functionalities. Replace *pattern* by "Linux version".

```
$ less -N #/Linux version + enter
$
```

6. Search for the total number of processors mentioned in the log file using the pattern "Total.*processor". <!--- *vim... --->
How many processors are activated?

> **Note:** This exercise is using a regular expression pattern, matching all strings that contain "Total" and "processor" with anything in between.

```
$ less -N       # type /Total.*processor + enter  --> 4 processors
$
```
7. Instead of viewing or printing entire files `grep` can be used to efficiently search for patterns inside files.
Search for the total number of processors using `grep`.
What option can you use to also print the line number?
```
$ grep -n "Total.*processor" /var/log/messages
###:Aug 27 ... raspberry kernel: ... Total of 4 processors activated
$
```

8. Knowing the line number of interest, it's easy to return to `less` and verify surrounding context by typing `:` followed by the line number.
How can we use `grep` to also show this context? For example 5 lines before and after the line of interest?

```
$ grep -n -C 5 "Total.*processor"
...
$
```

-------

Other widely used programs are `sed` and `awk`.
They are both quite powerful and allow editing the files we are working with.
In particular, `sed` is a typical solution for finding and replacing parts of a file **without having to manually edit** them, while `awk` implements the AWK programming language and is more suited for managing files organised in columns or using specific separators.
Remember that `grep` is the best option for extracting text but we can also return to the log file example using both `sed` and `awk`:

<!-- `sed 's/\(total.*processor\)/\1/i;t;d' /var/log/messages`-->
`sed -n '/total.*processor/Ip' /var/log/messages`

or

`awk '/[tT]otal.*processor/' /var/log/messages`

Apart from simple command line tools for viewing and editing files based on filters and expressions, there are also several Command Line Interface (CLI) editors that can be used, examples are `vim`, `nano` and `emacs`.

---------

9. In your home directory enter the command `nano myfile.txt`, which will open the editor `nano` and type in "This editor is great!". Save and exit `nano`.

> **Hint:** You can get help and a list of shortcuts by pressing `^G`.
This means pressing `Ctrl+g` and `M-r` means `Meta+r` (the meta key is usually the Alt key).

```
$ nano myfile.txt
This editor is great!  -->^X, Y, enter
$
```

10. Open again the same file with `nano` and press `Ctrl+\`, type "great" and press `enter`, type "ok" and `enter`, press 'y'. 
What happens?
```
$ nano myfile.txt
This editor is ok!  -->^\, great, ok, Y
$
```
11. Open "myfile.txt" with the command `vi`, press `i` to enter the *INSERT mode*, edit the file (write something) and press `Esc Esc` to return to the *COMMAND mode*, followed by `:q` to exit the editor.
What happened?
Follow the editor's suggestion to exit without writing the file.

```
$ vi myfile.txt
...     --> after :q
E37: No write since last change (add ! to override)
        --> use :q! to ignore changes
$
```

### Exercise 4 --- Linux Permissions

Permissions, users and groups.

-----------

In Linux each file has a set of permissions or access mode (read, write and execute), as well as an owner and group owner.
This is one of the reasons why Unix/Linux are also considered to be secure, providing quite a robust line of defence that separates files and folders from users, groups and applications.
Nowadays most operating systems have something like this, or similar.

-----------

1. Try to list the contents of the directory in "/root/" using the user "pi". What happens?

> With the command `ls -ld /targetdir/` you can verify the permissions of a directory (first column) as well as its owner (3rd col.) and group (4th col.)
>
> You should see something like: `drwx------ 2 root root 4096 Aug 27 14:00 /root`.
> In the first col. the 'd' stands for directory and the remaining 9 characters are the permissions for the user ('rwx'), for the group ('\-\-\-') and for others ('\-\-\-'), explained after the next exercise.

```
$ ls /root/
ls: cannot open directory /root: Permission denied
$
```

2. Find your username and associated groups using the commands `whoami` and `groups`
```
$ whoami
pi
$ groups
pi adm dialout cdrom sudo audio video plugdev games users immput netdev gpio i2c spi 
$
```

------------

With the information about users, groups and permissions we can better manage who accesses what and prevent mistakes or malicious actions.
To change permissions we can use the command `chmod` followed by a flag for the user (**u**), group (**g**) and others (**o**), a sign for adding or removing permissions (**+** and **-** respectively), and the permission we want to edit: read (**r**), write (**w**) or execute (**x**).

In all Linux machines there is a super user, or "root".
This user can access all the directories and files from other users, regardless of the permissions, and even change/create new users and change their passwords.
To run commands with administrator or root privileges we use the command `sudo` or change our terminal with `su` and run multiple commands as root.
The command `su` allows us to change our current terminal not only to root but also to any other existing user, provided we know the login name and password (e.g. `su - palma`).
However, if we are the super user, we can simply change user without need for any password (**Remember:** with great power comes great responsibility).

------------

3. Run the command `sudo whoami`. What's the result? What does this mean?
```
$ sudo whoami
root   #this means we ran the command whoami as the super user
$
```

4. List the contents of the directory in `/root/` using `sudo`. How many files are in that directory?
```
$ sudo ls -l /root
total 0
$
```

5. Change the permissions of the folder "/root/" with the command `chmod o+r` so that other users can read the content of the folder.
Check the new permissions with `ls -ld`.
List its contents **without** using `sudo`.

> **Note:** The new permissions include an 'r' in the permissions for others.

```
$ sudo chmod o+r /root
$ ls -ld /root
drwx---r-- 2 root root 4096 Aug 27 14:00 /root
$ ls -l /root
total 0
$
```
6. Change your current user to root with the command `sudo su` and confirm it with `whoami`.

> **Note:** You should be very careful when working as root and should avoid it unless it is completely necessary!

```
$ sudo su
$ whoami
root
$
```

7. Revert the permissions of the `/root/` folder, without using `sudo`, so other users cannot read it ('o-r').
Exit the "root terminal" by entering the `exit` command in the terminal.

```
$ chmod o-x /root
$ exit
$
```

### Exercise 5 --- Personalisation

1. Change the default password (`passwd`) of the user "pi".

> **Milestone:** make sure you have changed the password before continuing (e.g. login in another terminal using the new password).
> If you skip this step your Raspberry Pi will be **vulnerable to remote attacks** as soon as we connect it to the Internet.

```
$ passwd
Changing password for pi.
(current) UNIX password: reactive4115
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
$
```

2. Create a new user (`useradd`) using a login name of your choice, while also including the user in the already existing groups "dialout,audio,video".
Alternatively, create a user and add it to these groups afterwards (`usermod`).
Don't forget to set the password for the new account!
What options did you use?

> **Hint:** remember to use Linux's existing help commands and that you'll need administrator privileges.

```
$ sudo useradd -d /home/user/ -s /bin/bash/ -m -g users \
                             -G dialout,audio,video user
$ # omit -g users to automatically create a group named 'user'
$ sudo passwd user
Enter new UNIX password: 
Retype new UNIX password:
passwd: password updated successfully
$
```

3. Change terminal and login with the new user name.
```
$ # Alt+<F2> to change terminal
$ login: user <enter>
$ Password: <enter>
```

4. Add the new user to the list of *sudoers*
    - Return to the first terminal;
    - Add write permissions to the file **010_pi-nopasswd** `/etc/sudoers.d/` (`chmod`);
    - Edit the file to include your new user;
    - Remove the write permissions (`chmod`) and return to the previous terminal.

```
$ # Alt+left to change terminal
$ cd /etc/sudoers.d
$ sudo chmod +x 010_pi-nopasswd
$ sudo vim 010_pi-nopasswd # yyp:s/pi/user<enter>:wq<enter>
$ sudo chmod -x 010_pi-nopasswd
$ cd
$ # Alt+right
```

5. Change your _hostname_ to match your team number (e.g. "Team1"), based on the following steps:
    - find and edit the files **hostname** and **hosts** in "/etc";
    - replace any entries with your current _hostname_ with the new one;
    - reboot the system with the `reboot` command or with `shutdown -r`.

> With the `shutdown` command we can turn off the system completely, or halt, by typing `shutdown -h now`, reboot, schedule a shutdown or cancel a scheduled shutdown.

```
$ cd /etc
$ ls host*
$ sudo vim hostname #edit, :wq to save and quit
$ sudo vim hosts #edit, :wq to save and quit
$ # alternative option - use find and repeat the other commands
find /etc -type f -name host* 2> /dev/null
$ # same vim commands as in option 2

$ reboot # for all
```

6. How could you repeat the previous step without manually editing each file? (answer either by explaining the overall idea or with the actual command(s) you would use)
```
$ sudo sed -i 's/pi/team1/' /etc/hosts /etc/hostname
```

7. What would happen if you added "ntnu.no" after your hostname in your hosts file?
```
$ # every internet access to ntnu.no would be redirected to localhost
$ ping ntnu.no
PING team1 (127.0.0.1) 56(84) bytes of data.
 ...
```

### Exercise 6 --- Networking

Connecting the Raspberry Pi to the Internet.

1. Verify your system's IP addresse(s) by issuing the command `ip address`.
How many interfaces do you see?
Note the information for "eth0".

> **Hint:** Existing interfaces are numbered and named (e.g. "1:  XXX:").
> IP(v4) addresses and the respective mask follow the format XXX.XXX.XXX.XXX/YY.

```
$ ip address
1: lo:  ...  state UNKNOWN
    link/loopback ... 
    inet 127.0.0.1/8 scope host lo
...
2: eth0:  ...  state DOWN
    link/ether ...
```

2. What's the route your Raspberry Pi will follow to reach the Internet? Find out with `ip route`.
```
$ ip route
$ #no route to the Internet (the cable is disconnected...)
```

3. Connect the ethernet cable to your Raspberry and note the changes in your IP addresses and routes.

> **Note:** By default, the Linux distribution we are using has a running service, or daemon, that automatically configures network interfaces whenever a new link is found.
> This service is called `dhcpcd` and runs a networking protocol called DHCP.

```
$ ip address
1: lo:  ...  state UNKNOWN
    link/loopback ... 
    inet 127.0.0.1/8 scope host lo
...
2: eth0:  ...  state UP/UNKNOWN
    link/ether ...
    inet 129.241.200.XXX/24
...
$
$ ip route
default via 129.241.200.1 dev eth0 proto dhcp src 129.241.200.XXX
129.241.200.0/24 dev eth0 proto kernel scope link src 129.241.200.XXX
129.241.200.1 dev eth0 proto dhcp scope link src 129.241.200.XXX
```

4. Check if you have Internet connectivity using the command `ping` (stop it with `Ctrl+c`).
This will use the ICMP protocol to contact an Internet server of your choice (e.g. `ping ntnu.no` or `ping 8.8.8.8`).

> **Milestone:** if this command fails please ask for help before continuing.

```
$ PING ntnu.no (129.241.160.102) 56(84) bytes of data.
64 bytes from ntnu.no (129.241.160.X): icmp_seq=1 ttl=61 time=0.263 ms
64 bytes from ntnu.no (129.241.160.X): icmp_seq=2 ttl=61 time=0.311 ms
^C
--- ntnu.no ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 3ms
rtt min/avg/max/mdev = 0.263/0.287/0.311/0.024 ms
$
```

5. Use `wget` to download a *zip* file from:
 - https://www.iik.ntnu.no/ttm4175/wp-content/uploads/2018/08/ttm4175-files.zip
```
$ wget https://www. ... .zip
--2018-08-23 13:58:23--  https://www. ...
Loaded CA certificate '/etc/ssl/certs/ca-certificates.crt'
Resolving www.iik.ntnu.no (www.iik.ntnu.no)... 129.241.200.18
Connecting to www.iik.ntnu.no|129.241.200.18|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 682251 (666K) [application/zip]
Saving to: 'ttm4175-files.zip'

ttm4175-files.zip   100%[===...==>] 666.26K  --.-KB/s   in 0.06s   

2018-08-27 ... (11.4 MB/s) - ttm4175-files.zip saved [682251/682251]
$
```

6. Create a new user named "guest" with the password "komtek18!", making sure you also create a home folder (`-m` option in `useradd`).

> **Note:** this new user will be used for another team to login into your system.

```
$ sudo useradd -d /home/guest/ -m guest
$ sudo passwd guest
Enter new UNIX password: 
Retype new UNIX password:
passwd: password updated successfully
$
```

7. In the Linux distribution we are using the home directories give read and execute privileges to "group" and "others".
Change the permissions of the home directory of the user "pi" so that your guest cannot see its contents.
```
$ chmod o-rx /home/pi
$
```

8. Find a team close to you and exchange your IP addresses.
Use the received address, together with the command `ssh` to connect to the other team's computer (e.g. `ssh guest@ipaddress`).

> **Note:** a warning message should appear the first time you connect since the certificates being used have never been exchanged before.
> After logging in you should notice a different hostname.

```
$ ssh guest@129.241.200.XXX
The authenticity of host ...
...
Are you sure you want to continue connecting (yes/no)? yes <enter>
guest@129.241.200.XXX's password: <enter>
...
$
```

9. Send a message to all the users/terminals of the remote machine by using the command `wall`. What happened? Check with the other team.

> **Note:** if nothing happened on the remote side, ask the other team to type the command `mesg y` in their terminal.

```
$ wall my_message
Broadcast message from guest@teamX (pts/1) (Mon Aug...)

my_message

$
```

10. Instead of sending a message to all the users, use the command `who`, or the command `w` to find out who's in the system and send a message directly to their terminal using the command `write` and `Ctrl+d` to terminate the message.

> **Note:** if you receive the output "write: *user* has messages disabled on ttyX" ask your colleagues to type `mesg y` in their terminal.

```
$ write pi tty1
a message <enter>
^D
$
```

11. In a different terminal (or exit the `ssh` session), copy the file "myfile.txt" created earlier to the other team's machine using the command `scp`.
Verify that the home folder of the "guest" user has a copy of this file afterwards.
```
$ scp /home/pi/myfile.txt guest@129.241.200.XXX:.
guest@129.241.200.XXX's password: <enter>
myfile.txt                              100%  25    0.0KB/s 00:00
$
```

12. Return to the terminal with the remote session (or use `ssh` again), and try the following commands replacing the *user* and *tty* with the information obtained when checking `who`'s logged in:
- `echo "Redirecting to a new file (destructive)." > redir.txt`
- `echo "Redirecting, don't care if it already exists!" > redir.txt`
- `echo "Appending if it exists, creating if not." >> append.txt`
- `echo "Appending if it exists, creating if not." >> myfile.txt`
- `write user tty < myfile.txt`

What happened? Were the new files created locally or remotely?
```
The first creates a new file ("redir.txt") with the same string.
The second replaces the contents of "redir.txt" with the new string.
The third creates a new file ("append.txt") with the same string.
The fourth appends the new string instead of replacing the content.
The fifth used the content of "myfile.txt" as the input text for write.

The files were created remotely because we were in a remote terminal.
```

13. Try the commands:
- `cat myfile.txt | write user tty`
- `sed 's/ /_/g' myfile.txt | write user tty`

What happened? Was "myfile.txt" modified by any of the commands?

```
The first outputs the contents of "myfile.txt" to write.
The second replaces all the spaces by underscores and outputs the changed contents to write.

The file was not modified.
```

------------

Before commands are executed, their input and output can be redirected using a special notation interpreted by the shell.
">" and "<"  are symbols used for enabling this redirection, opening and closing files for the respective shell execution environment.

"|" is the *pipe* symbol, used in the famous Unix pipeline, in which the output of one command becomes the input of a second.
This allows using text as an interface between different programs and the creation of more complex programs based on simpler ones. 

------------

<!-- TODO
 - run remote commands without interactive shell
 - create ssh keys
 - screen
-->

### Exercise 7 --- More GNU/Linux

Additional experiments with common GNU/Linux programs.

1. Extract the *zip* file downloaded earlier with the command `unzip`.
```
$ unzip ttm4175-files.zip
Archive:  ttm4175-files.zip
   creating: ttm4175-files/
...
  inflating: ttm4175-files/onesmall.wav
$
```

2. Verify the size of the created folder and *zip* file with the commands:
- `ls -ld ttm4175-files*`
- `ls -ld --block-size=K ttm4175-files*`

Explain what you observe.
```
$ ls -ld --block-size=K ttm4175-files*
drwx--x--- 7 pi pi   4K Aug 27  2018 ttm4175-files
-rw-r--r-- 1 pi pi 667K Aug 27 15:51 ttm4175-files.zip
$
```

3. In the previous exercise, how can you use the command `sed 's/.* \([0-9]*K\).*/\1/'` the see the size only?
```
$ ls -ld --block-size=K ttm4175-files* | sed 's/.* \([0-9]*K\).*/\1/' # UNIX pipeline
4K
667K
$
```

4. As you may have noticed, the uncompressed folder is smaller than the compressed file.
Or is it?
Use the command `du`, with the necessary options, to verify the actual disk usage of the files in the folder.

> In Linux "everything" is a file, even a directory, and the command `ls` shows the size of the file corresponding to the directory, not its files.

```
$ du -hs ttm4175-files*
2.1M	ttm4175-files
668K	ttm4175-files.zip
```

5. Enter the "ttm4175-files" directory, execute the following commands and register what happens with each:
- `ln -s a/very/strange/directory/structure struct`
- `ls *.mp3`
- `file *.mp3`
- `ls *one*`
- `find . -name "*.txt"`
- `find . -type f -name "*.txt."`
- `find . -type f -name "*.txt" -print`
- `find . -type f -name "*.txt" -print -exec head '{}' \;`
- `find /usr -type f -executable -name find`
- `whereis find` 
- `time find /usr -type f -executable -name find`
- `time whereis find` 

> **Hint:** Use the documentation to find what the commands do and experiment with commands you already know (`ls`, `pwd`, etc.).

```
$ ln -s a/very/strange/directory/structure struct # soft/symbolic link
$ ls -la struct
lrwxrwxrwx 1 pi pi 34 Aug 23 01:12 struct -> a/very/strange/directory/structure
$
$ ls *.mp3
onesmall.mp3  torvalds-says-linux.mp3 
$
$ file *.mp3 
onesmall.mp3: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 8 bit, mono 11025 Hz
torvalds-says-linux.mp3: MPEG ADTS, layer III, v1, 128 kbps, 44.1 kHz, Stereo
$
etc. etc.
```


## References

- [Raspberry Pi -- Getting Started](https://www.youtube.com/watch?v=wjWZhV1v3Pk)
- [Unix Pipeline](https://www.youtube.com/watch?v=bKzonnwoR2I)
- [grep](https://www.youtube.com/watch?v=NTfOnGZUZDk)
- [Regular Expressions](https://hackaday.com/2018/03/09/linux-fu-regular-expressions/)[.](https://xkcd.com/208/)
- [Network Stacks and the Internet](https://www.youtube.com/watch?v=PG9oKZdFb7w)
- [Why do we need IP addresses?](https://www.youtube.com/watch?v=iGPXkxeOfdk)
- [IP addresses and the Internet](https://www.youtube.com/watch?v=L6bDA5FK6gs)

Additional _optional_ materials:

- [A little bit of history](https://www.youtube.com/watch?v=tc4ROCJYbm0)
- [Introduction to Linux](http://tille.garrels.be/training/tldp/index.html) (only chapters 1, 2, 3, 5 and 6)
- [Bash Guide for Beginners](http://www.tldp.org/LDP/Bash-Beginners-Guide/html/index.html) (only sections 1.1, 1.3, 1.6, 3.4, 4.1, 4.2, 5.1, 5.2, 6.1, 6.2 and 6.3)
- [Quick introduction to `vim`](https://www.ibm.com/developerworks/linux/tutorials/l-vi/index.html#N101AE)
- [Interactive `vim` tutorial](http://vimgenius.com/)
- [Bash Pitfalls and Solutions](https://mywiki.wooledge.org/BashPitfalls) (**advanced!**)


-----------------


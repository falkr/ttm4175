# Day 2: The Linux Terminal

Today, many of you will take your first steps with the powerful Linux terminal.

### Learning Goals

:goals:
- Become familiar with Linux commands and the terminal
- Feel home on the Raspberry Pi
- understand user permissions


### New Linux Commands

- [cd](commands.html#cd) --- change into another directory 
- [curl](commands.html#curl) --- powerful tool for web requests, among other to download a file
- [ls](commands.html#ls) --- list files and folders
- [pwd](commands.html#pwd) --- show in which directry you are
- [sudo](commands.html#sudo) --- running commands as super user


# Navigating Folders and Files

On Linux, **files** are sorted in **folders**, just like you are used to from other computers. 
Sometimes, _folder_ are also called _directories_. 
Since folders can be other folders, this creates a tree-like hierarchy. 
Each file and folder therefore has a **path**.

The path of the home directory, for instance, is in `/home/pi`, for the default user with the name `pi`.
There are two things about paths you need to remember:

- They start with a `/` in the beginning, this is the topmost folder. This topmost folder is also called _root_ folder.
- The different folders and files are separated by `/`.


### Find out where you are with pwd

When you are in the terminal, you are always in some folder. When you boot up and just open a terminal, you usually start in the home folder. If you are not sure, where you are currently, type the `pwd`command, which stands for _"**p**rint **w**orking **d**irectory"_.

```bash
pwd
```

The output of this command will then be the path of the current folder you are in.

### Change the folder with cd

Using the `cd` command, which stands for _"**c**hange **d**irectory"_, you can change into any riectory, using its path. Type the following to move into your home folder:

```bash
cd /home/pi
```

Since the home folder is so so useful, its path has an abbreviation, which is the funny snake `~` (tilde). You can hence also write the following to change into the home directory:

```bash
cd ~
```

If you want to move just one folder up in the hierarchy, for example, you are in `/home/pi` but would like to go into `/home/`, you can do that with the special path `..`. Here, the `..` just means "one up". So, we can type the following:

```bash
cd ..
```

This moves you one folder up. You can check where you are using the `pwd` command. 

### Listing Folder Content with ls

To look at the files and folders inside a folder use the `ls` command. (Remember it with the word _"**l**i**s**t"_.) For example, move into the root folder at the top and see which files and folders are listed there:

```bash
cd /
```

and then 

```bash
ls
```

will list the following:

---
type: figure
source: figures/teknostart/rpi-terminal-folders-1.png
---

Note that there are different colors for folders and files. 

If you want some more detailed information about folders and files, you can use the `ls -l` command, that means, the `ls` command with an **option** `-l`. When you invoke it in the root folder, for instance:

```bash
ls -l
```

now the listing will look as follows:

---
type: figure
source: figures/teknostart/rpi-terminal-folders-2.png
---


# Being Super User

Some commands or programs require special permissions to run, usually because they affect more than one user or handle critical resources, or are related to the security of the system.
As the user `pi`, you _have_ all these permissions, but to protect you from doing something stupid, you need to prove to the system that you are allowed to execute these specific commands or programs. For that, the command `sudo` exists, which stands for _"**s**uper **u**ser **do**"_. SOmtimes you just add this in front of another command that you want to execute with special rights. 

```bash
sudo <important command...>
```

Think of it as when your parents told you to say "Please!"





# Capture the Flag

Capture the Flag (CTF) is a special kind of information security competition. There are three common types of CTFs: Jeopardy, Attack-Defence and mixed.

- Jeopardy-style CTFs has a couple of questions (tasks) in range of categories. For example, Web, Forensic, Crypto, Binary or something else. A team gets some points for every solved task. Generally teams will be awarded more points for more difficult tasks. The next task in the chain will be unlocked after you solve the previous one. The team with the most points when the time is over is the winner. A famous example of this kind of CTF is the DEFCON CTF Qualifier.
- Attack-defence is another interesting kind of competition. Here every team has their own network, with many machines, or a single computer, with vulnarable services. The teams are given an amount of time to patch services and secure the network or system and developing exploits to hack the systems of other teams.  So, then organizers connects participants of competition and the wargame starts! You should protect own services for defence points and hack opponents for attack points. Historically this is a first type of CTFs, everybody knows about DEF CON CTF - something like a World Cup of all other competitions.

Today we are going to do a relatively short Jeopardy-style CTF. The category is Linux, which means that the security aspect of the CTF is not really present. It is more of a way to become more familiar with the terminal and navigation around the Linux file structure. The game consists of 10 levels that are supposed to make you feel a little more comfortable using the Terminal as a tool for the Linux Command Line. The first level is used as an example to show how the game is run.


## Install CTF

The file `teknostart_ctf.py` is located in you home folder, which would be `/home/pi`. This is a progam written in the programming language [Python](https://www.python.org/), and is a terminal-based game.



### Step 1: Move to the Home Directory

Open the terminal and check in which folder you are. We do that with the command `pwd` (_"print working directory"_):

```bash
pwd
````

The output shows in which folder or directory  you are. Move into your home directory, using the `cd` (_"change directory"_) command:

```bash
cd /home/pi/
````

:tip: You can also move to the home directory by writing `cd ~`. The wiggly line that looks like a snake is called _tilde_ and an abbreviation for your home directory.


### Step 2: Download CTF


We now download the file containing the CTF program. 

```bash
curl .... 
```

:tip: When you download such a file and then run it, you need to make sure that you know what it contains or trust its origin. The file can run programs that have access to everything on your computer. 


### Step 3: Run the program

To run an executable file in Linux, we type `./` followed by the name of the program. 
Run the program `teknostart_ctf.py`. 

```bash
./teknostart_ctf.py
```


# Example: First CTF Task

### Step 1

Run the program for the first time:

```bash
./teknostart_ctf.py
```

You should get an output back that looks like this. 

```
CURRENT LEVEL: level 1
----------------------------------------

I /etc/komtek ligger det èn fil, hva er navnet på denne filen?

Example answer:      filnavn.txt         
Answer given:        None                
Hash of answer:      dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91
Correct hash:        3240af5f279f28ba703346977438465621d43c5cfe10b053bfb48311b4de0058

----------------------------------------
```

- `CURRENT LEVEL` *is the level that you are currently on, this will increase as you progress*
- `Question` *is the task for this level, read it carefully* 
- `Example answer` *is an example answer to give you an idea of what format the answer should be. for instance, when asked about a file name, this example tries to show that we are looking for the full filename, including the file ending `.txt`.*
- `Answer given` *is the answer you gave, which is "None" by default*
- `Hash of answer` *is a hashed version of your answer. The game takes the answer that you put in, does some math on it, and generates a  [string](https://en.wikipedia.org/wiki/String_(computer_science)) which it will try to compare to the hashed version of the correct answer.*  **(TODO: Make this more clear)**
- `Correct hash` *is the hashed version of the correct answer. If this hash matches the hash of your answer, the answer is correct*


### Step 2: Solve the task

The first you will see is what level you are on, in this case, level 1. As you progress, this will increase. Next is the challenge for this level. This question asks for a file name stored at a particular location, more specifically in `/etc/komtek`. 

In this example, the task is to find the file in `/etc/komtek`.

First we change our directory to that folder:
![alt text](https://home.samfundet.no/~halvogro/ting/bilder/image-40.png)

To check that we are in fact in the right folder, we can use `pwd`.

![alt text](https://home.samfundet.no/~halvogro/ting/bilder/image-42.png)

We can now list all the files in the folder with the command `ls`.
![alt text ](https://home.samfundet.no/~halvogro/ting/bilder/image-43.png)

and here is our file!

### Step 3: Check if you got the correct answer

To test our answer, we run the program again and input our answer `first_flag.txt`.

First we change directory back to where `./teknostart_ctf.py`is located.
1. `cd /home` or simply `cd`, these commands both changes the current directory to you home folder. 
2. `./teknostart_ctf.py first_flag.txt`

You will receive the message:
```
Congratulations, you have been promoted to the next level!
```
followed by the next question. Try to solve as many of the tasks as you can.

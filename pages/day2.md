# Day 2: The Linux Terminal

Today, many of you will take your first steps with the powerful Linux terminal.

### Learning Goals

:goals:
- Become familiar with Linux commands and the terminal
- Feel home on the Raspberry Pi
- understand user permissions

### New Linux Commands

- [curl](commands.html#curl) --- powerful tool for web requests, among other to download a file



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
pwd /home/pi/
````

:tip: You can also move to the home directory by writing `cd ~`. The wiggly line that looks like a snake is called _tilde_ and an abbreviation for your home directory.


### Step 2: Download CTF


We now download the file containing the CTF program. 

```bash
curl .... 
```

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

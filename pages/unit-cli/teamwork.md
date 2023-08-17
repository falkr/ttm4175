# The Linux Command Line Interface (CLI)

## Learning Goals

:goals: Goals for this week's lab

- Get to know the Linux Command Line Interface (CLI)
    - Understand its importance
    - Learn basic commands for 
        - Navigation
        - Remote access
        - Networking-related tasks
    - Understand basic virtualization principles


## Overview of the Day

- Connect to the Lab VM
- Practice using basic commands for file system manipulation and file search in a Jeopardy-style Capture-the-Flag (CTF) scenario
- Practice using text search and text aggregation commands to solve a whodunit-style crime mystery

# Connecting to the Lab VM

After receiving the credentials for your team's VM, please refer to [the preparation page](preparation.html#connecting-via-vnc) for a guide on how to connect to it.

:tip:
We suggest that you use one computer to connect to the VM and type in the commands.


Upon connecting to the VM, launch the *Terminal Emulator* application from the desktop.


# Capture the Flag

Capture the Flag (CTF) is a special kind of information security competition. The goal is to collect passwords, or **flags** to progress. There are three common types of CTFs: Jeopardy, Attack-Defence, and mixed.


- **Jeopardy-style CTFs** have a couple of questions (tasks) in a range of categories. For example, web, forensic, or crypto. Teams get points for every solved task. Generally, teams will be awarded more points for more difficult tasks. Consecutive tasks are unlocked after solving the previous one. The team with the most points when the time is over is the winner. A famous example of this kind of CTF is the *DEFCON CTF Qualifier*.
- **Attack-defence** is another interesting kind of competition. Here, every team has their own network, with many machines, or a single computer, with vulnerable services. The teams are given an amount of time to patch services and secure the network or system, and to develop exploits to hack the systems of other teams. Then, organizers connect participants of the competition and the wargame starts. You should protect own services for defence points and hack opponents for attack points. Historically, this is the first type of CTFs. For instance, the *DEFCON CTF* is something like the World Cup of CTF competitions.

Today, we are going to do a relatively short Jeopardy-style CTF about basic Linux commands. It will help you become more familiar with the terminal and navigation around the Linux file structure. The game consists of 12 levels that are supposed to make you feel a little more comfortable using the Terminal as a tool for the Linux Command Line. The first level is used as an example to show how the game is run.


## Preparing the CTF

Note: this CTF is based on Halvor Groven's [original implementation from 2020](https://home.samfundet.no/~halvogro/teknostart2020/teknostart_ctf.zip).

### Step 1: Move to the CTF Directory

Open the terminal and check which folder you are in. We do that with the command `pwd` (_"print working directory"_):

```bash
pwd
```

Move into the `teknostart_ctf` folder inside your home directory, using the `cd` (_"change directory"_) command:

```bash
cd /home/netlab/teknostart_ctf
```

:tip: You can also move to the home directory by writing `cd ~`. The wiggly line that looks like a snake is called _tilde_ and an abbreviation for your home directory.


### Step 2: The CTF and Levelcheck Programs

This is a terminal based game and is written in the programming language [Python]((https://www.python.org/)). There are two files that are important for the CTF:

- `teknostart_ctf.py`, which is the actual CTF program. Its usage is explained in the next section.
- `levelcheck` is needed for some levels and checks if the tasks have been completed. It prints out the flag if the task has been done correctly. It is used to retrieve the flag (password) for some levels, where it has to be checked whether you completed the task correctly.

To run an executable file in the folder that you are currently in, we type `./` followed by the name of the program.

# Example: First CTF Task

### Step 1

Run the program for the first time.

```bash
./teknostart_ctf.py
```

You should get an output that looks like this. 

```
CURRENT LEVEL: level 1

----------------------------------------

In which folder are you located when you open the terminal?

Example answer:      /folder/folder      
Answer given:        None                
Hash of answer:      dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91
Correct hash:        1c4d3877bf4fe64f9d55cdbbf10d9b02c329b2a5a162ae3014b83da8c3024a71
Levelchecker:        NO                  

----------------------------------------

```

- `CURRENT LEVEL` is the level that you are currently on, this will increase as you progress.
- `Question` is the task for this level, read it carefully.
- `Example answer` is an example answer to give you an idea of what format the answer should be. For instance, when asked about a file name, this example tries to show that we are looking for the full filename, including the file ending `.txt`.
- `Answer given` is the answer you gave, which is "None" by default.
- `Hash of answer` is a hashed version of your answer. The game takes the answer that you put in, does some math on it, and generates a [string](https://en.wikipedia.org/wiki/String_(computer_science)) which it will try to compare to the hashed version of the correct answer.
- `Correct hash` is the hashed version of the correct answer. If this hash matches the hash of your answer, the answer is correct.
- `levelcheck` tells you whether you have to use the `levelcheck` program to check that you have done the task correctly.
-- The value is either `YES` or `NO` for each level. If this says `YES`, it means you have to navigate to `/home/netlab/teknostart_ctf` and run `./levelcheck` to check that you have completed the task correctly. If you have, you will get the password (flag) to progress to the next level.


### Step 2: Solve the Task

The first you will see is what level you are on, level 1 in this case. As you progress, this will increase. Next is the challenge for this level. This question asks for the folder path that you are in each time you launch a new terminal.

First, we open a new terminal and check which folder we are in by typing `pwd`.


---
type: figure
source: img/ctf-001.png
---


As we can see, we are located in `/home/netlab`. 

### Step 3: Check Your Answer

To test our answer, we run the program again and input our answer, `/home/netlab`.

First we change the directory back to where the program `teknostart_ctf.py` is located.

Because we are already inside the folder `/home/netlab`, we can simply type `cd teknostart_ctf`, which will put us in `/home/netlab/teknostart_ctf`. 

You can confirm the presence of the program by typing `ls` to list the files in the directory, and checking for `teknostart_ctf.py` among the outputs.

We can now run it, and input our answer `/home/netlab`.


---
type: figure
source: img/ctf-002.png
---


Success! We have provided the correct flag and the next task is given to us. Try to solve as many of the following tasks as you can.


# CLI Mystery

[Command Line Mystery](https://github.com/veltman/clmystery)

intro, pointers to cheatsheet and how to use hints, how to check solutions.




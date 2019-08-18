y 2: The Linux Terminal

Today, many of you will take your first steps with the powerful Linux terminal.

### Learning Goals

:goals:
- Become familiar with Linux commands and the terminal
- Feel home on the Raspberry Pi
- understand user permissions

### New Linux Commands

- [curl](commands.html#curl) --- powerful tool for web requests, among other to download a file
- ls --- List the files in you current directory
- mkdir --- Create a folder in your current directory
- cd --- Change directory
- touch --- Create a file in your current directory
- rmdir --- Remove a folder
- rm --- remove a file
- 



# Capture the Flag

Capture the Flag (CTF) is a special kind of information security competition. The goal is to collect passwords, or **flags** to progress. There are three common types of CTFs: Jeopardy, Attack-Defence and mixed.

- Jeopardy-style CTFs has a couple of questions (tasks) in range of categories. For example, Web, Forensic, Crypto, Binary or something else. A team gets some points for every solved task. Generally teams will be awarded more points for more difficult tasks. The next task in the chain will be unlocked after you solve the previous one. The team with the most points when the time is over is the winner. A famous example of this kind of CTF is the DEFCON CTF Qualifier.
- Attack-defence is another interesting kind of competition. Here every team has their own network, with many machines, or a single computer, with vulnarable services. The teams are given an amount of time to patch services and secure the network or system and developing exploits to hack the systems of other teams.  So, then organizers connects participants of competition and the wargame starts! You should protect own services for defence points and hack opponents for attack points. Historically this is a first type of CTFs, everybody knows about DEF CON CTF - something like a World Cup of all other competitions.

Today we are going to do a relatively short Jeopardy-style CTF. The category is Linux, which means that the security aspect of the CTF is not really present. It is more of a way to become more familiar with the terminal and navigation around the Linux file structure. The game consists of 12 levels that are supposed to make you feel a little more comfortable using the Terminal as a tool for the Linux Command Line. The first level is used as an example to show how the game is run.


## Preparing the CTF
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
curl https://home.samfundet.no/~halvogro/ting/teknostart_ctf.zip -O
```

:tip: When you download such a file and then run it, you need to make sure that you know what it contains or trust its origin. The file can run programs that have access to everything on your computer. 


### Step 3: Install and run

With `curl`, you downloaded a zip file. All the files needed for the CTF is here. 

1. Unzip the files by typing `unzip teknostart_ctf.zip`

To be able to run the program we first need to som files.

2. Type `cd teknostart_ctf`to change directory to the folder you just unzipped. 
3. Type `pwd`and confirm that you are inside the `/home/pi/teknostart_ctf`folder. 

Here there are three files that are important for the CTF:
- `teknostart_ctf.py`, which is the actual CTF program, it wil be demostrated later how to use it.
--  This is a terminal based game and is written in the programming language [Python]((https://www.python.org/))
- `levelcheck` is needed for some levels and checks if the tasks has been completed. It prints out the flag if the task has been done correctly. used to retrieve the flag (password) for some levels, where it has to be checked wether you completed the task correctly`
- `install` is an executable program that is only going to be run once to set everything up. 

To run an executable file in the folder that you are currently in, we type `./` followed by the name of the program.
4. Type `./install`to run the installer.

Now we are ready to begin the CTF.

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

In which folder are you located when you open the terminal?

Example answer:      /folder/folder      
Answer given:        None                
Hash of answer:      dc937b59892604f5a86ac96936cd7ff09e25f18ae6b758e8014a24c7fa039e91
Correct hash:        1c4d3877bf4fe64f9d55cdbbf10d9b02c329b2a5a162ae3014b83da8c3024a71
Levelchecker:        NO                  

----------------------------------------

```

- `CURRENT LEVEL` *is the level that you are currently on, this will increase as you progress*
- `Question` *is the task for this level, read it carefully* 
- `Example answer` *is an example answer to give you an idea of what format the answer should be. for instance, when asked about a file name, this example tries to show that we are looking for the full filename, including the file ending `.txt`.*
- `Answer given` *is the answer you gave, which is "None" by default*
- `Hash of answer` *is a hashed version of your answer. The game takes the answer that you put in, does some math on it, and generates a  [string](https://en.wikipedia.org/wiki/String_(computer_science)) which it will try to compare to the hashed version of the correct answer.* 
- `Correct hash` *is the hashed version of the correct answer. If this hash matches the hash of your answer, the answer is correct*
- LevelChecker *Tells you if you have to get check that you done the task correctly.*
-- The value is either `YES` or `NO` for each level. If this says `YES`, it means you have to navigate to `/home/pi/teknostart_ctf`and run `./levelchecker`to check that you have completed the task correctly. If you have you will get the password (flag) to progress to the next level. 


### Step 2: Solve the task

The first you will see is what level you are on, in this case, level 1. As you progress, this will increase. Next is the challenge for this level. This question asks for the folder path that you are in when you each time you launch a new terminal.

First we open a new terminal:
![alt text](https://home.samfundet.no/~halvogro/ting/bilder/image-47.png)

Now, to check which folder location we are in, we type `pwd`

![alt text](https://home.samfundet.no/~halvogro/ting/bilder/image-48.png)

As we can see, we are located in `/home/pi`. 

### Step 3: Check if you got the correct answer

To test our answer, we run the program again and input our answer `/home/pi`.

First we change directory back to where the program `teknostart_ctf.py`is located.

Because we are already inside the folder `/home/pi` we can simply type `cd teknostart_ctf`, which will put us in  `/home/pi/teknostart_ctf`. 

When we now type `ls` to list the files in the directory, we se our `teknostart_ctf.py`file.
![alt text](https://home.samfundet.no/~halvogro/ting/bilder/image-50.png)

We can now run it, and input our answer `/home/pi`.
![alt text](https://home.samfundet.no/~halvogro/ting/bilder/image-52.png)

Success! We had the right flag. The next task is given to us, try to solve that and as many of the following tasks as you can.


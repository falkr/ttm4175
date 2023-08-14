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


# General Overview

The preparations for this unit consist of three parts
    1. **Reading** up on background information about the command line and some basic functions
    2. **Watching** a few videos showcasing the use of those basic commands
    3. **Trying out** the commands on your own machine and learning how to connect to the Virtual Machine (VM) that we'll use in this and upcoming labs


You can complete these parts in any order you prefer, but we suggest setting up your own environment first and experiment with the commands as they come up in the videos and readings.


# 1) Introduction to the CLI and Documentation of Important Commands

[A tutorial introduction to the Unix command line](https://www.learnenough.com/command-line-tutorial)

The **introduction of Chapter 1 along with Sections 1.1, 1.2, and 1.4** (boxes and exercises are optional at this point) provides a broad overview into the topic.

- [Linux directory structure](https://linuxhandbook.com/linux-directory-structure/)


# 2) Videos on Basic Commands for Interacting with Files (Navigation, Manipulation, Search)

An introductory series on basic commands you'll use in the command line environment.

- File system navigation and inspection (`cd`, `ls`, ..)
---
type: youtube
video: j6vKLJxAKfw
---


- File system manipulation (`cp`, `rm`, ..)
---
type: youtube
video: eoejHvAPDFs
---


- Search and match inside files using `grep` (the first five minutes of this are sufficient at this stage)
---
type: youtube
video: VGgTmxXp7xQ
---


- Printing file contents using `cat`
---
type: youtube
video: EKWGioJTMkM
---


- Getting help with `man`
---
type: youtube
video: blFOgzwJbfE
---


- Redirecting command outputs to files using `>` / `>>` and chaining together (*piping*) commands with `|` 
---
type: youtube
video: CE8bukfjOZ4
---


# 3) Practical 

## Setting up a CLI Environment on Your Own Machine

-> subpage Mac-Terminal / Win-WSL



## Connecting to the Remote Lab Virtual Machine (VM)

intro: we can connect to remote machines either via ssh (if we only want to use the CLI) or using graphical tools - you may know TeamViewer - we'll use VNC for that.

disclaimer: you need to be in the NTNU network to connect to the VMs -> either on-site via eduroam or via VPN -> link to NTNU VPN wiki page with instructions

shell and SSH

extend based on [Mac Guide](https://falkr.github.io/ttm4175-2022/shell-mac.html) and [Windows Guide](https://falkr.github.io/ttm4175-2022/shell-win.html)
in both cases: `ssh -V` to check whether ssh is installed


https://learn.microsoft.com/en-us/windows/wsl/install-manual 
https://learn.microsoft.com/en-us/windows/terminal/tutorials/ssh 
https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui#install-openssh-for-windows (we'll only need the client part)


# Additional Resources

- [Commands for getting help](commands-help.html): how to use the `man` and `apropos` commands to get help and information directly on the command line
- [Unix/Linux Command Reference](https://files.fosswire.com/2007/08/fwunixref.pdf): handy overview of many commonly used commands and options
- [explainshell.com](https://explainshell.com/): online tool that parses a given command and provides details on the command itself as well as the provided options / flags / arguments



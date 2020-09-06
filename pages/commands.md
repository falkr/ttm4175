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

# Docker commands

## docker pull <name>

Let's you get an image or repository from a registry (e.g. Docker hub).

## docker ps 

Lists all running containers.
The option `-a` can be used in addition to the command so that all existing containers are shown, even the stopped ones.

## docker images

Lists all locally available images (created or downloaded).

## docker start <container ID/name>

Start one or more stopped containers.

## docker stop <container ID/name>

Stop one or more running containers.

## docker rm <container ID/name>

Remove one or more containers.

## docker rmi <image ID(s)>

Remove one or more images.


## docker build -t <image ID/name>

Build an image from a Dockerfile.

* Docker build vil bygge et docker-image utifra en docker-fil. I docker-filen er det spesifisert et sett med instruksjoner for hvordan imaget skal bli bygget opp. 

* -t er et flagg som sier at vi kan legge til tags til image, her sier vi at docker-image skal hete mittimage. 

* Ved å sette punktum på slutten sier vi at docker-filen ligger i mappen vi allerede er i. Man kan også alternativt spesifisere hele pathen til docker-filen istedenfor punktumet.


## docker run -dit --name <name_of_your_choice> --privileged <image_name_you_want_to_use>

Run a command in a **new** container.

* Docker run starter en prosess i en isolert container som og er bygd ut i fra et image. 
* -dit flagget
* -i står for interactive. 
* -t står for terminal
* -d lar deg kjøre containeren i detached mode. Da kjører den i bakgrunnen av terminalen. 
* --name setter navn på containeren. 
* --privileged setter at containeren har tillatelse til å gjøre endringer på innstillinger som er låst bak tillatelser. (hvis det ikke trenges eller at det står i dockerfilen så har du det ikke med)

:warning:
The privileged flag shouldn't be used unless needed! It opens up the host running Docker to possible attacks from inside the privileged container.


## docker exec -it <container ID/name> bash

Run a command in a **running** container.

* Lar deg komme inn i et interaktivt shell av containeren hvor du kan utføre kommandoer som da skjer inne i containeren.
* Når du går ut av shell, vil containeren stoppe.
* Når du skal bruke id-en til containeren så trenger du ikke å bruke hele bare nok til at den er unik.
* Syntaks: `docker exec -it <container ID/Name> /bin/bash`
    * exec står for execute
    * i står for interactive
    * t står for terminal
    * bash tar deg til mappen bin som ligger under root mappen. Der ligger "programfiler". `bash` er et "program" som ligger i denne mappen og står for Bourne-again shell.

Eksempler:

* `docker exec -it a73450b64455 bash`
* `docker exec -it min-container bash`


## docker run -d --name siteNr2 -p 8081:80 website2

This example shows a `docker run` that exposes port 80 of the container through port 8081 of the host machine using the `-p` option.
This means that in your host machine (localhost or 127.0.0.1) you can open port 8081 to reach services/applications bound/listening to port 80 inside your container.

# Docker Compose

Define and run multi-container applications with Docker.

## docker-compose build

* Bygger images angitt av 'docker-compose.yml' filen.

## docker-compose up -d

* Kjører containerne og nettverkene som er definert i docker-compose.yml filen.
* Syntaks: ‘docker-compose up --build’
 --build bygger imagene på nytt dersom Docker oppdager at det har skjedd en endring i noen av imagene som brukes.
 
## docker-compose down

* Stopper og fjerner containers og nettverkene


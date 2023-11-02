# Password Cracking 

In this lab, you will (1) download and install virtualBox and Kali Linux, and (2) you will learn how to use John the ripper to crack passwords.


# Download and install VirtualBox 

First you need to download VirtualBox and Kali Linux VM, and install Kali Linux on VirtualBox. You can use the following tutorial to do so: 

---
type: link
link: "https://itsfoss.com/install-kali-linux-virtualbox/"
title: "Kali Linux Installation"
icon: gear-wide-connected
---



:task: After successfully installing Kali linux, you are asked to navigate  to the tools that are equipped with Kali linux. What are the different  categories of tools that Kali Linux provide? 


In the rest of the lab you will use one of the tools that are listed under the category "Password Attacks", which is called John, or "John the Ripper". 


# Password cracking with John the Ripper 

In this task you will learn how to read and crack passwords on the Kali machine. You will learn how to use John the Ripper to bypass the password protection applied in Kali.

## John the Ripper

John the Ripper is a cracking tool that runs in both *brute-force* and *dictionary attack* modes. It's basic functionality is to repeatedly try different passwords and hash them until it finds a match. However, since the space of all possible passwords is virtually infinite, testing all password in this manner (brute-force search) will not be feasible unless the password was very short.
Instead, we will try a list of more likely passwords known as *dictionary attack* mode. 

John the Ripper comes with a pre-installed dictionary of some typical passwords located in */usr/share/john/password.lst*.


User accounts are stored in two main files in linux /etc/passwrd and /etc/shadow. 

### /etc/passwd file

The passwd file contains information about all user accounts of the system, without the passwords. Each line represents one user and contains different fields that are separated by ":". Each entry of the /etc/passwrd file looks like 

```
tom:x:1001:1001:,,,:/home/tom:/bin/bash
```

We can see that the entry consists of 7 fields, which are 
1. username `tom`
2. password `x` means that the encrypted password is stored in the /etc/shadow file
3. user id (UID), which is the uid of the user, in this case it is: 1001
4. group id (UID), which is the gid of the user, in this case it is: 1001
5. user id information (comment), which is an extra information about the user, in this case it is empty `,,,`
6. home directory: /home/tom
7. shell: the path to the shell

### /etc/shadow file
The shadow file contains secure information about all user accounts of the system. Each line represents one user and contains different fields that are separated by `:`. Each entry of the /etc/shadow file looks like

```
tom:$y$j9T$tdzhkxe2roboPaji2GMzh.$jbAYYu0KutRWoGWPcN5PfAL8llhIzPGUFbfS5nKAja6:19662:0:99999:7:::
```

We can see that an entry consists of 6 fields: 
1. username `tom`
2. password `$y$j9T$tdzhkxe2roboPaji2GMzh.$jbAYYu0KutRWoGWPcN5PfAL8llhIzPGUFbfS5nKAja6`. The password field has the following format: `$id$param$salt$hashed`. "id" indicates the algorithm id which has the following values: 
`$1$` means MD5, `$2a$` means Blowfish,... `$5$` means SHA-256, `$6$` means  SHA-512, and `$y$` means YESCRYPT. 
The above password indicates that the algorithm used is Yescrypt, the parameter is `j9T`, the salt is `tdzhkxe2roboPaji2GMzh.`, and the encrypted/hashed password is `jbAYYu0KutRWoGWPcN5PfAL8llhIzPGUFbfS5nKAja6`
3. lastchange, which indicates when the password was changed last. The number indicates the number of days since 01.01.1970. In this case, it is 19662 days. 
4. minimum number of days to change the password, which is 0
5. maximum number of days to change the password, which is 99999
6. when user is to be warned about the change of the password, in terms of number of days before it will expire. 
7. when the account will be disabled
8. expiration date


### Investigate /etc/passwd and /etc/shadow files

The first task is now to investigate the /etc/passwd and /etc/shadow files for users on the Kali system. 

**Step 1: Reading the files:** For reading the files you can runt he following commands:

```bash
sudo cat /etc/passwd
```

```bash
sudo cat /etc/shadow
```

Please study the files and try to understand their format and content.

**Step 2: Combining passwd and shadow files:** Combining both files in one file is useful for cracking. To do this you use the "unshadow" command, like this:

```bash
cd /home/kali/Desktop 
sudo unshadow /etc/passwd /etc/shadow > passwords
```

This will combine both files in one file, called "passwords", and it will be stored it in the Desktop. 

To read the new file run

```bash
cat passwords
```

Please study the content and the format of the new file.  


**Step 3:** Add two new users to Kali and repeat tasks 1 and 2 again. 

In this task we will add two users, the first (tom) with an easy password, that can be find in a dictionary, and the second (ric) with non trivial password. 

You can add the users using the "adduser" commmand:

```bash
sudo adduser tom
```
(Set new password to password)

```bash
sudo adduser ric
```
(Set new password to ka1i) Please note that the third character of the password is the number one "1". 
	
Now, repeat tasks 1 and 2 and check the difference in the passwd and shadow files. 


### Default dictionary

Start by running John the Ripper on our obtained Windows 7 hash file with the default dictionary, using the following command:

```bash
john --wordlist --format=crypt  --user='kali'
```

This command tells John to use a dictionary attack (–-wordlist) with words from the default dictionary */etc/share/john/password.lst*; using the hash function yescrypt (–-format=crypt); targeting user "kali"; and where the target hashes are stored "passwords" file.
 
To show the passwords that are already cracked from previous invocations on the "passwords" file, you run

```bash
john -show passwords
```

:task: Repeat the same command for the 2 other users that you created. Did John the Ripper succeed in guessing all passwords?


### Creating new passwords from existing ones
Instead of using a larger dictionary, John the Ripper can apply a multitude of transformations to a wordlist in order to create new passwords from existing ones. For example, we could make it append numbers to the end of all the words in the dictionary, such that if the word "car" was in the original dictionary, then it would also try *car0* , *car1*, ..., *car 9*, *car00*, *car01*, ..., etc.

These transformations are defined by a set of rules found in the configuration file */etc/john/john.conf*.

+ Open the config file /etc/john/john.conf using nano, vim, or any text editor application you prefer. 

+ Scroll down to the line containing "[List.Rules:Wordlist]". 

Every line underneath contains a transformation rule which will be applied to every word of the dictionary. First comes zero or more rejection rules, all starting with a hyphen, e.g. -c, -8, -s, etc. These are used to decide whether the rest of the transformation rules on the line should be applied to a word or not. You can just ignore these. 

Next come the actual transformation rules themselves. For example the rule: ` <5 c r Q` 

It applies to words of length less than 5 *( <5 )* ; and if so, it will capitalize *( c )* and reverse *( r )* it. The *Q* command ensures that words that are not changed won't be unnecessarily added to the dictionary, avoiding duplicates (e.g. capitalizing an already capitalized word does not change it).

For example, if "car" was in the dictionary, then the above rule would make John the Ripper also try the word *raC*; that is by checking first if the word's length is less than 5, then capitalizing it to get *Car*, and finally reversing it to get the result *raC*. 

:task:Your task now is to create a rule that applies to all words that are longer than 1 and less than 7, and replaces all appearances of lowercase "L" with the number "1". For example, if the word "hello" was in the dictionary, then "he11o" would also be added.

:tip:
Use the command "s" to substitute a letter by another. For example, *so0* substitutes letter "o" with a zero.
The description of every possible transformation rule can be found on the [John the Ripper web page.](http://www.openwall.com/john/doc/RULES.shtml)


+ To check how the default rules work, create a dictionary file *test.dict* containing the single word "labrador" `# echo "labrador" > test.dict`

+ Apply the default John rules to * test.dict * and print the results as follows: `# john --worldlist=test.dict --rules --stdout`

+ To find out how many new password did John create from this single-word dictionary, pipe the output above with '|' into *wc*.  




# Final Steps

### Learning Goals

In your double-team, reflect about what you learned today. Write a few sentences that capture (in your own words) what you learned and why it can be useful. Share these few sentences with everyone in the double-team.


### Individual Reflection

We recommend that you take some time to consider if there are any parts of this unit that you want to repeat individually, at your own pace. If you decide to do so, please perform the tasks you want individually and write your own individual reflection. 


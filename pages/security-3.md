# Password clearing and cracking 

In this lab, you will learn how to clear a password in Windows and how to use ophcrack and John the ripper to crack passwords.

# Clearing the user password in Windows
In the previous lab, you had to swap the system files in order to change the user's password. Another alternative that you will try now is to clear the password. 
## Updating chntpw

Passwords in Windows are stored hashed in the Security Accounts Manager (SAM) database, located in the */Windows/System32/config* folder. We will manipulate the SAM registry in order to clear the hashed password of user **Lab2**.
SAM file is stored in a binary format and cannot simply be read by a text editor. We will use a program called *chntpw* in order to clear the users password from the SAM file.

+ Make sure that Windows 7 is mounted within Kali, then go to the following folder containing the SAM file:

`# mount /dev/sdb2 /mnt/windows`

`# cd /mnt/windows/Windows/System32/config`

`# ls`
+ Start *chntpw* in interactive mode by using *-i* flag option and read in the SAM file
`#chntpw -i sam` (The SAM file is stored either in uppercase or in lowercase so choose the name that is used on your system).

+ Follow the on-screen instructions. Select option 1 to begin clearing a user password (the number in square brackets denotes the default).
+ We want to clear the password of user **Lab2**, so enter its RID 
+ Choose option 1 again to clear the password of user **Lab2**  
+ Write changes to disk by quitting the current context (q) and confirm that you want to save the changes (y). You have now cleared the password of **Lab2** user.

Finally, return to your home folder `# cd ` and unmount the Windows partition from kali Linux `# unmount /mnt/windows`.
Reboot the machine and select Windows 7. You should now be able to login into **Lab2** account without a password.


# Cracking the Windows 7 user password
Start by creating 5 user accounts in Windows for which you will try to crack the passwords.
## Create new users in Windows
+ Get administrator access: follow the same steps from part 1 of the previous lab (attach Windows 7 to Kali in virtual box, then mount the Windows 7 partition within Kali and swap *osk.exe* and *cmd.exe*) in order to get administrator access
+ Create 5 users: **Lab10**, **Lab20**, **Lab30**, **Lab40**, and **Lab50** and assign a different password to each user. For the first two users, assign a commonly-used password (you can search the web for the list of top 10,000 most common passwords). For the remaining users, choose passwords that are considered strong.

:hint:

Use the `net user` command to create a new user    

+ Remember to revert the changes you made on *osk.exe* and *cmd.exe* files.  



## Obtaining the password hashes

Your task now is to **obtain** the password hashes stored in the SAM database. We need to use Kali with the Windows 7 partition mounted. Make sure that you have the Windows 7 disk attached to your Kali Linux virtual machine.

+ Locate the SAM database by changing to the *Windows/System32/config* directory

:hint:

`cd /mnt/windows/Windows/System32/config/`

`ls`

In order to enhance the security of the SAM database against off-line attacks, Microsoft introduced the Syskey function, which partially encrypts the SAM database based on a key stored in another registry file called SYSTEM. Hence you need to extract the contents of both the SYSTEM file and the SAM file. Both are stored in a binary format and are not readily readable. 

+ Use the tool *samdump2* to extract the content of the SYSTEM file and the SAM file, and write the contents to *win_pwd_hashes.text* `# samdump2 system sam > ~/win_pwd_hashes.txt`

`# cd ~ ` 

## Examining the SAM database

+ Take a look at the content of the *win_pwd_hashes.text*  `# cat win_pwd_hashes.txt`. Each line entry represents a user account on the system with their respective hashes.

## Examining the SAM database in Ophcrack

Ophcrack is a program that comes with a graphical user interface that allows you to see the format of the passwords in the SAM database.
+ Open Ophcrack by running *ophcrack* in the terminal of your Kali Linux machine
+ Click on Load ->PWDUMP file
+ Find the file *win_pwd_hashes.txt*. It will show you the hashed passwords.
+ try the Crack functionality on the available users. Did it succeed in cracking all passwords?

## John the Ripper
John the Ripper is a cracking tool that runs in both *brute-force* and *dictionary attack* modes. It's basic functionality is to repeatedly try different passwords and hash them until it finds a match. However, since the space of all possible passwords is virtually infinite, testing all password in this manner (brute-force search) will not be feasible unless the password was very short.
Instead, we will try a list of more likely passwords known as *dictionary attack* mode. 

John the Ripper comes with a pre-installed dictionary of some typical passwords located in */usr/share/john/password.lst*.


### Default dictionary

+ Start by running John the Ripper on our obtained Windows 7 hash file with the default dictionary, using the following command (note the use of single quotes around the username): ` # john --wordlist --format=NT --user='Lab 3 - DO NOT WIPE!' win_pwd_hashes.txt` 

This command tells John to use a dictionary attack (–-wordlist) with words from the default dictionary */etc/share/john/password.lst*; using the hash function NTLMv2 (–-format=NT); targeting user Lab 3 - DO NOT WIPE! (–-user=...); and where the
target hashes are stored in win_pwd_hashes.txt. 

If the output of John the Ripper shows 0 guesses, it means the password is not contained in the default dictionary and it could not be cracked.

+ Repeat the same command with the 5 users that you created. Did John the Ripper succeed in guessing all passwords?

### Creating new passwords from existing ones
Instead of using a larger dictionary, John the Ripper can apply a multitude of transformations to a wordlist in order to create new passwords from existing ones. For example, we could make it append numbers to the end of all the words in the dictionary, such that if the word "car" was in the original dictionary, then it would also try *car0* , *car1*, ..., *car 9*, *car00*, *car01*, ..., etc.

These transformations are defined by a set of rules found in the configuration file */etc/john/john.conf*.
+ Open the config file by running `leafpad /etc/john/john.conf & ` from the terminal.
+ Scroll down to the line containing "[List.Rules:Wordlist]". 

Every line underneath contains a transformation rule which will be applied to every word of the dictionary. First comes zero or more rejection rules, all starting with a hyphen, e.g. -c, -8, -s, etc. These are used to decide whether the rest of the transformation rules on the line should be applied to a word or not. You can just ignore these. 

Next comes the actual transformation rules themselves.

For example the rule: ` <5 c r Q` 

It applies to words of length less than 5 *( <5 )* ; and if so, it will capitalize *( c )* and reverse *( r )* it. The *Q* command ensures that words that are not changed won't be unnecessarily added to the dictionary, avoiding duplicates (e.g. capitalizing an already capitalized word does not change it).

For example, if "car" was in the dictionary, then the above rule would make John the Ripper also try the word *raC*; that is by checking first if the word's length is less than 5, then capitalizing it to get *Car*, and finally reversing it to get the result *raC*. 

+ Your task now is to create a rule that applies to all words that are longer than 1 and less than 7, and replaces all appearances of lowercase "L" with the number "1". For example, if the word "hello" was in the dictionary, then "he11o" would also be added.

:hint:

use the command "s" to substitute a letter by another. example *so0* substitutes letter "o" with a zero

The description of every possible transformation rule can be found at the John the Ripper web page http://www.openwall.com/john/doc/RULES.shtml

+ To check how the default rules work, create a dictionary file *test.dict* containing the single word "labrador" `# echo "labrador" > test.dict`
+ Apply the default John rules to * test.dict * and print the results as follows: `# john --worldlist=test.dict --rules --stdout`
+ To find out how many new password did John create from this single-word dictionary, pipe the output above with '|' into *wc*.  




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

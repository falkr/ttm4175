# Password clearing and cracking 

In this lab, you will learn how to clear a password in Windows and how to use ophcrack and John the ripper to crack passwords.

# Create user accounts in Windows 7 

+ Start the Windows 7 VM and log in with the user **Lab4** (no password is required).

+ Go to "Control Panel" and create four standard user accounts **user1**, **user2**, **user3**, and **user4**. Assign a different password to each of the users. For the first two users, choose one of the commonly-used password. Here you can find a [list of the most common passwords](https://en.wikipedia.org/wiki/List_of_the_most_common_passwords). For the remaining users, choose stronger passwords that are of different lengths, with and without special characters. 

+ Shut down the Windows VM

# Clearing the user password in Windows

In the previous lab, you had to swap the system files in order to change the user's password. Another alternative that you will try now is to clear the password. 

## Updating chntpw

Passwords in Windows are stored hashed in the Security Accounts Manager (SAM) database, located in the */Windows/System32/config* folder. We will manipulate the SAM registry in order to clear the hashed password of user **Lab2**.
SAM file is stored in a binary format and cannot simply be read by a text editor. We will use a program called *chntpw* in order to clear the user's password from the SAM file.

+ Make sure that Windows 7 is mounted within Kali. Log in to Kali with **root** account, and go to the following folder containing the SAM file:

```bash
mount /dev/sdb2 /mnt/windows
cd /mnt/windows/Windows/System32/config
ls
```

+ Start *chntpw* in interactive mode by using *-i* flag option and read in the SAM file
```bash
#chntpw -i sam (The SAM file is stored either in uppercase or in lowercase so choose the name that is used on your system).
```
+ Follow the on-screen instructions. Select option 1 to begin clearing a user password (the number in square brackets denotes the default).

+ We want to clear the password of user **Lab2**, so enter its RID 

+ Choose option 1 again to clear the password of user **Lab2**  

+ Quit the current context (q), then quit the main menu (q), and confirm that you want to save the changes (y). You have now cleared the password of **Lab2** user.

Finally, return to your home folder `# cd ` and unmount the Windows partition from kali Linux `# umount /mnt/windows`.

Reboot the machine and select Windows 7. You should now be able to login into **Lab2** account without a password.


# Cracking the Windows 7 user password

## Obtaining the password hashes

Your task now is to **obtain** the password hashes stored in the SAM database. We need to use Kali with the Windows 7 partition mounted. Make sure that you have the Windows 7 disk attached to your Kali Linux virtual machine.

+ Mount Windows 7 into Kali and locate the SAM database by changing to the *Windows/System32/config* directory

```bash
mount /dev/sdb2 /mnt/windows
cd /mnt/windows/Windows/System32/config
ls
```


In order to enhance the security of the SAM database against off-line attacks, Microsoft introduced the Syskey function, which partially encrypts the SAM database based on a key stored in another registry file called SYSTEM. Hence you need to extract the contents of both the SYSTEM file and the SAM file. Both are stored in a binary format and are not readily readable. 

+ Use the tool *samdump2* to extract the content of the SYSTEM file and the SAM file, and write the contents to *win_pwd_hashes.text* 

```bash
samdump2 system sam > ~/win_pwd_hashes.txt
cd 
```

## Examining the SAM database

+ Take a look at the content of the *win_pwd_hashes.text*  `# cat win_pwd_hashes.txt`. Each line entry represents a user account on the system with their respective hashes.


## Examining the SAM database in Ophcrack

Ophcrack is a program that comes with a graphical user interface that allows you to see the format of the passwords in the SAM database.

+ Open Ophcrack by running `ophcrack` in the terminal of your Kali Linux machine

+ Click on Load ->PWDUMP file

+ Find the file *win_pwd_hashes.txt*. It will show you the hashed passwords.

+ try the Crack functionality on the available users. Did it succeed in cracking any of the passwords?


## John the Ripper

John the Ripper is a cracking tool that runs in both *brute-force* and *dictionary attack* modes. It's basic functionality is to repeatedly try different passwords and hash them until it finds a match. However, since the space of all possible passwords is virtually infinite, testing all password in this manner (brute-force search) will not be feasible unless the password was very short.
Instead, we will try a list of more likely passwords known as *dictionary attack* mode. 

John the Ripper comes with a pre-installed dictionary of some typical passwords located in */usr/share/john/password.lst*. Open the pre-installed dictionary of John the Ripper and check its content.

### Default dictionary

+ Start by running John the Ripper on our obtained Windows 7 hash file with the default dictionary, using the following command (note the use of single quotes around the username): 
```bash
# john --wordlist --format=NT --user='user1' win_pwd_hashes.txt
```

This command tells John to use a dictionary attack (–-wordlist) with words from the default dictionary */etc/share/john/password.lst*; using the hash function NTLMv2 (–-format=NT); targeting user **user1** (–-user=...); and where the target hashes are stored in win_pwd_hashes.txt. 

If the output of John the Ripper shows 0 guesses, it means the password is not contained in the default dictionary and it could not be cracked.

+ Repeat the same command for the 3 other users that you created. Did John the Ripper succeed in guessing all passwords?

:tip:

Note that in the case where the password is not simple or didn't exist in John's dictionary, then you would need a much bigger dictionary and a lot longer time to crack it. You can use your own password lists or download a large one from Internet (there’s lots of dictionary file in terabyte size).

### Creating new passwords from existing ones

Instead of using a larger dictionary, John the Ripper can apply a multitude of transformations to a wordlist in order to create new passwords from existing ones. For example, we could make it append numbers to the end of all the words in the dictionary, such that if the word "car" was in the original dictionary, then it would also try *car0* , *car1*, ..., *car 9*, *car00*, *car01*, ..., etc.

These transformations are defined by a set of rules found in the configuration file */etc/john/john.conf*.

+ Open the config file by running `leafpad /etc/john/john.conf & ` from the terminal. (If you don't have leafpad installed in Kali, run the following command to install it `apt-get install leafpad`).

+ Scroll down to the line containing "[List.Rules:Wordlist]". 

Every line underneath contains a transformation rule which will be applied to every word of the dictionary. The rules starting with a hyphen, e.g. -c, -8, -s, etc are used to decide whether the rest of the transformation rules on the line should be applied to a word or not. You can just ignore these. 

The actual transformation look like this one: ` <5 c r Q` 

This rule applies to words of length less than 5 *( <5 )* ; and if so, it will capitalize *( c )* and reverse *( r )* it. The *Q* command ensures that words that are not changed won't be unnecessarily added to the dictionary, avoiding duplicates (e.g. capitalizing an already capitalized word does not change it).

For example, if "car" was in the dictionary, then the above rule would make John the Ripper also try the word *raC*; that is by checking first if the word's length is less than 5, then capitalizing it to get *Car*, and finally reversing it to get the result *raC*. 

+ Your task now is to create a rule that applies to all words that are longer than 1 and less than 7, and replaces all appearances of lowercase "L" with the number "1". For example, if the word "hello" was in the dictionary, then "he11o" would also be added. Use the command "s" to substitute a letter by another (example *so0* substitutes letter "o" with the number 0).

<button class="w3collapsible">Hint</button>
<div class="w3content">

The rule that you want to define will be: >1 <7 sl1 Q
</div>


Take a look at the [John the Ripper web page](http://www.openwall.com/john/doc/RULES.shtml). The description of every possible transformation rule is provided.


+ To check how the default rules work, create a dictionary file *test1.dict* containing the single word "labrador" `# echo "labrador" > test1.dict`

+ Apply the default John rules to *tes1t.dict* and print the results as follows: `# john --wordlist=test1.dict --rules --stdout`

+ How many new passwords did John create from this single-word dictionary? find out by piping the output above with '|' into *wc*. 

:tip:

The *wc* command will display the following three numbers: number of lines, number of words and number of bytes of the file.  


+ Similarly, create a dictionary *test2.dict* containing the word "hello" and apply the default John rules to it. Does the file contains the word "he11o" as a result of the rule that you added earlier? Why hasn't this rule been applied to the word "labrador"?

### Cracking password in Linux

+ In Kali Linux, create a user named **kuser** and assign a simple password to it (choose a password from the common passwords list)

+ Use the *unshadow* command to combine the entries of */etc/passwd* and */etc/shadow* to create 1 file with username and password details. Redirect the output to */root/kuser_passwd*

```bash
 unshadow /etc/passwd /etc/shadow > /root/kuser_passwd
```

+ Run John the Ripper on the obtained file

```bash
john --wordlist=/usr/share/john/password.lst /root/kuser_passwd 
```

+ If the password was cracked, we can now use john –show  option to list cracked passwords

```bash
john --show /root/kuser_passwd 
```

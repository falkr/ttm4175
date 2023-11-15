# Security 2

In this lab you will learn about two phases in the penetration testing process, which are information gathering and scanning. The lab is divided into two parts, one for each step. 

# Information Gathering

In this part you will gather information about the target you want to pentest.
Let us assume that you are planning to conduct a penetration test on NTNU servers.
The first task is to collect as much information as you can about the ntnu domain.
This includes gathering information about IP addresses, web servers, mail servers, DNS servers, and other information like subdomains, email addresses, etc.
We will use few tools that come in Kali to allow you to do "PASSIVE" reconnaissance. 



## theHarvester

heHarvester is a  tool to perform reconnaissance stage open source intelligence (OSINT) gathering to help determine a domain's external threat landscape.
The tool gathers names, emails, IPs, subdomains, and URLs by using multiple public resources.
You can [learn about the tool here](https://www.kali.org/tools/theharvester/#tool-documentation).
In order to gather information about ntnu, limiting the results to 200 hits and to use "all" search engines, you can run the following command: 

```bash
theHarvester -d ntnu.no -l 100 -b all 
```

After you run this command, study the output of the command and what type of information you got from it.


## Whois Lookup

The next tool is "Whois" that can also be used in the information gathering and reconnaissance phase.
The tools allows you to get information like  server name registrar, addresses, phone numbers, organization handles, URL, and others.
Whois can be given an IP address of a site name.
Run the following commands.
Note that the IP address used in the second one is one of the IP addresses that we got from the last task:

```bash
whois ntnu.no
```

```bash
whois 129.241.106.103
```

Do you see any difference in the output? What type of information did you get?

## DNS Enumeration

"dnsenum" is a reconnaissance tool that gather extensive information about a domain.
For example, the host’s addresses, the namservers, mail servers, extra names and subdomains, calculated C class domain network ranges, reverse lookups on netranges. For more information you can see:

---
type: link
link: "https://www.kali.org/tools/dnsenum/"
title: "Kali Linux Dnsenum Documentation"
icon: file-earmark-text
---


Run the following command and study the results that you get:

```bash
whois 129.241.106.103
```

Is there any overlap with the information you get from the other tools?

## Spiderfoot 

SpiderFoot is a comprehensive and powerful OSINT automation tool.
It integrates many data sources available and utilises a range of methods for data analysis. 
Spiderfoot comes with web UI that can help you to use the tool.
To lunch the web UI, run the following command:

```bash
spiderfoot -l 127.0.0.1:6000
```

Then open a browser and go to `127.0.0.1:6000`, or `localhost:6000`. 
This will open the user interface.
Click on "New Scan", and you will be asked to give a "Scan name" and "Scan Target".
The scan name can be any name you give it for your scan, let us call it "NTNU scan".
The scan target can be of the following types: 

```
Domain Name: e.g. example.com
IPv4 Address: e.g. 1.2.3.4
IPv6 Address: e.g. 2606:4700:4700::1111
Hostname/Sub-domain: e.g. abc.example.com
Subnet: e.g. 1.2.3.0/24
Bitcoin Address: e.g. 1HesYJSP1QqcyPEjnQ9vzBL1wujruNGe7R
E-mail address: e.g. bob@example.com
Phone Number: e.g. +12345678901 (E.164 format)
Human Name: e.g. “John Smith” (must be in quotes)
Username: e.g. “jsmith2000” (must be in quotes)
Network ASN: e.g. 1234
```

You can specify the scan (1) by use case, (2) by required data, and (3) by module. 
If you want a fully passive mode, then you have to choose, "Passive" use case. "All" will search everything, but the scan will be active and your identity/node will be disclosed in the scan. There are the options footprint, or investigate that are less intensive.  Regarding using modules, you will need to provide keys for some modules. There is information about how to get the keys for each module in the module tab. In most cases you will be required to create accounts in the module provider and get a key form the them. In this lab you do not have add any keys. 

Now we want to run a scan on the ntnu.no website. For that reason we will provide the following domain name as a target "ntnu.no". Try first to run a passive scan on the target. Then later try both investigate and footprint modes. 

The output of the scan can be viewed in various format, like tabular and graph. go through the results and study the various types of information that you received. 


You can find more information about spiderfoot here:
* <https://null-byte.wonderhowto.com/how-to/use-spiderfoot-for-osint-gathering-0180063/>
* <https://medium.com/@itdanny/spiderfoot-v4-0-0-open-source-f71c34d6a06>
* <https://www.youtube.com/watch?v=cimJbdn-8rg>



# Vulnerability Scanning

In this part you will gain remote access to a machine and scan it for vulnerable services.
Next week we will exploit those services.

## Installing Metasploitable

Metasploitable is an intentionally vulnerable virtual machine. It runs Linux and has a variety of configured or outdated services running (web server, FTP server, etc). We will be using it as a target for vulnerability scanning in this lab. 
Follow the following tutorial to import and install Metasploitable 2 in your VirtualBox. 


---
type: link
link: "https://www.geeksforgeeks.org/how-to-install-metasploitable-2-in-virtualbox/"
title: "How to install Metasploitable 2 in VirtualBox"
icon: file-earmark-text
---


## Configuring a virtual network

In this lab, your Kali machine will run on the same local area network (LAN) as the vulnerable Metasploitable machine. 
To connect our machines, we will use the networking mode called “Host-only networking” which allows us to completely separate our guest machines from the outside world while still being connected together in a (virtual) LAN. In this mode, VirtualBox functions as a virtual switch so that all virtual machines that use this mode appear to be on the same LAN. Moreover, no traffic can come from, or escape to, the outside world (i.e., the Internet).


## Attach Metasploitable machine and Kali to the LAN

+ Attach the Metasploitable machine to the LAN. Go to “Settings -> Network” and select “Host-only Adapter” from the drop-down menu. Make sure no other network adapters are attached. This way the Metasploitable will only be able to access the LAN and not the Internet.

+ Do the same for the Kali machine, but add a second adapter as well. Choose “NAT” for this adapter. Having two adapters attached to the Kali machine allows us to both access the LAN and the Internet, which we will need later to download and update some tools.

+ Now boot up both machines in VirtualBox and log in to them. The default username/password combination for Metasploitable is *msfadmin/msfadmin*.

+ Verify that both machines are on the same LAN


By default, VirtualBox will only allow IP addresses in the 192.68.56.0/21 range. This means both Kali and metasploitable will get an address within that range. Let us assume that Kali got the address 192.168.56.3 and metasploitable got the address 192.168.56.4.  Run the command *ifconfig* on both machines and make sure that both belong to the same network.


# Discovering hosts with Nmap

Consider the scenario where an attacker has just joined the network with no prior knowledge of the other connected machines. The first thing we want to know is how many hosts are connected and what their IP-addresses are. To gather this information we will use Nmap (Network Mapper).

Use the following command to scan the network with Nmap and discover the machines that are "live" and the services they are running: 

```bash
# nmap -sn 192.168.56.1/24`
```


`-sn` tells Nmap not to do a port scan after host discovery. 
Note that the IP-address is written with a slash and a number at the end.
Since we don’t know which IP-address the victim machine has, we want to scan a range of addresses.
To do so we use subnet mask. Here we are masking 24 out of 32 bits, which means that 32−24 = 8 bits are unmasked and we get 2^8 = 256 different host-addresses. Therefore, Nmap will scan the range 192.168.56.1-192.168.56.255 and look for live hosts.

The scan will return few IP-addresses, which include the default gateway and the DHCP server provided by VirtualBox, as well as Kali’s IP address and the last one is the victim’s.

# Data collection

Now that we know the IP-address of the potential target, the next step is to gather more information about it.

## OS detection

The first thing we want to know about a newly discovered host is what operating system it’s running. Different operating systems have different vulnerabilities so knowing which one we are dealing with will be crucial to the success of our attack. 

Since network protocols are standardized, the operating systems are supposed to send the same messages over the network. Fortunately, the operating systems have slightly different implementations of the network stack and therefore send network packets with slightly different time intervals between them. By analyzing these patterns, it’s possible to make a good guess as to which OS is sending the packets. Nmap has this functionality built in.

Run Nmap with the "-O" flag to use the OS detection functionality:

```
# nmap -O <IP_address_victim_machine>
```

If the scan was successful the last few lines that the command returns will have information about the OS of the victim machine.

## Port scanning

The next step is to know which services the victim machine is running. The quickest way to find running services is by trying to connect to them. This is known as port scanning and involves trying to connect to all the ports on a remote system and see which ones give a meaningful reply back. By interpreting the reply, it’s possible to figure out which server is listening to the port.

Kali has several tools for port scanning, but we will use Nmap. By default, Nmap only scans the top 1000 most popular ports. We want as much information as possible, so we tell Nmap to scan all TCP-ports:

```
# nmap -p 0-65535 -sV <IP_address_victim_machine>
```


The `-sV` flag makes Nmap try to figure out the version of the services it has discovered. This scan is quite comprehensive, so it will take a few minutes to complete. The obtained results will show the running services and their versions.

# Finding vulnerabilities

Now that we know some basic information about the victim, we can start looking for vulnerabilities with the help of a vulnerability scanner. A vulnerability scanner has a database of known configuration problems and exploits, that it tests against a remote machine. It then generates a report that shows the systems security problems and (sometimes) how to fix them.

## Installing Nessus

We are going to use Nessus, a widely used vulnerability scanner, to scan the victim machine. Kali dosen’t come with Nessus by default, so we must install it. 

- Start by going to the Nessus download page https://www.tenable.com/downloads/nessus (open it in Firefox inside the Kali virtual machine). 
- Download the 64-bit file for Debian/Kali (the one with AMD64 in the name). 
- After it has downloaded, open a terminal and run the following commands:

```bash
cd Downloads
sudo dpkg -i Nessus-8.7.1-debian6_amd64.deb
/etc/init.d/nessusd start
```

:aside: You can also see [this short tutorial for help](https://www.youtube.com/watch?v=TbpfX07NoV4)


Nessus will now start its web interface on port 8834. To access it, point your web browser to `https://localhost:8834`. You will get a warning saying that your connection is insecure. This is because Nessus uses HTTPS with what’s called a “Self-signed certificate”. These certificates are not part of the “Chain-of-trust” and thus the browser cannot verify that the server is who they claim they are. In our case, the kali machine is the server and we are just connecting to our own machine, so we can safely ignore the warning. Click “Advanced” -> “Add exception” to add an exception for Nessus and continue connecting.

:aside:If you ever see a similar warning while browsing the Internet normally, be extremely careful. It could mean that someone is tampering with your traffic!


+ Nessus will start downloading and installing plugins used to check for vulnerabilities. 

## Starting a scan

Click "New Scan" and then "Basic Network Scan". Enter the IP-address of the victim in the "Targets" field, and name the scan "Metasploitable". You don’t need to provide a description. Click the dropdown arrow and select "Launch" to start the scan.

The scan will take a few minutes to complete. You can check the progress by selecting the scan under "My Scans". Once vulnerabilities are found they will appear under the "Vulnerabilities" tab.

## Analyzing the results

Once the scan has finished, a breakdown of the discovered vulnerabilities will be displayed. Vulnerabilities are grouped by how serious they are. Red means critical, orange means high and so on. Click on a vulnerability to show more information about that specific vulnerability, including suggested remedies and sometimes which tools can be used to exploit the vulnerability.

Save the results so you can use them later when looking for appropriate exploits next week. 


# Final Steps

### Learning Goals

In your double-team, reflect about what you learned today. Write a few sentences that capture (in your own words) what you learned and why it can be useful. Share these few sentences with everyone in the double-team. (You should use this text in the individual reflection below.)
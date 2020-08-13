# Terminal and SSH on Macs


The macOS operating system is based on UNIX, which makes it in many respect similar to Linux, at least for the inner workings. The graphical user interface, the desktop and the apps are of course different.

For this reason, macOS already comes with a terminal and you can use many of the commands we use on Linux also on a Mac. You can find it in the folder `Applications/Utilities`. Just open it as you would with any other application.

---
type: figure
source: figures/terminal/terminal-mac-1.png
caption: ""
---

You should then see a terminal window:


---
type: figure
source: figures/terminal/terminal-mac-2.png
caption: ""
---


In this terminal, you can use ssh as on Linux, with the ssh command. 

```bash
ssh pi@<remote_ip_address> -p <port>
```
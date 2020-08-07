# Terminal and SSH in Windows


A current installation of Windows already has a terminal and SSH installed. Open the windows menu, and type `power` to find the Windows PowerShell. Open it as an administrator.

---
type: figure
source: figures/terminal/terminal-win-1.png
caption: ""
---

You should see a terminal window opening.

---
type: figure
source: figures/terminal/terminal-win-2.png
caption: ""
---

Type the following command: 

```bash
Get-WindowsCapability -Online | ? Name -like 'OpenSSH*'
```

If SSH is installed, you'll see something like the following:

---
type: figure
source: figures/terminal/terminal-win-3.png
caption: ""
---


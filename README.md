# TELPOT  
### Capturing Cyber Attacks with generic Telnet Based Honeypot :
This is an implementation of a _simple telnet based Honeypot_ named as **TELPOT**, which consists of a simple echo-server and a proxy written in twisted-python. It's also tested using TELNET_SERVER in place of echo-server. It was deployed in a remote machine having a **public IP** in Digital Ocean.
It had the functionality that, it will show a fake login system to the attacker with an attractive banner. The attacker can make unlimited atttempts to try different passwords. While the attacker is trying to connect to it, this Honeypot will be logging his **IP address**, **port nuumber**, **the date and time** of his login and the **attempts** that the attackers have made with different **passwords**.  
There are two extra directories, one is **IP_PORT** which will contain files according to Date which will store all the IPs and Ports captured at that particular Date. Same will be another directory named **UNAME_PASS** which will contain files storing the username and passwords attempted by the attackers.  And **log_directory** will keep all the logs (scripts) sent by the attacker to compromise my system.
This whole record was accessed remotely through the _specially-designated directory_ **Data Volumes** as it can be seen in the docker-compose file.

**Why TELPOT is differnet from others:**
-> The _docker-compose_ file will run the echo-server at the backend. However , that can be easily replaced by any other server of our own choice. There is another directory TELNET_SERVER which contains the Dockerfile for running Telnet-Server. That was also tested with TELPOT.
This TELPOT is generic and easy to modify accordingly.

_Read below for more information_
---------------------------------------------------------------------------------------------------------------------------------
**Telpot - Capturing Cyber Attacks with generic Telnet Based Honeypot**

MAZHAR IMAM KHAN

Intern from:  Indian Institute of Engineering Science and Technology, Shibpur

Abstract: A honey-pot is a deception toolkit, designed to hook an attacker attempting to compromise the production systems of any institute/organization. If designed and deployed correctly, a honey-pot can function as an advance surveillance tool as well as a threat intelligence collection mechanism. It can also be used to analyze the behavioral signature of the attackers trying to compromise a system and to provide useful insights into potential system loop-holes. This presentation(Link given below), consists of a Telnet Honeypot which acts as an IOT device whose image is built by own customized builds. The honeypot will be capable of recording plenty of information about the attacker, including interactive TTY sessions recordings. All the attacks will be logged which will help me to do active attack payload analysis to find common patterns and gain intelligence. It will actually store the attempted login usernames and passwords in separate files and even the timing of the session will be recorded. It will also record all the logs of the attacker in separate files. In addition to this, the recorded passwords and usernames and all the captured IPs are shown visually using ELK. 
The major contributions in this project work includes:

1.  Lightweight model of Honeypot using C, Python and Twisted Python.

2. Integrating the project with ELK.

3. Capturing the drive-by-download based attacks and analysing those captured malwares.

Note: Note: The biggest catch by TELPOT was a clever attacker who downloaded a Mirai variant piece by piece to fool antivirus and was reported to VirusTotal for the first time.

Link To My Presentation: https://prezi.com/view/Xt0RLRvUItKyBRmy5QCE/

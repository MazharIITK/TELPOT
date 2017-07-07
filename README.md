# TELPOT  
### Capturing Cyber Attacks with generic Telnet Based Honeypot :
This is an implementation of a _simple telnet based Honeypot_ named as **TELPOT**, which consists of a simple echo-server and a proxy written in twisted-python. It's also tested using TELNET_SERVER in place of echo-server. It was deployed in a remote machine having a **public IP** in Digital Ocean.
It had the functionality that, it will show a fake login system to the attacker with an attractive banner. The attacker can make unlimited atttempts to try different passwords. While the attacker is trying to connect to it, this Honeypot will be logging his **IP address**, **port nuumber**, **the date and time** of his login and the **attempts** that the attackers have made with different **passwords**.  
There are two extra directories, one is **IP_PORT** which will contain files according to Date which will store all the IPs and Ports captured at that particular Date. Same will be another directory named **UNAME_PASS** which will contain files storing the username and passwords attempted by the attackers.  And **log_directory** will keep all the logs (scripts) sent by the attacker to compromise my system.
This whole record was accessed remotely through the _specially-designated directory_ **Data Volumes** as it can be seen in the docker-compose file.

**Why TELPOT is differnet from others:**
-> The _docker-compose_ file will run the echo-server at the backend. However , that can be easily replaced by any other server of our own choice. There is another directory TELNET_SERVER which contains the Dockerfile for running Telnet-Server. That was also tested with TELPOT.
This TELPOT is generic and easy to modify accordingly.

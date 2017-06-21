# TestHoneypot
### This was the first test of my simple Honeypot:
This is an implementation of a _simple telnet based Honeypot_, which consists of a simple echo-server and a proxy written in
twisted-python. It was deployed in a remote machine having a **public IP** in Digital Ocean.
It had the functionality that, it will show a fake login system to the attacker with an attractive banner. The attacker can make unlimited atttempts to try different passwords. The attacker will be attracted with the prompts like **slight mispelling. Please check the password and Try Again!!** , **Check the caps-lock key and retype the password.** etc. in order to let him try as much as he can.
While the attacker is trying to connect to it, this Honeypot will be logginh his **IP address**, **port nuumber**, **the date and time** of his login and the **attempts** that the attackers have made with different **passwords**. 
This whole record was accessed remotely through the _specially-designated directory_ **Data Volumes** as it can be seen in the docker-compose file.
Further changes will be made to add some good features to my Honeypot.

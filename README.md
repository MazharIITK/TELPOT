# TestHoneypot
### This was the first test of my simple Honeypot:
This is an implementation of a _simple telnet based Honeypot_, which consists of a simple echo-server and a proxy written in
twisted-python. It was deployed in a remote machine having a **public IP 139.59.18.204** in Digital Ocean.
It had a simple functionality that, it could log the **IP address** and **port nuumber** of the attackers and the file was
accessed remotely through the _specially-designated directory_ **Data Volumes** as it can be seen in the docker-compose file.
Further changes will be made to add some good features to my Honeypot.

FROM riot/riotbuild

run apt-get update && apt-get install telnetd xinetd -y 

run echo "telnet stream tcp nowait telnetd /usr/sbin/tcpd /usr/sbin/in.telnetd" >>  /etc/inetd.conf 

copy inetd.conf /etc/xinetd.conf

run /etc/init.d/xinetd restart 

run useradd admin -m;
run echo "admin:admin" | chpasswd 

expose 23

entrypoint ["/bin/bash"]
#CMD ["/etc/init.d/xinetd","restart","&&","/bin/bash"]


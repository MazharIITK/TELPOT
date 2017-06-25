FROM mazharmiki/twisted

MAINTAINER mazhar <mkhan31995@gmail.com>


RUN mkdir -p proxy/log_directory

RUN mkdir proxy/IP_PORT

RUN mkdir proxy/UNAME_PASS

COPY proxy.py proxy/proxy.py

COPY banner.dat proxy/banner.dat

EXPOSE 23

ENTRYPOINT ["python2.7"]
CMD ["/proxy/proxy.py"]

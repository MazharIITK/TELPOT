FROM mazharmiki/twisted

MAINTAINER mazhar <mkhan31995@gmail.com>


RUN mkdir -p proxy/log_directory

COPY proxy.py proxy/proxy.py

EXPOSE 23

ENTRYPOINT ["python2.7"]
CMD ["/proxy/proxy.py"]

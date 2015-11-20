FROM ubuntu:14.04
RUN apt-get update && apt-get install -y build-essential python2.7 python2.7-dev python-pip python-virtualenv
EXPOSE 8080
WORKDIR /solution
CMD ["make", "install", "go"]
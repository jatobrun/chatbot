FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y
WORKDIR /app
COPY . /app
RUN apt-get install python3-pip -y
RUN pip3 install -r requirements.txt
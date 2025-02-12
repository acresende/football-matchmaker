FROM ubuntu:20.04

USER root

RUN apt update 

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq install python3-opencv python3-dev python3-pip git libsm6 libxext6 libxrender-dev


# Install packages requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /mnt/code

CMD ["bash"]
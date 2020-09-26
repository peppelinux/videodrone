# DOCKER-VERSION 17.10.0-ce
FROM python:slim
MAINTAINER Giuseppe De Marco <giuseppe.demarco@unical.it>

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update
RUN apt install -y locales

# generate chosen locale
RUN sed -i 's/# it_IT.UTF-8 UTF-8/it_IT.UTF-8 UTF-8/' /etc/locale.gen
RUN locale-gen it_IT.UTF-8
# set system-wide locale settings
ENV LANG it_IT.UTF-8
ENV LANGUAGE it_IT
ENV LC_ALL it_IT.UTF-8

ENV VDPATH=VideoDrone
ENV VD_DRONECONN="videodrone.drones.jitsi_chrome"
ENV VD_ROOM="thatroom"
ENV VD_Y4M="/$VDPATH/y4ms/"
ENV VD_LIFETIME=24
ENV VD_DRONE_NUMBER=2

# install dependencies
RUN apt update
RUN apt install -y wget chromium unzip 

# install xvfb
RUN apt-get install -yqq xvfb
# set display port and dbus env to avoid hanging
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

RUN apt clean

# install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install virtualenv
RUN virtualenv -ppython3 env
RUN . env/bin/activate

RUN wget https://raw.githubusercontent.com/peppelinux/videodrone/master/build.sh -O build.sh
RUN bash build.sh $VDPATH

WORKDIR /$VDPATH

## Add the wait script to the image
# ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.2/wait /wait
# RUN chmod +x /wait

# check with
# docker inspect --format='{{json .State.Health}}' uniticket
# HEALTHCHECK --interval=3s --timeout=2s --retries=1 CMD curl --fail http://localhost:8000/ || exit 1

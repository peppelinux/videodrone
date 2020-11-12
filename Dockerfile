FROM alpine:3.12.1
MAINTAINER Giuseppe De Marco <giuseppe.demarco@unical.it>

RUN apk update
RUN apk add chromium
RUN apk add chromium-chromedriver

RUN apk add xvfb
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

RUN apk add py-pip
RUN pip install videodrone

ENV VDPATH=VideoDrone
ENV VD_Y4M="/$VDPATH/y4ms/"

RUN mkdir $VDPATH
WORKDIR $VD_Y4M
RUN wget https://media.xiph.org/video/derf/y4m/stefan_cif.y4m
WORKDIR $VDPATH

# syntax=docker/dockerfile:1

FROM ubuntu:22.04

RUN apt update
RUN apt install -y curl python3-dev python3-pip \
	libglib2.0-0 libgl1 libegl1-mesa libxkbcommon-x11-0 \
	libdbus-1-3 libxcb-xkb1 libxcb-icccm4 libxcb-image0 \
	libxcb-keysyms1 libxcb-render-util0 libxcb-shape0 


RUN curl -sSL https://get.docker.com/ | sh

COPY requirements.txt *.py /

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ADD img /img

#ENV QT_DEBUG_PLUGINS=1

ENTRYPOINT [ "python3", "main.py" ]

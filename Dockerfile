# syntax=docker/dockerfile:1

FROM ubuntu:22.04

RUN apt update && apt install -y curl git unzip \
	python3-dev python3-pip \
	libglib2.0-0 libgl1 libegl1-mesa libxkbcommon-x11-0 \
	libdbus-1-3 libxcb-xkb1 libxcb-icccm4 libxcb-image0 \
	libxcb-keysyms1 libxcb-render-util0 libxcb-shape0 \
	libxcb-xinerama0 libx11-xcb-dev '^libxcb.*-dev' # libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev

COPY requirements.txt *.py /

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ADD img /img
ADD protobuf_types /protobuf_types

ADD https://github.com/protocolbuffers/protobuf/releases/download/v21.8/protoc-21.8-linux-x86_64.zip protoc.zip
RUN unzip protoc.zip
RUN mv bin/protoc /usr/local/bin/protoc

RUN /usr/local/bin/protoc -I=protobuf_types --python_out=. protobuf_types/*.proto

#ENV QT_DEBUG_PLUGINS=1

ENTRYPOINT [ "python3", "main.py" ]

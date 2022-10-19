# syntax=docker/dockerfile:1

FROM ubuntu:22.04

RUN apt update && apt install -y curl git python3-dev python3-pip \
	libglib2.0-0 libgl1 libegl1-mesa libxkbcommon-x11-0 \
	libdbus-1-3 libxcb-xkb1 libxcb-icccm4 libxcb-image0 \
	libxcb-keysyms1 libxcb-render-util0 libxcb-shape0 


RUN curl -sSL https://get.docker.com/ | sh

COPY requirements.txt *.py /

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ADD img /img
ADD protobuf_types /protobuf_types

ADD https://gitlab.com/ApexAI/ade-cli/uploads/591bf9c7ef766cf859749b21afa700b7/ade+x86_64 /usr/local/bin/ade
RUN chmod 0755 /usr/local/bin/ade


ADD https://github.com/protocolbuffers/protobuf/releases/download/v21.8/protoc-21.8-linux-x86_64.zip protoc.zip
RUN unzip protoc.zip
RUN mv bin/protoc /usr/local/bin/protoc

RUN /usr/local/bin/protoc -I=protobuf_types --python_out=. protobuf_types/*.proto

#ENV QT_DEBUG_PLUGINS=1

ENTRYPOINT [ "python3", "main.py" ]

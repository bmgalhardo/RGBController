FROM ubuntu:latest
ENV DEBIAN_FRONTEND="noninteractive" TZ="Europe/Lisbon"
RUN apt update && \
    apt install -y git \
    build-essential \
    qtcreator \
    qt5-default \
    libusb-1.0-0-dev \
    libhidapi-dev \
    pkgconf

RUN git clone https://gitlab.com/CalcProgrammer1/OpenRGB
WORKDIR OpenRGB/
RUN qmake OpenRGB.pro && make -j8
CMD ./openrgb --server
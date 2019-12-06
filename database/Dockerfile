FROM influxdb:alpine

MAINTAINER marcelarosalesj@gmail.com

COPY . /database
WORKDIR /database
EXPOSE 8086
RUN apk add python3 vim
RUN pip3 install -r requirements.txt

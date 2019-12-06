FROM spmallick/opencv-docker:opencv

MAINTAINER marcelarosalesj@gmail.com

COPY . /vision-sense
WORKDIR /vision-sense
RUN apt install -y inetutils-ping
RUN /root/.virtualenvs/OpenCV-master-py3/bin/pip install -r requirements.txt
CMD ["/root/.virtualenvs/OpenCV-master-py3/bin/python", "-u", "/vision-sense/vision-sense.py"]
RUN echo "FINISH"

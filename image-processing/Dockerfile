FROM spmallick/opencv-docker:opencv

MAINTAINER marcelarosalesj@gmail.com

COPY . /image-processing
WORKDIR /image-processing
EXPOSE 5000 
RUN apt install -y inetutils-ping
RUN /root/.virtualenvs/OpenCV-master-py3/bin/pip install -r requirements.txt
CMD ["/root/.virtualenvs/OpenCV-master-py3/bin/python", "-u", "/image-processing/image-processing.py"]

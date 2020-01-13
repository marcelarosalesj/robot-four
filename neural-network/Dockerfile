FROM tensorflow/tensorflow
WORKDIR /

# Get required packages
RUN apt update && \
  apt install vim git python-tk -y
                  
# Get required python modules
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

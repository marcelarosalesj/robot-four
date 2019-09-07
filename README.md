# robot-4

Robot-four is a mobile robot thought to work on an edge cloud environment.


## Architecture

### Hardware
* Pixhawk
* Companion Computer Raspberry Pi

### Software
* Docker container
* Computer Vision application based on OpenCV


## Container Development environment
```
# Get started
docker pull spmallick/opencv-docker:opencv
xhost +local:docker
docker run -v $(pwd):/localdisk --device=/dev/video0:/dev/video0 --device=/dev/video1:/dev/video1 -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -p 5000:5000 -p 8888:8888 -it spmallick/opencv-docker:opencv /bin/bash

# To reuse the development container
docker start  <container_hash>
docker attach <container_hash>
```

## Mount USB
Check out this [guide](https://pimylifeup.com/raspberry-pi-mount-usb-drive/)

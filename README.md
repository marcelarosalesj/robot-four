# Fog robot

Fog robot is a mobile robot thought to work on an edge cloud environment.

## Hardware components

* Pixhawk
* Companion Computer Raspberry Pi

## Software architecture
The Software Architecture is based on microservices using Docker containers. The vision processing is done with OpenCV framework.

* vision-sense
* image-processing
* control-panel
* wheel-motion

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

## References
* [Building your first Chat Application using Flask in 7 minutes](https://codeburst.io/building-your-first-chat-application-using-flask-in-7-minutes-f98de4adfa5d)
* [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
* [Code repository for micro-services: mono repository or multiple repositories](https://medium.com/@somakdas/code-repository-for-micro-services-mono-repository-or-multiple-repositories-d9ad6a8f6e0e)

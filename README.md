# Fog robot

Fog robot is a mobile robot thought to work on an edge cloud environment.

## Hardware components

* Pixhawk
* Companion Computer Raspberry Pi

## Software architecture
The Software Architecture is based on microservices using Docker containers. The vision processing is done with OpenCV framework.

* vision-sense: client system that automatically pulls an image every x seconds, stores it in storage directory and request an operation to image-processing.
* image-processing: server system that performs operation on the image
* control-panel: front-end
* wheel-motion: server system that manages the wheels of the Fog robot.
* storage: filesystem that stores all images related to this system.

## Getting started
```
DISPLAY=:0.0 ; export DISPLAY
xhost +local:docker
docker network create my-network --driver bridge
docker-compose up
```

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
For some the `Dockerfile` files in this project, it is required to use the appropriate virtualenv to use the OpenCV installation.


## Proxies
For running `docker-compose` in an internal network, consider to setup these:
* Add to `/etc/systemd/system/docker.service.d/http-proxy.conf` this `Environment="HTTP_PROXY=http://proxy_url:proxy_port" "NO_PROXY=localhost,127.0.0.0/8"`
* Add here `~/.docker/config.json` this
```
{
 "proxies":
 {
   "default":
   {
     "httpProxy": "http://proxy.server:port",
     "httpsProxy": "http://proxy.server:port",
     "noProxy": "localhost,127.0.0.1"
   }
 }
}
```


## Docker compose

```
# to start the containers
docker-compose up

# to remove everything
docker-compose down -v --rmi all --remove-orphans
```

## Mount USB
Check out this [guide](https://pimylifeup.com/raspberry-pi-mount-usb-drive/)

## References
* [Building your first Chat Application using Flask in 7 minutes](https://codeburst.io/building-your-first-chat-application-using-flask-in-7-minutes-f98de4adfa5d)
* [Designing a RESTful API with Python and Flask](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask)
* [Code repository for micro-services: mono repository or multiple repositories](https://medium.com/@somakdas/code-repository-for-micro-services-mono-repository-or-multiple-repositories-d9ad6a8f6e0e)
* [API Integration in Python – Part 1](https://realpython.com/api-integration-in-python/)
* [Using pyZMQ for inter-process communication: Part 1](https://www.pythonforthelab.com/blog/using-pyzmq-for-inter-process-communication-part-1/)

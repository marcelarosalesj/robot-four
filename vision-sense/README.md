# vision-sense

Get an image from a camera, store it in `../storage` and send a request to image-processing/bw

```
# Build image
docker build --build-arg http_proxy=$PROXY --build-arg https_proxy=$PROXY -t r4-vs .

# For X11 forwarding
DISPLAY=:0.0 ; export DISPLAY
xhost +local:docker

# Create container
docker run --device=/dev/video0:/dev/video0 -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -p 5000:5000 -p 8888:8888 --name r4-cont r4-vs:latest
```


## InfluxDB

* [InfluxDB Python Examples](https://influxdb-python.readthedocs.io/en/latest/examples.html)

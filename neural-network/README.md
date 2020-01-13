# Neural network

## Tensorflow container
```
DISPLAY=:0.0 ; export DISPLAY
xhost +local:docker

docker run -it --device=/dev/video0:/dev/video0 -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY --name nn -v $(pwd):/localdisk -v $(pwd)/data:/data -v $(pwd)/sub:/sub tensorflow/tensorflow /bin/bash
```

## Development environment: Docker container with CUDA support
- [Tensorflow and Docker](https://www.tensorflow.org/install/docker)
- [nvidia-docker support](https://github.com/NVIDIA/nvidia-docker)
- [NVIDIA CUDA Installation Guide for Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
- Note: if you're using the nvidia-docker toolkit, remember to have all previous cuda installation removed before installing. For example: `sudo apt-get purge nvidia-*` or `sudo apt autoremove`.
- For cuda installation I used package local (deb).
- After installing nvidia driver and nvidia-docker, you can pull docker tensorflow image with gpu support.
```
docker run --gpus all -it --rm tensorflow/tensorflow:latest-gpu \
    python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
```

## References
* [Deep Learning Guide: Introduction to Implementing Neural Networks using TensorFlow in Python](https://www.analyticsvidhya.com/blog/2016/10/an-introduction-to-implementing-neural-networks-using-tensorflow/)
* [A quick complete tutorial to save and restore Tensorflow models](https://cv-tricks.com/tensorflow-tutorial/save-restore-tensorflow-models-quick-complete-tutorial/)
*

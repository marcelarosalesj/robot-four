# Neural network


## Development environment
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

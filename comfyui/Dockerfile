ARG DOCKER_FROM=nvcr.io/nvidia/cuda:12.4.0-devel-ubi8 
#ARG DOCKER_FROM=nvidia/cuda:12.3.2-runtime-ubuntu22.04

FROM ${DOCKER_FROM}

# Install needed packages
RUN dnf install -y \
    unzip \
    zip \
    rsync \
    python3.12 \
    python3.12-pip \
    git \
    sudo \
    net-tools \
    bind-utils \
    xz \
    zlib-devel
    
ENV DOCKER_FROM_BASE=localhost/cuda-cudnn:12.4.0-devel-ubi8
ENV BUILD_FILE="/etc/image_base.txt"
ENV NV_CUDNN_PACKAGE_NAME=libcudnn9-cuda-12
ENV NV_CUDNN_VERSION=9.3.0.75-1
RUN echo "DOCKER_FROM: ${DOCKER_FROM_BASE}" | tee ${BUILD_FILE}
RUN echo "CUDNN: ${NV_CUDNN_PACKAGE_NAME} (${NV_CUDNN_VERSION})" | tee -a ${BUILD_FILE}

##### ComfyUI preparation
# The comfy user will have UID 1024 and GID 1024
ENV COMFYUSER_DIR="/comfy"
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \
    && useradd -u 1024 -U -d ${COMFYUSER_DIR} -s /bin/bash -m comfy \
    && echo 'comfy:comfy' | chpasswd \
    && usermod -G users comfy \
    #&& adduser comfy sudo \
    && usermod -aG wheel comfy \
    && test -d ${COMFYUSER_DIR}
RUN it="/etc/comfyuser_dir"; echo ${COMFYUSER_DIR} > $it && chmod 555 $it

ENV NVIDIA_VISIBLE_DEVICES=all

EXPOSE 8188

USER comfy
WORKDIR ${COMFYUSER_DIR}
COPY --chown=comfy:comfy --chmod=555 init.bash init.bash
COPY --chown=comfy:comfy --chmod=555 start.bash start.bash

ARG BUILD_DATE="unknown"
LABEL comfyui-nvidia-docker-build=${BUILD_DATE}

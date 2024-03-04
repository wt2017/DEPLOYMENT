# Nvidia base image
FROM docker.io/nvidia/cuda:12.2.2-devel-ubi8

# Add user wyou
RUN useradd -ms /bin/bash wyou
WORKDIR /home/wyou

# Install packages required by alpha-zero
RUN dnf install -y python3.11
RUN dnf install -y python3.11-pip

RUN pip3.11 install --timeout=1000 --no-cache-dir coloredlogs
RUN pip3.11 install --timeout=1000 --no-cache-dir numpy
RUN pip3.11 install --timeout=1000 --no-cache-dir tqdm
RUN pip3.11 install torch torchvision torchaudio -f https://download.pytorch.org/whl/cu122/torch_stable.html

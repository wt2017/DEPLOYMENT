FROM nvcr.io/nvidia/cuda:12.4.0-devel-ubi8 as base
FROM base as base-amd64

RUN dnf -y install wget
RUN wget https://developer.download.nvidia.com/compute/cudnn/9.3.0/local_installers/cudnn-local-repo-rhel9-9.3.0-1.0-1.x86_64.rpm
RUN rpm -i cudnn-local-repo-rhel9-9.3.0-1.0-1.x86_64.rpm
RUN dnf clean all
RUN dnf -y install cudnn-cuda-12

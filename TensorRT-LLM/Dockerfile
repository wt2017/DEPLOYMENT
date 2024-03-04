# Nvidia base image
FROM localhost/tensorrt_llm_2/devel

# Add a layer
RUN python3 -m pip install --upgrade pip
COPY tensorrt-llm.tar /workspace/tensorrt-llm.tar
RUN tar xvf tensorrt-llm.tar
WORKDIR /workspace/TensorRT-LLM/
RUN python3 ./scripts/build_wheel.py --clean  --trt_root /usr/local/tensorrt
RUN pip install ./build/tensorrt_llm*.whl


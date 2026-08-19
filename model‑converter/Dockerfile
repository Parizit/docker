ARG VERSION=1.0.2

FROM python:3.10.18-slim AS builder

LABEL \
  org.opencontainers.image.version="${VERSION}" \
  org.opencontainers.image.created="${BUILD_DATE:-$(date --iso-8601=seconds)}"
  
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_BREAK_SYSTEM_PACKAGES=1 \
    DEBIAN_FRONTEND=noninteractive
    
RUN apt-get update \
    && apt-get install -y --no-install-recommends zip libgl1 libglib2.0-0  \
    && pip3 install --upgrade pip \
    && pip3 install --upgrade torch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 --index-url https://download.pytorch.org/whl/cpu \
    && pip3 install --no-cache-dir \
         ultralytics==8.3.170 \
         protobuf==4.25.4 \
         psutil \
         ruamel.yaml \
         scipy \
         tqdm \
         seaborn \
         onnx==1.18.0 onnxruntime==1.22.1 \
         IPython gitpython setuptools==70.0.0 \
         rknn-toolkit2 \
    # Очищаем APT-кеш
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.cache/pip
         
CMD ["bash"]

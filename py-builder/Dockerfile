ARG VERSION=1.1.0
ARG BUILD_DATE

FROM python:3.8-slim AS builder

ARG VERSION
ARG BUILD_DATE

LABEL \
  org.opencontainers.image.version="${VERSION}" \
  org.opencontainers.image.created="${BUILD_DATE}"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    DEBIAN_FRONTEND=noninteractive

# Устанавливаем системные зависимости для сборки и binutils (objdump)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
         zip binutils \
    && rm -rf /var/lib/apt/lists/*

# Обновляем pip и ставим инструменты
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir pyinstaller pyarmor

COPY gen_metadata.py /tools/gen_metadata.py

CMD ["bash"]

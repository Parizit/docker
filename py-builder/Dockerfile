ARG VERSION=1.1.0
ARG BUILD_DATE
FROM ubuntu:20.04 AS builder

# Устанавливаем системные зависимости для сборки и binutils (objdump)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
         zip \
         python3-pip python3-dev \
         binutils libgl1 libglib2.0-0 \
    # Обновляем pip и устанавливаем инструменты без кеша
    && pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir \
        pyinstaller pyarmor \
        numpy pika websockets \
    # Очищаем APT-кеш
    && rm -rf /var/lib/apt/lists/*

COPY gen_metadata.py /tools/gen_metadata.py

LABEL \
  org.opencontainers.image.version="${VERSION}" \
  org.opencontainers.image.created="${BUILD_DATE}"

# По умолчанию обеспечиваем доступ к shell для отладки
CMD ["bash"]

ARG VERSION=1.0.1
FROM ubuntu:20.04 AS builder

LABEL \
  org.opencontainers.image.version="${VERSION}" \
  org.opencontainers.image.created="${BUILD_DATE:-$(date --iso-8601=seconds)}"

# Устанавливаем системные зависимости для сборки и binutils (objdump)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
         zip \
         python3-pip python3-dev \
         binutils \
    # Обновляем pip и устанавливаем инструменты без кеша
    && pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir \
        pyinstaller pyarmor \
        numpy pika websockets \
    # Очищаем APT-кеш
    && rm -rf /var/lib/apt/lists/*

# По умолчанию обеспечиваем доступ к shell для отладки
CMD ["bash"]


docker buildx build \
  -f Dockerfile.ubuntu \
  --platform linux/amd64,linux/arm64 \
  --build-arg UBUNTU_VERSION=20.04 \
  --build-arg VERSION=3.0.0 \
  --build-arg BUILD_DATE="$(date -u +"%Y-%m-%dT%H:%M:%SZ")" \
  --pull \
  -t parizit/py-builder:3.0.0-3.8-ubuntu20.04 \
  -t parizit/py-builder:3.8 \
  --push .

docker buildx build \
  -f Dockerfile.ubuntu \
  --platform linux/amd64,linux/arm64 \
  --build-arg UBUNTU_VERSION=22.04 \
  --build-arg VERSION=3.0.0 \
  --build-arg BUILD_DATE="$(date -u +"%Y-%m-%dT%H:%M:%SZ")" \
  --pull \
  -t parizit/py-builder:3.0.0-3.10-ubuntu22.04 \
  -t parizit/py-builder:3.10 \
  --push .
  
docker buildx build \
  -f Dockerfile.ubuntu \
  --platform linux/amd64,linux/arm64 \
  --build-arg UBUNTU_VERSION=24.04 \
  --build-arg VERSION=3.0.0 \
  --build-arg BUILD_DATE="$(date -u +"%Y-%m-%dT%H:%M:%SZ")" \
  --pull \
  -t parizit/py-builder:3.0.0-3.12-ubuntu24.04 \
  -t parizit/py-builder:3.12 \
  --push .

docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --build-arg PYTHON_VERSION=3.10 \
  --build-arg VERSION=2.0.0 \
  --build-arg BUILD_DATE="$(date -u +"%Y-%m-%dT%H:%M:%SZ")" \
  --pull \
  -t parizit/py-builder:2.0.0-3.10-bullseye \
  -t parizit/py-builder:3.12 \
  --push .

docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --build-arg PYTHON_VERSION=3.11 \
  --build-arg VERSION=2.0.0 \
  --build-arg BUILD_DATE="$(date -u +"%Y-%m-%dT%H:%M:%SZ")" \
  --pull \
  -t parizit/py-builder:2.0.0-3.11-bullseye \
  -t parizit/py-builder:3.11 \
  --push .
  
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --build-arg PYTHON_VERSION=3.12 \
  --build-arg VERSION=2.0.0 \
  --build-arg BUILD_DATE="$(date -u +"%Y-%m-%dT%H:%M:%SZ")" \
  --pull \
  -t parizit/py-builder:2.0.0-3.12-bullseye \
  -t parizit/py-builder:3.12 \
  --push .

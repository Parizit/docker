docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --build-arg PYTHON_VERSION=3.8 \
  --build-arg VERSION=2.0.0 \
  --build-arg BUILD_DATE="$(date -u +"%Y-%m-%dT%H:%M:%SZ")" \
  --pull \
  -t parizit/py-builder:2.0.0-3.8-bullseye \
  -t parizit/py-builder:3.8 \
  -t parizit/py-builder:latest \
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

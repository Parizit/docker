docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --build-arg VERSION=2.0.0 \
  --build-arg BUILD_DATE="$(date -u +"%Y-%m-%dT%H:%M:%SZ")" \
  --pull \
  -t parizit/py-builder:2.0.0 \
  -t parizit/py-builder:latest \
  --push .

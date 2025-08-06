docker buildx build \
  --platform linux/amd64,linux/arm64 \
  --build-arg VERSION=1.0.3 \
  --build-arg BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ") \
  -t parizit/py-builder:1.0.3 \
  -t parizit/py-builder:latest \
  --push .

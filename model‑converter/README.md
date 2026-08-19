docker build --build-arg VERSION=1.0.2 -t parizit/model-converter:1.0.2 -t parizit/model-converter:latest .
docker push parizit/model-converter:1.0.2 && docker push parizit/model-converter:latest


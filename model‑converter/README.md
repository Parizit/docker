docker build --build-arg VERSION=1.0.1 -t parizit/model-converter:1.0.1 -t parizit/model-converter:latest .
docker push parizit/model-converter:1.0.1 && docker push parizit/model-converter:latest


docker build --build-arg VERSION=1.0.2 -t parizit/py-builder:1.0.2 .
docker push parizit/py-builder:1.0.2
docker tag parizit/py-builder:1.0.2 parizit/py-builder:latest
docker push parizit/py-builder:latest

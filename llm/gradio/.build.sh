# .build.sh
# Build script for Docker Hub

TAG=2
IMAGE_PATH=docker.io/wdenniss/gradio-demo
IMAGE_NAME=$IMAGE_PATH:$TAG
IMAGE_NAME_LATEST=$IMAGE_PATH:latest

docker build . -t $IMAGE_NAME
docker push $IMAGE_NAME

docker tag $IMAGE_PATH:$TAG $IMAGE_NAME_LATEST
docker push $IMAGE_NAME_LATEST

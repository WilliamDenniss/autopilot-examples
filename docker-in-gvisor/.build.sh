REPO=wdenniss/docker-in-gvisor
IMAGE=$REPO:latest
#REPO=us-west1-docker.pkg.dev/gke-autopilot-test/dind-test
#IMAGE=$REPO/docker-in-gvisor:latest

docker build -t $IMAGE images/basic/docker
docker push $IMAGE

echo "$IMAGE pushed".


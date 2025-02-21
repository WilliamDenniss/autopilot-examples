Example gradio app for communicating with a vLLM service.

Must set the `MODEL_ID` environment variable with the matching model ID of the vLLM deployment.

To build, update the image name with the path to your own AR repository, and run:

```
IMAGE_NAME=us-docker.pkg.dev/gke-autopilot-test/gradio/app:8
docker build . -t $IMAGE_NAME
docker push $IMAGE_NAME
```

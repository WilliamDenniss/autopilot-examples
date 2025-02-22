Example deployment of [DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)
running on a single spot A100 80 GPU, with an example gradio interface to interact with the model.

`deepseek-ai/DeepSeek-R1-Distill-Qwen-32B` can also run on this A100 80GB configuration (update the `MODEL_ID` environment variable in deployments with that value to try).

# Create the secret

Requires creation of a secret with your Hugging Face token (more details in the [GKE docs](https://cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-vllm#create_a_kubernetes_secret_for_hugging_face_credentials)).

```
HF_TOKEN=your_api_key
kubectl create secret generic hf-secret \
    --from-literal=hf_api_token=$HF_TOKEN \
    --dry-run=client -o yaml | kubectl apply -f -
```

# Deploy

```
kubectl create -f .
```

# Connect

```
kubectl get svc
```

Note: this exposes the demo publicly on the internet. Use with caution.
Alternatively you can remove the `type: LoadBalancer` field from gradio-service.yaml and connect locally.
```
kubectl port-forward svc/gradio-service 8080:80
```

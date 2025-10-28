# Gemma 3 27B in 3 configurations

0. Create your Hugging Face Secret

```
HF_TOKEN=your_token
kubectl create secret generic hf-secret \
    --from-literal=hf_api_token=${HF_TOKEN}
```

1. Create a vLLM Deployment

Choose one or multiple.

TPU v5 2x2
```
kubectl create -f tpu/vllm-gemma-3-27b-tpu-v5.yaml
```

GPU A100 80GB
```
kubectl create -f a100-80/vllm-gemma-3-27b-a100-80.yaml
```

GPU L4 x4
```
kubectl create -f l4/vllm-gemma-3-27b-l4.yaml
```

2. Port-forward

TPU v5 2x2
```
kubectl port-forward deployment/vllm-gemma-3-27b-tpu-v5 8000:8000
```

GPU A100 80GB
```
kubectl port-forward deployment/vllm-gemma-3-27b-a100-80 8000:8000
```

GPU L4 x4
```
kubectl port-forward deployment/vllm-gemma-27b-l4 8000:8000
```

3. Watch

Wait for the Pods to be Ready

```
watch -d kubectl get nodes,deploy,pods
```

Tail logs to observe LLM boot

```
kubectl logs -f $POD_NAME
```

4. Test

```
curl http://127.0.0.1:8000/v1/completions \
-H "Content-Type: application/json" \
-d '{
    "prompt": "Recipe for Anzac biscuits",
    "max_tokens": 2000
}' | python extract_text.py
```

```
curl http://127.0.0.1:8000/v1/completions \
-H "Content-Type: application/json" \
-d '{
    "prompt": "How to make wood-fired pizza",
    "max_tokens": 2000
}' | python extract_text.py
```

5. Aggregate

To run a single Service aggregating all Pods from all Deployments serving the same model

```
kubectl create -f gemma-3-27b-service.yaml
```

To connect locally, proxy (rather than port forward) for load balancing

```
kubectl proxy
```

Example using the proxied service:

```
curl http://localhost:8001/api/v1/namespaces/default/services/http:gemma-3-27b-it:8000/proxy/v1/completions \
-H "Content-Type: application/json" \
-d '{
    "prompt": "Recipe for Anzac biscuits",
    "max_tokens": 2000
}' | python extract_text.py
```

```
curl http://localhost:8001/api/v1/namespaces/default/services/http:gemma-3-27b-it:8000/proxy/v1/completions \
-H "Content-Type: application/json" \
-d '{
    "prompt": "How to make wood-fired pizza",
    "max_tokens": 2000
}' | python extract_text.py
```

5. Delete

```
kubectl delete -f tpu/vllm-gemma-3-27b-tpu-v5.yaml
kubectl delete -f a100-80/vllm-gemma-3-27b-a100-80.yaml
kubectl delete -f l4/vllm-gemma-3-27b-l4.yaml
kubectl delete -f gemma-3-27b-service.yaml
```
# ☸️ Phase 14: Deploy Locally With Kubernetes

Goal: deploy the full microservice stack to Docker Desktop Kubernetes.

This phase happens before CI/CD and AWS so you can practice deployment locally first.

## 🧱 What Will Run In Kubernetes

| Component | Kubernetes Object |
| --- | --- |
| PostgreSQL | Deployment + Service + PersistentVolumeClaim |
| Redis | Deployment + Service |
| Auth service | Deployment + Service |
| Product service | Deployment + Service |
| Order service | Deployment + Service |
| Frontend | Deployment + Service |
| Nginx gateway | Deployment + NodePort Service |

## 🪜 Step 1: Make Sure Docker Desktop Kubernetes Is Running

```powershell
kubectl config use-context docker-desktop
kubectl get nodes
```

Expected:

```text
docker-desktop   Ready
```

## 🪜 Step 2: Build Local Images

Kubernetes needs images to run.

Build them from project root:

```powershell
docker build -t auth-service:local .\services\auth-service
docker build -t product-service:local .\services\product-service
docker build -t order-service:local .\services\order-service
docker build -t microservices-frontend:local .\frontend
```

Why `:local`?

These images stay on your laptop. You do not need Docker Hub or AWS ECR for this phase.

The gateway uses the official Nginx image and a Kubernetes ConfigMap for its config.

## 🪜 Step 3: Apply Kubernetes Manifests

Run:

```powershell
kubectl apply -f .\kubernetes\local
```

This creates:

- Namespace
- ConfigMap
- Secret
- PostgreSQL
- Redis
- Backend services
- Frontend
- Gateway

## 🪜 Step 4: Watch Pods Start

```powershell
kubectl get pods -n microservices-local -w
```

Wait until pods show:

```text
Running
```

Stop watching with `Ctrl+C`.

## 🪜 Step 5: Check Services

```powershell
kubectl get svc -n microservices-local
```

Look for:

```text
gateway   NodePort   ...   80:30080/TCP
```

## 🪜 Step 6: Test In Browser

Open:

```text
http://localhost:30080
```

Test APIs:

```text
http://localhost:30080/api/auth/health
http://localhost:30080/api/products
http://localhost:30080/api/orders
```

## 📬 Test One API In Postman

Use Postman exactly like earlier, but change the URL to Kubernetes gateway.

Example:

| Field | Value |
| --- | --- |
| Method | `GET` |
| URL | `http://localhost:30080/api/products` |

Expected:

```text
200 OK
```

## 🧪 Create Order Through Kubernetes

In Postman:

| Field | Value |
| --- | --- |
| Method | `POST` |
| URL | `http://localhost:30080/api/orders` |
| Body | `raw` -> `JSON` |

Body:

```json
{
  "userId": 1,
  "productId": 1,
  "quantity": 2
}
```

Expected:

```text
201 Created
```

## 🛠️ Useful Debug Commands

List pods:

```powershell
kubectl get pods -n microservices-local
```

Describe a pod:

```powershell
kubectl describe pod <pod-name> -n microservices-local
```

View logs:

```powershell
kubectl logs deployment/auth-service -n microservices-local
kubectl logs deployment/product-service -n microservices-local
kubectl logs deployment/order-service -n microservices-local
kubectl logs deployment/gateway -n microservices-local
```

Restart one deployment:

```powershell
kubectl rollout restart deployment/auth-service -n microservices-local
```

## 🧹 Cleanup

Delete the local Kubernetes deployment:

```powershell
kubectl delete namespace microservices-local
```

This removes all Kubernetes objects created for this project.

## ✅ Checkpoint

You are ready when:

- `kubectl get pods -n microservices-local` shows running pods.
- `http://localhost:30080` opens the frontend.
- `http://localhost:30080/api/products` returns products.
- You understand how to view Kubernetes logs.

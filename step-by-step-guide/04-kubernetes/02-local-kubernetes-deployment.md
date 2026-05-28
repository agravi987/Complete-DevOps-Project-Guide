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

## 🪜 Step 2: Build And Push Images To Docker Hub

Kubernetes needs images to run.

Using Docker Hub is the easiest way to avoid `ErrImagePull` or `ImagePullBackOff` while learning Kubernetes. The Kubernetes node can pull the same image that you pushed to Docker Hub, so it does not depend on whether the image exists only on your laptop.

Create public Docker Hub repositories with these names:

- `auth-service`
- `product-service`
- `order-service`
- `microservices-frontend`

Then set your Docker Hub username and image tag in PowerShell:

```powershell
$env:DOCKERHUB_USERNAME="your-dockerhub-username"
$env:IMAGE_TAG="v1"
docker login
```

Build the images from the project root:

```powershell
docker build -t "$env:DOCKERHUB_USERNAME/auth-service:$env:IMAGE_TAG" .\services\auth-service
docker build -t "$env:DOCKERHUB_USERNAME/product-service:$env:IMAGE_TAG" .\services\product-service
docker build -t "$env:DOCKERHUB_USERNAME/order-service:$env:IMAGE_TAG" .\services\order-service
docker build -t "$env:DOCKERHUB_USERNAME/microservices-frontend:$env:IMAGE_TAG" .\frontend
```

Push the images:

```powershell
docker push "$env:DOCKERHUB_USERNAME/auth-service:$env:IMAGE_TAG"
docker push "$env:DOCKERHUB_USERNAME/product-service:$env:IMAGE_TAG"
docker push "$env:DOCKERHUB_USERNAME/order-service:$env:IMAGE_TAG"
docker push "$env:DOCKERHUB_USERNAME/microservices-frontend:$env:IMAGE_TAG"
```

Confirm that Docker Hub can pull one image back:

```powershell
docker pull "$env:DOCKERHUB_USERNAME/auth-service:$env:IMAGE_TAG"
```

If this works, Kubernetes will also be able to pull the image as long as the repository is public. For private Docker Hub repositories, you must create a Kubernetes image pull secret. For this learning project, public repositories are simpler.

## 🪜 Step 3: Update Kubernetes Image Names

Open:

```text
kubernetes/local/04-backend-services.yaml
kubernetes/local/05-frontend-and-gateway.yaml
```

Replace the local image names with your Docker Hub image names.

In `04-backend-services.yaml`, use:

```yaml
image: your-dockerhub-username/auth-service:v1
imagePullPolicy: IfNotPresent
```

```yaml
image: your-dockerhub-username/product-service:v1
imagePullPolicy: IfNotPresent
```

```yaml
image: your-dockerhub-username/order-service:v1
imagePullPolicy: IfNotPresent
```

In `05-frontend-and-gateway.yaml`, use:

```yaml
image: your-dockerhub-username/microservices-frontend:v1
imagePullPolicy: IfNotPresent
```

Do not change the gateway image:

```yaml
image: nginx:alpine
```

Important:

- Replace `your-dockerhub-username` with your real Docker Hub username.
- Use the same tag that you pushed, for example `v1`.
- Do not keep `imagePullPolicy: Never` when using Docker Hub. `Never` tells Kubernetes not to pull the image.

## Optional: Local Images Without Docker Hub

If you are using only Docker Desktop Kubernetes, local images can also work.

Build them from the project root:

```powershell
docker build -t auth-service:local .\services\auth-service
docker build -t product-service:local .\services\product-service
docker build -t order-service:local .\services\order-service
docker build -t microservices-frontend:local .\frontend
```

For local images, the manifest can use:

```yaml
image: auth-service:local
imagePullPolicy: Never
```

This means the image must already exist inside Docker Desktop. If the image is missing, Kubernetes cannot pull it from Docker Hub because `auth-service:local` is only a local name.

The gateway uses the official Nginx image and a Kubernetes ConfigMap for its config.

## 🪜 Step 4: Apply Kubernetes Manifests

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

## 🪜 Step 5: Watch Pods Start

```powershell
kubectl get pods -n microservices-local -w
```

Wait until pods show:

```text
Running
```

Stop watching with `Ctrl+C`.

If any pod shows `ErrImagePull` or `ImagePullBackOff`, describe the pod:

```powershell
kubectl describe pod <pod-name> -n microservices-local
```

Look at the `Events` section. Most image errors are caused by one of these:

- The image name in the manifest does not match Docker Hub.
- The image tag was not pushed.
- The Docker Hub repository is private.
- `imagePullPolicy` is still set to `Never`.

## 🪜 Step 6: Check Services

```powershell
kubectl get svc -n microservices-local
```

Look for:

```text
gateway   NodePort   ...   80:30080/TCP
```

## 🪜 Step 7: Verify The Deployment Is Successful

Use this checklist every time you deploy.

### 1. Check that all deployments are available

```powershell
kubectl get deployments -n microservices-local
```

Expected result:

```text
NAME              READY   UP-TO-DATE   AVAILABLE   AGE
auth-service      1/1     1            1           2m
frontend          1/1     1            1           2m
gateway           1/1     1            1           2m
order-service     1/1     1            1           2m
postgres          1/1     1            1           2m
product-service   1/1     1            1           2m
redis             1/1     1            1           2m
```

The important columns are:

- `READY` should be `1/1`.
- `AVAILABLE` should be `1`.

### 2. Wait until Kubernetes marks deployments available

```powershell
kubectl wait --for=condition=available deployment --all -n microservices-local --timeout=180s
```

Expected result:

```text
deployment.apps/auth-service condition met
deployment.apps/product-service condition met
deployment.apps/order-service condition met
deployment.apps/frontend condition met
deployment.apps/gateway condition met
deployment.apps/postgres condition met
deployment.apps/redis condition met
```

### 3. Check pods

```powershell
kubectl get pods -n microservices-local
```

Expected result:

```text
NAME                               READY   STATUS    RESTARTS   AGE
auth-service-xxxxx                 1/1     Running   0          2m
product-service-xxxxx              1/1     Running   0          2m
order-service-xxxxx                1/1     Running   0          2m
frontend-xxxxx                     1/1     Running   0          2m
gateway-xxxxx                      1/1     Running   0          2m
postgres-xxxxx                     1/1     Running   0          2m
redis-xxxxx                        1/1     Running   0          2m
```

The deployment is not healthy yet if you see `Pending`, `CrashLoopBackOff`, `ErrImagePull`, or `ImagePullBackOff`.

### 4. Check the gateway service

```powershell
kubectl get svc gateway -n microservices-local
```

Expected:

```text
NAME      TYPE       CLUSTER-IP   EXTERNAL-IP   PORT(S)        AGE
gateway   NodePort   ...          <none>        80:30080/TCP   2m
```

### 5. Test in the browser

Open:

```text
http://localhost:30080
```

### 6. Test API health endpoints

```powershell
Invoke-RestMethod http://localhost:30080/api/auth/health
Invoke-RestMethod http://localhost:30080/api/products/health
Invoke-RestMethod http://localhost:30080/api/orders/health
```

Then test real API data:

```powershell
Invoke-RestMethod http://localhost:30080/api/products
```

If the browser opens and the API commands return successful responses, your Kubernetes deployment is working.

### 7. Check recent Kubernetes events if something is still wrong

```powershell
kubectl get events -n microservices-local --sort-by=.lastTimestamp
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

- Docker Hub images are pushed and Kubernetes manifests use those image names.
- `kubectl wait --for=condition=available deployment --all -n microservices-local --timeout=180s` succeeds.
- `kubectl get pods -n microservices-local` shows running pods.
- There are no `ErrImagePull` or `ImagePullBackOff` pod errors.
- `http://localhost:30080` opens the frontend.
- `http://localhost:30080/api/products` returns products.
- You understand how to view Kubernetes logs.

## Next Phase

[Phase 15: Git And GitHub](../05-ci-cd/01-git-github.md)

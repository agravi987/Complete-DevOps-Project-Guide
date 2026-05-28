# 🛠️ Troubleshooting

Use this when something does not work.

## 🐳 Docker Desktop Not Running

Error:

```text
Cannot connect to the Docker daemon
```

Fix:

1. Start Docker Desktop.
2. Wait for the engine to finish starting.
3. Run the command again.

## 🚧 Port Already Allocated

Error:

```text
Bind for 0.0.0.0:3001 failed: port is already allocated
```

Find what is running:

```powershell
docker ps
netstat -ano | findstr :3001
```

Stop old container:

```powershell
docker stop <container-name>
```

## 📦 npm ci Fails In Docker

Cause:

`npm ci` requires `package-lock.json`.

Fix:

```powershell
cd services\auth-service
npm install
```

Commit `package-lock.json`.

## 🐘 Service Cannot Connect To PostgreSQL

Check container status:

```powershell
docker compose ps
docker compose logs postgres
docker compose logs auth-service
```

Check environment values:

```powershell
docker exec -it auth-service env
```

Inside Docker Compose, the host should be:

```text
POSTGRES_HOST=postgres
```

Not:

```text
POSTGRES_HOST=localhost
```

## 🌐 Nginx Route Returns 502

Cause:

Nginx cannot reach the upstream service.

Check:

```powershell
docker compose ps
docker compose logs microservices-gateway
docker compose logs product-service
```

Make sure service names in `nginx.conf` match names in `docker-compose.yml`.

## ⚛️ React Shows Gateway Not Running Yet

Check:

```powershell
docker compose ps
Invoke-RestMethod http://localhost:8080/api/products
```

Make sure `VITE_API_BASE_URL` is:

```env
VITE_API_BASE_URL=http://localhost:8080/api
```

Rebuild frontend after changing Vite environment variables:

```powershell
docker compose build frontend
docker compose up -d frontend
```

## 📬 Postman Variables Not Replaced

Symptom:

```text
{{gatewayBaseUrl}}/api/products
```

appears in the request URL or the request fails immediately.

Fix:

1. Check the request URL manually.
2. If you created a Postman environment yourself, select it in the environment dropdown.
3. If you are not using environments, replace variables like `{{gatewayBaseUrl}}` with `http://localhost:8080`.
4. Run the request again.

## 📬 Postman Register Returns 409

This means the test user already exists.

This is not always a problem. Continue with login.

To create a fresh user:

1. Open the Postman environment.
2. Change `userEmail`.
3. Save the environment.
4. Run Register User again.

## ☸️ kubectl Cannot Find The Cluster

Check your current context:

```powershell
kubectl config current-context
kubectl config get-contexts
```

Switch to Docker Desktop:

```powershell
kubectl config use-context docker-desktop
kubectl get nodes
```

If `docker-desktop` does not exist, enable Kubernetes in Docker Desktop settings.

## ☸️ Kubernetes Pod Shows ErrImagePull Or ImagePullBackOff

First, find the exact pod name:

```powershell
kubectl get pods -n microservices-local
```

Then describe the failing pod:

```powershell
kubectl describe pod <pod-name> -n microservices-local
```

Read the `Events` section at the bottom. It usually tells you which image Kubernetes failed to pull.

Common causes:

- The image name in the Kubernetes manifest is wrong.
- The image tag does not exist on Docker Hub.
- The image was built but not pushed.
- The Docker Hub repository is private.
- `imagePullPolicy` is set to `Never`, so Kubernetes is not allowed to pull the image.

Recommended fix with Docker Hub:

```powershell
$env:DOCKERHUB_USERNAME="your-dockerhub-username"
$env:IMAGE_TAG="v1"
docker login

docker build -t "$env:DOCKERHUB_USERNAME/auth-service:$env:IMAGE_TAG" .\services\auth-service
docker build -t "$env:DOCKERHUB_USERNAME/product-service:$env:IMAGE_TAG" .\services\product-service
docker build -t "$env:DOCKERHUB_USERNAME/order-service:$env:IMAGE_TAG" .\services\order-service
docker build -t "$env:DOCKERHUB_USERNAME/microservices-frontend:$env:IMAGE_TAG" .\frontend

docker push "$env:DOCKERHUB_USERNAME/auth-service:$env:IMAGE_TAG"
docker push "$env:DOCKERHUB_USERNAME/product-service:$env:IMAGE_TAG"
docker push "$env:DOCKERHUB_USERNAME/order-service:$env:IMAGE_TAG"
docker push "$env:DOCKERHUB_USERNAME/microservices-frontend:$env:IMAGE_TAG"
```

Update the app images in:

```text
kubernetes/local/04-backend-services.yaml
kubernetes/local/05-frontend-and-gateway.yaml
```

Use Docker Hub image names:

```yaml
image: your-dockerhub-username/auth-service:v1
imagePullPolicy: IfNotPresent
```

Do the same for `product-service`, `order-service`, and `microservices-frontend`.

Apply again:

```powershell
kubectl apply -f .\kubernetes\local
kubectl wait --for=condition=available deployment --all -n microservices-local --timeout=180s
```

Check that the pods recovered:

```powershell
kubectl get pods -n microservices-local
```

Optional local-only fix:

If you are using Docker Desktop Kubernetes and local images only, build the local image with the exact name used in the manifest:

```powershell
docker build -t auth-service:local .\services\auth-service
docker build -t product-service:local .\services\product-service
docker build -t order-service:local .\services\order-service
docker build -t microservices-frontend:local .\frontend
```

Then restart the deployment:

```powershell
kubectl rollout restart deployment/auth-service -n microservices-local
kubectl rollout restart deployment/product-service -n microservices-local
kubectl rollout restart deployment/order-service -n microservices-local
kubectl rollout restart deployment/frontend -n microservices-local
```

## ☸️ Kubernetes Gateway Does Not Open

Check the gateway service:

```powershell
kubectl get svc -n microservices-local
```

You should see:

```text
gateway   NodePort   ...   80:30080/TCP
```

Then open:

```text
http://localhost:30080
```

## 🔐 AWS ECR Login Fails

Check:

```powershell
aws sts get-caller-identity
aws --version
```

Login again:

```powershell
aws ecr get-login-password --region $env:AWS_REGION |
  docker login --username AWS --password-stdin $env:ECR_REGISTRY
```

## 🚀 ECS Task Stops Immediately

Check CloudWatch logs first.

Common causes:

- Wrong container port
- Missing environment variable
- Wrong image URI
- App crashes on startup
- Task cannot read Secrets Manager value
- Security group blocks database connection

## 🧠 Best Debugging Habit

Read the first real error. The first error usually tells you the cause. Later errors often only describe side effects.

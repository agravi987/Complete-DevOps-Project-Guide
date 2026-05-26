# 🧪 Lab 07: Local Kubernetes Deployment

## 🎯 Objective

Deploy the microservices project locally using Kubernetes in Docker Desktop.

This lab comes before CI/CD and AWS.

## 🧰 Tools

- Docker Desktop
- Docker Desktop Kubernetes
- kubectl
- PowerShell
- Postman or browser

## 🪜 Part 1: Verify Kubernetes

Run:

```powershell
kubectl config use-context docker-desktop
kubectl get nodes
```

Expected:

```text
docker-desktop   Ready
```

If this does not work, enable Kubernetes in Docker Desktop first.

## 🪜 Part 2: Build Images

Run from project root:

```powershell
docker build -t auth-service:local .\services\auth-service
docker build -t product-service:local .\services\product-service
docker build -t order-service:local .\services\order-service
docker build -t microservices-frontend:local .\frontend
```

## 🪜 Part 3: Deploy To Kubernetes

```powershell
kubectl apply -f .\kubernetes\local
```

Watch pods:

```powershell
kubectl get pods -n microservices-local -w
```

Stop watching with `Ctrl+C` after pods are running.

## 🪜 Part 4: Test The App

Open:

```text
http://localhost:30080
```

Test API:

```text
http://localhost:30080/api/products
```

In Postman:

| Field | Value |
| --- | --- |
| Method | `GET` |
| URL | `http://localhost:30080/api/products` |

Expected:

```text
200 OK
```

## 🪜 Part 5: Debug Like DevOps

Check pods:

```powershell
kubectl get pods -n microservices-local
```

Check services:

```powershell
kubectl get svc -n microservices-local
```

Check gateway logs:

```powershell
kubectl logs deployment/gateway -n microservices-local
```

Check product service logs:

```powershell
kubectl logs deployment/product-service -n microservices-local
```

## 🧹 Cleanup

When finished:

```powershell
kubectl delete namespace microservices-local
```

## 🧠 What You Learned

- How Docker Desktop Kubernetes works locally
- How to deploy manifests with `kubectl apply`
- How Kubernetes Services give stable names
- How NodePort exposes the gateway locally
- How to inspect pods and logs

## 💾 Commit

```powershell
git add .
git commit -m "docs: add local kubernetes deployment guide"
```

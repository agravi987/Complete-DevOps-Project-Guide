# ☸️ Phase 13: Enable Kubernetes In Docker Desktop

Goal: turn on Kubernetes locally before learning CI/CD or AWS.

Docker Compose is great for local development. Kubernetes is the next level because it teaches how real container platforms run applications.

## 🧠 What You Are Doing

You are not deploying to cloud yet.

You are running a small Kubernetes cluster inside Docker Desktop on Windows.

```text
Windows
  |
  v
Docker Desktop
  |
  v
Local Kubernetes Cluster
  |
  v
Microservices App
```

## 🪜 Step 1: Enable Kubernetes

In Docker Desktop:

1. Open Docker Desktop.
2. Go to `Settings`.
3. Open `Kubernetes`.
4. Enable `Kubernetes`.
5. Click `Apply & Restart`.
6. Wait until Kubernetes shows as running.

This may take a few minutes the first time.

## 🪜 Step 2: Verify kubectl

Open PowerShell:

```powershell
kubectl version --client
kubectl config current-context
kubectl get nodes
```

Expected context:

```text
docker-desktop
```

Expected node:

```text
docker-desktop   Ready
```

## 🪜 Step 3: If Context Is Wrong

Run:

```powershell
kubectl config get-contexts
kubectl config use-context docker-desktop
kubectl get nodes
```

## 🧠 Kubernetes Concepts You Need

| Concept | Simple Meaning |
| --- | --- |
| Pod | Smallest running unit in Kubernetes |
| Deployment | Keeps pods running and recreates failed pods |
| Service | Stable network name for pods |
| ConfigMap | Non-secret configuration |
| Secret | Sensitive configuration |
| Namespace | Separate area inside the cluster |
| NodePort | Exposes an app on a local port |

## ✅ Checkpoint

Continue only when this works:

```powershell
kubectl get nodes
```

and the node status is:

```text
Ready
```


# ☸️ Local Kubernetes Deployment

This section lets you test deployment locally using Kubernetes in Docker Desktop before CI/CD and AWS.

## 🎯 Goal

By the end of this section, you will understand:

- How to enable Kubernetes in Docker Desktop
- How to verify `kubectl`
- How to build local Docker images for Kubernetes
- How to deploy PostgreSQL, Redis, services, frontend, and Nginx gateway
- How Kubernetes Deployments, Services, ConfigMaps, and Secrets work
- How to test the app through Kubernetes on your laptop
- How to clean up local Kubernetes resources

## 📖 Files In This Section

| Order | File | Hands-On Result |
| --- | --- | --- |
| 1 | [01-docker-desktop-kubernetes.md](01-docker-desktop-kubernetes.md) | Enable and verify Kubernetes |
| 2 | [02-local-kubernetes-deployment.md](02-local-kubernetes-deployment.md) | Deploy the full stack locally |

## 🧪 Matching Lab

- [Lab 07: Local Kubernetes Deployment](../../hands-on/07-local-kubernetes-lab.md)

## 📦 Kubernetes Manifests

Use these manifests:

[../../kubernetes/local](../../kubernetes/local)

## ✅ Section Checkpoint

You are ready for CI/CD when:

- `kubectl get nodes` shows `docker-desktop`.
- Local Docker images are built.
- Pods are running in namespace `microservices-local`.
- Gateway works at `http://localhost:30080`.
- You can test APIs through Kubernetes.


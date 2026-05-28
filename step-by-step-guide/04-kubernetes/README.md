# Local Kubernetes

Deploy the same project to Kubernetes on Docker Desktop.

Do this after Docker Compose and API testing work. Kubernetes should not be the first place where you discover app bugs.

## Phases

| Phase | Open | Finish with |
| --- | --- | --- |
| 13 | [Enable Kubernetes](01-docker-desktop-kubernetes.md) | Docker Desktop Kubernetes enabled and `kubectl` verified |
| 14 | [Deploy To Local Kubernetes](02-local-kubernetes-deployment.md) | Full stack running in namespace `microservices-local` |

## Manifests

The local Kubernetes YAML files are here:

[../../kubernetes/local](../../kubernetes/local)

## Section Checkpoint

Before moving to CI/CD:

- `kubectl get nodes` shows `docker-desktop`.
- Docker Hub images are pushed, or local images are built if you choose the local-only path.
- Kubernetes manifests use image names that match your chosen image source.
- Pods are running in `microservices-local`.
- Gateway works at `http://localhost:30080`.
- You can view pod logs with `kubectl logs`.

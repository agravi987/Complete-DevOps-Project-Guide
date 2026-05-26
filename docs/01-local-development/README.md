# 💻 Local Development

This section builds the project directly on your Windows machine before Docker or AWS.

## 🎯 Goal

By the end of this section, you will have:

- Node.js installed and verified
- A clean project folder structure
- Auth service running locally
- Product service running locally
- Order service running locally
- React frontend running locally

## 📖 Files In This Section

| Order | File | Hands-On Result |
| --- | --- | --- |
| 1 | [01-prerequisites.md](01-prerequisites.md) | Your Windows machine is ready |
| 2 | [02-project-structure.md](02-project-structure.md) | Project folders and root files exist |
| 3 | [03-auth-service.md](03-auth-service.md) | Auth API runs on port `3001` |
| 4 | [04-product-and-order-services.md](04-product-and-order-services.md) | Product and order APIs run |
| 5 | [05-frontend.md](05-frontend.md) | React frontend starts on port `5173` |

## 🧪 Matching Labs

- [Lab 01: Windows Setup](../../hands-on/01-windows-setup-lab.md)
- [Lab 02: Build First Microservice](../../hands-on/02-build-first-microservice-lab.md)

## ✅ Section Checkpoint

Before moving to Docker, confirm:

```text
http://localhost:3001/health
http://localhost:3002/health
http://localhost:3003/health
http://localhost:5173
```

# 🏗️ Architecture

The project is a small e-commerce style microservice system.

## 🧱 Services

| Component | Responsibility |
| --- | --- |
| Frontend | Browser UI built with React |
| Gateway | Nginx reverse proxy and single public entry point |
| Auth Service | User registration, login, and health check |
| Product Service | Product listing and product APIs |
| Order Service | Order creation and order APIs |
| PostgreSQL | Persistent relational data |
| Redis | Fast cache and temporary data |

## 💻 Local Architecture

```text
User Browser
  |
  | http://localhost:8080
  v
Nginx Gateway
  |
  +-- /api/auth     -> auth-service:3001
  +-- /api/products -> product-service:3002
  +-- /api/orders   -> order-service:3003
  +-- /             -> frontend:5173

auth-service/product-service/order-service
  |
  +-- postgres:5432
  +-- redis:6379
```

Important Docker rule:

Inside Docker Compose, containers talk to each other using service names, not `localhost`.

Examples:

```text
DB_HOST=postgres
REDIS_HOST=redis
AUTH_SERVICE_URL=http://auth-service:3001
```

From your Windows browser, you still use `localhost` because the browser is outside Docker:

```text
http://localhost:8080
```

## ☸️ Local Kubernetes Architecture

Docker Desktop Kubernetes uses the same app pieces, but Kubernetes manages them with Deployments and Services.

```text
User Browser
  |
  | http://localhost:30080
  v
gateway Service (NodePort)
  |
  v
gateway Deployment / Nginx Pod
  |
  +-- auth-service Service    -> auth-service Pod
  +-- product-service Service -> product-service Pod
  +-- order-service Service   -> order-service Pod
  +-- frontend Service        -> frontend Pod

backend Pods
  |
  +-- postgres Service -> postgres Pod + PVC
  +-- redis Service    -> redis Pod
```

Important Kubernetes rule:

Pods should talk to other apps through Kubernetes Service names.

Examples:

```text
POSTGRES_HOST=postgres
REDIS_HOST=redis
```

## ☁️ AWS Architecture Later

The AWS version follows the same idea:

```text
Internet
  |
  v
Application Load Balancer
  |
  v
ECS Fargate Services
  |
  +-- Auth Task
  +-- Product Task
  +-- Order Task
  +-- Frontend/Gateway Task
  |
  +-- RDS PostgreSQL
  +-- ElastiCache Redis
  +-- Secrets Manager
  +-- CloudWatch Logs
```

The local architecture helps you understand the cloud architecture before you spend money.

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

## System Overview

```mermaid
flowchart TB
    browser["User Browser"]:::external

    subgraph entry["Entry Point"]
        gateway["Nginx Gateway<br/>one public URL"]:::gateway
    end

    subgraph ui["User Interface"]
        frontend["React Frontend<br/>browser screens"]:::frontend
    end

    subgraph backend["Backend APIs"]
        auth["Auth Service<br/>users and sessions"]:::service
        product["Product Service<br/>catalog data"]:::service
        orders["Order Service<br/>checkout data"]:::service
    end

    subgraph storage["Stateful Services"]
        postgres[("PostgreSQL<br/>persistent records")]:::database
        redis[("Redis<br/>fast cached data")]:::cache
    end

    browser --> gateway
    gateway -- "web pages" --> frontend
    gateway -- "/api/auth" --> auth
    gateway -- "/api/products" --> product
    gateway -- "/api/orders" --> orders

    auth --> postgres
    product --> postgres
    orders --> postgres
    product -.-> redis
    orders -.-> redis

    classDef external fill:#f8fafc,stroke:#475569,color:#0f172a,stroke-width:2px;
    classDef gateway fill:#fff7ed,stroke:#ea580c,color:#7c2d12,stroke-width:2px;
    classDef frontend fill:#ecfeff,stroke:#0891b2,color:#164e63,stroke-width:2px;
    classDef service fill:#eef2ff,stroke:#4f46e5,color:#312e81,stroke-width:2px;
    classDef database fill:#ecfdf5,stroke:#059669,color:#064e3b,stroke-width:2px;
    classDef cache fill:#fef2f2,stroke:#dc2626,color:#7f1d1d,stroke-width:2px;
```

## 💻 Local Architecture

```mermaid
flowchart LR
    browser["Windows Browser<br/>http://localhost:8080"]:::external

    subgraph compose["Docker Compose Network"]
        gateway["gateway<br/>Nginx reverse proxy"]:::gateway
        frontend["frontend<br/>React :5173"]:::frontend

        subgraph apis["API Containers"]
            authSvc["auth-service<br/>Node.js :3001"]:::service
            productSvc["product-service<br/>Node.js :3002"]:::service
            orderSvc["order-service<br/>Node.js :3003"]:::service
        end

        subgraph data["Shared Data Containers"]
            postgres[("postgres<br/>PostgreSQL :5432")]:::database
            redis[("redis<br/>Redis :6379")]:::cache
        end
    end

    browser --> gateway
    gateway -- "/" --> frontend
    gateway -- "/api/auth" --> authSvc
    gateway -- "/api/products" --> productSvc
    gateway -- "/api/orders" --> orderSvc

    authSvc --> postgres
    productSvc --> postgres
    orderSvc --> postgres
    productSvc -.-> redis
    orderSvc -.-> redis

    classDef external fill:#f8fafc,stroke:#475569,color:#0f172a,stroke-width:2px;
    classDef gateway fill:#fff7ed,stroke:#ea580c,color:#7c2d12,stroke-width:2px;
    classDef frontend fill:#ecfeff,stroke:#0891b2,color:#164e63,stroke-width:2px;
    classDef service fill:#eef2ff,stroke:#4f46e5,color:#312e81,stroke-width:2px;
    classDef database fill:#ecfdf5,stroke:#059669,color:#064e3b,stroke-width:2px;
    classDef cache fill:#fef2f2,stroke:#dc2626,color:#7f1d1d,stroke-width:2px;
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

```mermaid
flowchart LR
    browser["User Browser<br/>http://localhost:30080"]:::external

    subgraph cluster["Docker Desktop Kubernetes Cluster"]
        nodePort["gateway Service<br/>NodePort 30080"]:::k8sService
        gatewayPod["gateway Deployment<br/>Nginx Pod"]:::gateway

        frontendSvc["frontend Service"]:::k8sService
        frontendPod["frontend Pod"]:::frontend

        authSvc["auth-service Service"]:::k8sService
        authPod["auth-service Pod"]:::pod

        productSvc["product-service Service"]:::k8sService
        productPod["product-service Pod"]:::pod

        orderSvc["order-service Service"]:::k8sService
        orderPod["order-service Pod"]:::pod

        postgresSvc["postgres Service"]:::k8sService
        postgresPod[("postgres Pod<br/>PVC attached")]:::database

        redisSvc["redis Service"]:::k8sService
        redisPod[("redis Pod")]:::cache
    end

    browser --> nodePort
    nodePort --> gatewayPod
    gatewayPod -- "/" --> frontendSvc
    frontendSvc --> frontendPod
    gatewayPod -- "/api/auth" --> authSvc
    authSvc --> authPod
    gatewayPod -- "/api/products" --> productSvc
    productSvc --> productPod
    gatewayPod -- "/api/orders" --> orderSvc
    orderSvc --> orderPod

    authPod --> postgresSvc
    postgresSvc --> postgresPod
    productPod --> postgresSvc
    orderPod --> postgresSvc
    productPod -.-> redisSvc
    orderPod -.-> redisSvc
    redisSvc --> redisPod

    classDef external fill:#f8fafc,stroke:#475569,color:#0f172a,stroke-width:2px;
    classDef gateway fill:#fff7ed,stroke:#ea580c,color:#7c2d12,stroke-width:2px;
    classDef frontend fill:#ecfeff,stroke:#0891b2,color:#164e63,stroke-width:2px;
    classDef k8sService fill:#f0f9ff,stroke:#0284c7,color:#075985,stroke-width:2px;
    classDef pod fill:#eef2ff,stroke:#4f46e5,color:#312e81,stroke-width:2px;
    classDef database fill:#ecfdf5,stroke:#059669,color:#064e3b,stroke-width:2px;
    classDef cache fill:#fef2f2,stroke:#dc2626,color:#7f1d1d,stroke-width:2px;
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

```mermaid
flowchart LR
    internet["Internet"]:::external

    subgraph aws["AWS Region"]
        alb["Application Load Balancer"]:::gateway

        subgraph ecs["ECS Fargate Services"]
            gatewayTask["Frontend + Gateway Task"]:::frontend
            authTask["Auth Task"]:::service
            productTask["Product Task"]:::service
            orderTask["Order Task"]:::service
        end

        subgraph managed["Managed Data"]
            rds[("RDS PostgreSQL")]:::database
            elasticache[("ElastiCache Redis")]:::cache
        end

        subgraph ops["Operations and Security"]
            secrets["Secrets Manager"]:::security
            logs["CloudWatch Logs"]:::observability
        end
    end

    internet --> alb
    alb --> gatewayTask
    gatewayTask -- "/api/auth" --> authTask
    gatewayTask -- "/api/products" --> productTask
    gatewayTask -- "/api/orders" --> orderTask

    authTask --> rds
    productTask --> rds
    orderTask --> rds
    productTask -.-> elasticache
    orderTask -.-> elasticache

    authTask -.-> secrets
    productTask -.-> secrets
    orderTask -.-> secrets
    gatewayTask -.-> logs
    authTask -.-> logs
    productTask -.-> logs
    orderTask -.-> logs

    classDef external fill:#f8fafc,stroke:#475569,color:#0f172a,stroke-width:2px;
    classDef gateway fill:#fff7ed,stroke:#ea580c,color:#7c2d12,stroke-width:2px;
    classDef frontend fill:#ecfeff,stroke:#0891b2,color:#164e63,stroke-width:2px;
    classDef service fill:#eef2ff,stroke:#4f46e5,color:#312e81,stroke-width:2px;
    classDef database fill:#ecfdf5,stroke:#059669,color:#064e3b,stroke-width:2px;
    classDef cache fill:#fef2f2,stroke:#dc2626,color:#7f1d1d,stroke-width:2px;
    classDef security fill:#fdf4ff,stroke:#c026d3,color:#701a75,stroke-width:2px;
    classDef observability fill:#fefce8,stroke:#ca8a04,color:#713f12,stroke-width:2px;
```

The local architecture helps you understand the cloud architecture before you spend money.

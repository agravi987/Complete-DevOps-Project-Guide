# 🐳 Containers And Local Infrastructure

This section turns your local apps into a real multi-container system.

## 🎯 Goal

By the end of this section, you will have:

- Docker images for each service
- PostgreSQL running in Docker
- Redis running in Docker
- Nginx gateway routing traffic
- Persistent database storage
- Redis product caching
- A daily local DevOps workflow

## 📖 Files In This Section

| Order | File | Hands-On Result |
| --- | --- | --- |
| 1 | [01-dockerize-services.md](01-dockerize-services.md) | Build Docker images |
| 2 | [02-docker-compose-postgres-redis.md](02-docker-compose-postgres-redis.md) | Run services, PostgreSQL, and Redis together |
| 3 | [03-nginx-gateway.md](03-nginx-gateway.md) | Access everything through `localhost:8080` |
| 4 | [04-local-dev-workflow.md](04-local-dev-workflow.md) | Use logs, shell, rebuild, and reset commands |
| 5 | [05-database-integration.md](05-database-integration.md) | Persist users, products, and orders |
| 6 | [06-redis-cache.md](06-redis-cache.md) | Cache product data in Redis |

## 🧪 Matching Labs

- [Lab 03: Docker Compose Stack](../../hands-on/03-docker-compose-stack-lab.md)
- [Lab 04: Nginx Gateway](../../hands-on/04-nginx-gateway-lab.md)
- [Lab 05: Database And Redis](../../hands-on/05-database-and-cache-lab.md)

## ✅ Section Checkpoint

Your local system is ready when these work:

```text
http://localhost:8080
http://localhost:8080/api/auth/health
http://localhost:8080/api/products
http://localhost:8080/api/orders
```

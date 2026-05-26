# Containers And Local Infrastructure

Turn the local app into a multi-container system.

Finish local development first. This section assumes the backend services and frontend already run without Docker.

## PowerShell File And Folder Commands

Use these direct commands whenever a phase says to create a folder or file:

```powershell
New-Item -ItemType Directory -Path .\folder-name
New-Item -ItemType File -Path .\folder-name\file-name.txt
```

## Phases

| Phase | Open | Finish with |
| --- | --- | --- |
| 6 | [Dockerize Services](01-dockerize-services.md) | Dockerfiles and images for backend services and frontend |
| 7 | [Docker Compose Stack](02-docker-compose-postgres-redis.md) | PostgreSQL, Redis, services, and frontend started together |
| 8 | [Nginx Gateway](03-nginx-gateway.md) | One browser/API entry point at `localhost:8080` |
| 9 | [Local Dev Workflow](04-local-dev-workflow.md) | Daily Docker commands for logs, rebuilds, shells, ports, and resets |
| 10 | [Database Integration](05-database-integration.md) | Services reading and writing real PostgreSQL data |
| 11 | [Redis Caching](06-redis-cache.md) | Product data cached in Redis |

## Section Checkpoint

Before moving to API testing, these should work:

```text
http://localhost:8080
http://localhost:8080/api/auth/health
http://localhost:8080/api/products
http://localhost:8080/api/orders
```

Also confirm:

```powershell
docker compose ps
docker compose logs auth-service
docker compose logs product-service
docker compose logs order-service
```

# 🚀 Complete Microservice DevOps Project Guide

This repository is my complete DevOps project reference.

It is designed for real hands-on learning on Windows first, then Docker, CI/CD, and AWS step by step.

The goal is simple:

> Build locally. Containerize it. Automate it. Deploy it. Understand every step.

## 🧭 Start Here

If you are new, follow this order:

1. Read [docs/00-start-here.md](docs/00-start-here.md)
2. Follow the documentation in [docs/README.md](docs/README.md)
3. Practice using [hands-on/README.md](hands-on/README.md)
4. Use [docs/reference/README.md](docs/reference/README.md) whenever you get stuck

## 🏗️ What You Will Build

You will build a small production-style microservice system:

| Component | Purpose |
| --- | --- |
| ⚛️ React Frontend | User interface |
| 🌐 Nginx Gateway | Single entry point and reverse proxy |
| 🔐 Auth Service | Register, login, JWT basics |
| 📦 Product Service | Product APIs |
| 🧾 Order Service | Order APIs |
| 🐘 PostgreSQL | Persistent database |
| ⚡ Redis | Cache layer |
| 🐳 Docker | Containerize services |
| 🧩 Docker Compose | Run the full stack locally |
| 🚀 GitHub Actions | CI checks |
| ☁️ AWS | ECR, ECS Fargate, RDS, ElastiCache, Secrets Manager |

## 🧱 Architecture

```text
Browser
  |
  v
React Frontend
  |
  v
Nginx Gateway
  |
  +--> Auth Service
  |
  +--> Product Service
  |
  +--> Order Service
          |
          v
PostgreSQL + Redis
```

Detailed explanation:

[docs/reference/architecture.md](docs/reference/architecture.md)

## 🗂️ Repository Structure

```text
.
├── docs/
│   ├── 00-start-here.md
│   ├── 01-local-development/
│   ├── 02-containers/
│   ├── 03-ci-cd/
│   ├── 04-aws/
│   └── reference/
│
├── hands-on/
│   ├── 01-windows-setup-lab.md
│   ├── 02-build-first-microservice-lab.md
│   ├── 03-docker-compose-stack-lab.md
│   ├── 04-nginx-gateway-lab.md
│   ├── 05-database-and-cache-lab.md
│   ├── 06-ci-cd-lab.md
│   └── 07-aws-first-deployment-lab.md
│
└── templates/
    ├── aws/
    └── github-actions/
```

## 📚 Learning Roadmap

Follow the phases in order.

| Phase | Guide | Hands-On Result |
| --- | --- | --- |
| 0 | [Start Here](docs/00-start-here.md) | Understand how to use the repo |
| 1 | [Windows Prerequisites](docs/01-local-development/01-prerequisites.md) | Install and verify tools |
| 2 | [Project Structure](docs/01-local-development/02-project-structure.md) | Create a clean monorepo |
| 3 | [Auth Service](docs/01-local-development/03-auth-service.md) | Run first API locally |
| 4 | [Product and Order Services](docs/01-local-development/04-product-and-order-services.md) | Add more microservices |
| 5 | [Frontend](docs/01-local-development/05-frontend.md) | Start React UI |
| 6 | [Dockerize Services](docs/02-containers/01-dockerize-services.md) | Build Docker images |
| 7 | [Docker Compose](docs/02-containers/02-docker-compose-postgres-redis.md) | Run app, DB, and cache together |
| 8 | [Nginx Gateway](docs/02-containers/03-nginx-gateway.md) | Use one entry point |
| 9 | [Daily Workflow](docs/02-containers/04-local-dev-workflow.md) | Debug with logs and commands |
| 10 | [Database Integration](docs/02-containers/05-database-integration.md) | Persist real data |
| 11 | [Redis Caching](docs/02-containers/06-redis-cache.md) | Cache products |
| 12 | [Git and GitHub](docs/03-ci-cd/01-git-github.md) | Push code professionally |
| 13 | [GitHub Actions CI](docs/03-ci-cd/02-github-actions-ci.md) | Run automated checks |
| 14 | [AWS Foundation](docs/04-aws/01-aws-foundation.md) | Prepare AWS safely |
| 15 | [ECR and ECS Fargate](docs/04-aws/02-ecr-and-ecs-fargate.md) | Deploy first container |
| 16 | [Managed AWS Services](docs/04-aws/03-rds-elasticache-secrets.md) | Use RDS, Redis, secrets |
| 17 | [Cleanup](docs/04-aws/04-cleanup.md) | Stop AWS costs |

## 🧪 Hands-On Labs

Use these when you want practical tasks instead of reading only:

- [Lab 01: Windows Setup](hands-on/01-windows-setup-lab.md)
- [Lab 02: Build First Microservice](hands-on/02-build-first-microservice-lab.md)
- [Lab 03: Docker Compose Stack](hands-on/03-docker-compose-stack-lab.md)
- [Lab 04: Nginx Gateway](hands-on/04-nginx-gateway-lab.md)
- [Lab 05: Database And Cache](hands-on/05-database-and-cache-lab.md)
- [Lab 06: CI/CD](hands-on/06-ci-cd-lab.md)
- [Lab 07: AWS First Deployment](hands-on/07-aws-first-deployment-lab.md)

## ✅ Beginner Rules

- 🪟 Use PowerShell on Windows unless a step says otherwise.
- 📍 Run commands from the folder shown in each step.
- 🔐 Never commit real passwords, AWS keys, or `.env` files.
- 💾 Commit after every working phase.
- 🧪 Test locally before AWS.
- 🧹 Delete AWS resources after practice.

## 🧰 Quick Reference

| Need | Go Here |
| --- | --- |
| Forgot a command | [Commands Cheat Sheet](docs/reference/commands-cheatsheet.md) |
| Need the project folder map | [Project Folder Map](docs/reference/project-folder-map.md) |
| Something broke | [Troubleshooting](docs/reference/troubleshooting.md) |
| Confused by a term | [Glossary](docs/reference/glossary.md) |
| Need environment variables | [Environment Variables](docs/reference/environment-variables.md) |
| Want to track progress | [Progress Tracker](docs/reference/progress-tracker.md) |
| Need official docs | [Official Links](docs/reference/official-links.md) |

## 🧠 Version Notes

This guide was prepared on May 26, 2026.

- Node.js examples use Node.js 24 LTS.
- Docker Compose commands use the modern `docker compose` syntax.
- AWS examples use AWS CLI v2.

If you read this much later, check official version docs before using the same versions in a production project.

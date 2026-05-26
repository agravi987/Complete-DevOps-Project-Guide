# 🗓️ Beginner Study Plan

Use this plan if you want a clear learning path instead of deciding what to do each day.

## Day 1: Setup

Goal:

- Install tools
- Verify PowerShell commands
- Create project folder

Do:

- [docs/01-local-development/01-prerequisites.md](../01-local-development/01-prerequisites.md)
- [hands-on/01-windows-setup-lab.md](../../hands-on/01-windows-setup-lab.md)

## Day 2: First API

Goal:

- Build auth service
- Understand health checks
- Test register and login

Do:

- [docs/01-local-development/03-auth-service.md](../01-local-development/03-auth-service.md)
- [hands-on/02-build-first-microservice-lab.md](../../hands-on/02-build-first-microservice-lab.md)

## Day 3: More Services

Goal:

- Add product service
- Add order service
- Run multiple services locally

Do:

- [docs/01-local-development/04-product-and-order-services.md](../01-local-development/04-product-and-order-services.md)

## Day 4: Docker

Goal:

- Create Dockerfiles
- Build and run containers

Do:

- [docs/02-containers/01-dockerize-services.md](../02-containers/01-dockerize-services.md)

## Day 5: Docker Compose

Goal:

- Run services, PostgreSQL, Redis, and frontend together

Do:

- [docs/02-containers/02-docker-compose-postgres-redis.md](../02-containers/02-docker-compose-postgres-redis.md)
- [hands-on/03-docker-compose-stack-lab.md](../../hands-on/03-docker-compose-stack-lab.md)

## Day 6: Gateway

Goal:

- Add Nginx
- Use one entry point

Do:

- [docs/02-containers/03-nginx-gateway.md](../02-containers/03-nginx-gateway.md)
- [hands-on/04-nginx-gateway-lab.md](../../hands-on/04-nginx-gateway-lab.md)

## Day 7: Database And Cache

Goal:

- Persist data in PostgreSQL
- Cache product data in Redis

Do:

- [docs/02-containers/05-database-integration.md](../02-containers/05-database-integration.md)
- [docs/02-containers/06-redis-cache.md](../02-containers/06-redis-cache.md)
- [hands-on/05-database-and-cache-lab.md](../../hands-on/05-database-and-cache-lab.md)

## Day 8: Postman Testing

Goal:

- Test one API at a time
- Understand status codes
- Test gateway APIs

Do:

- [docs/03-api-testing/01-postman-api-testing.md](../03-api-testing/01-postman-api-testing.md)
- [hands-on/06-postman-api-testing-lab.md](../../hands-on/06-postman-api-testing-lab.md)

## Day 9: Local Kubernetes

Goal:

- Enable Docker Desktop Kubernetes
- Deploy the stack locally with `kubectl`
- Test the app through `localhost:30080`

Do:

- [docs/04-kubernetes/01-docker-desktop-kubernetes.md](../04-kubernetes/01-docker-desktop-kubernetes.md)
- [docs/04-kubernetes/02-local-kubernetes-deployment.md](../04-kubernetes/02-local-kubernetes-deployment.md)
- [hands-on/07-local-kubernetes-lab.md](../../hands-on/07-local-kubernetes-lab.md)

## Day 10: CI/CD

Goal:

- Push to GitHub
- Add GitHub Actions

Do:

- [docs/05-ci-cd/01-git-github.md](../05-ci-cd/01-git-github.md)
- [docs/05-ci-cd/02-github-actions-ci.md](../05-ci-cd/02-github-actions-ci.md)
- [hands-on/08-ci-cd-lab.md](../../hands-on/08-ci-cd-lab.md)

## Day 11: AWS First Deployment

Goal:

- Push image to ECR
- Run first ECS Fargate service
- Clean up resources

Do:

- [docs/06-aws/01-aws-foundation.md](../06-aws/01-aws-foundation.md)
- [docs/06-aws/02-ecr-and-ecs-fargate.md](../06-aws/02-ecr-and-ecs-fargate.md)
- [hands-on/09-aws-first-deployment-lab.md](../../hands-on/09-aws-first-deployment-lab.md)
- [docs/06-aws/04-cleanup.md](../06-aws/04-cleanup.md)

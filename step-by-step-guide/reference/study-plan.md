# Beginner Study Plan

Use this plan when you want a day-by-day schedule. It uses the same workbook phases as the main README.

Do not look for a second checklist after each topic. The phase page already includes the build work and verification.

## Day 1: Setup And Structure

Goal:

- Install required tools.
- Verify commands in PowerShell.
- Create the project folder structure.

Do:

- [Windows Prerequisites](../01-local-development/01-prerequisites.md)
- [Project Structure](../01-local-development/02-project-structure.md)

## Day 2: First API

Goal:

- Build the auth service.
- Test health, register, and login.
- Commit the working service.

Do:

- [Auth Service](../01-local-development/03-auth-service.md)

## Day 3: More Services And Frontend

Goal:

- Add product service.
- Add order service.
- Add the React frontend.

Do:

- [Product And Order Services](../01-local-development/04-product-and-order-services.md)
- [Frontend](../01-local-development/05-frontend.md)

## Day 4: Docker Images

Goal:

- Add Dockerfiles.
- Build and run containers directly.

Do:

- [Dockerize Services](../02-containers/01-dockerize-services.md)

## Day 5: Docker Compose

Goal:

- Start PostgreSQL, Redis, backend services, and frontend together.
- Verify containers and logs.

Do:

- [Docker Compose Stack](../02-containers/02-docker-compose-postgres-redis.md)
- [Local Dev Workflow](../02-containers/04-local-dev-workflow.md)

## Day 6: Gateway

Goal:

- Add Nginx.
- Test APIs through one local entry point.

Do:

- [Nginx Gateway](../02-containers/03-nginx-gateway.md)

## Day 7: Database And Cache

Goal:

- Persist app data in PostgreSQL.
- Cache product data in Redis.

Do:

- [Database Integration](../02-containers/05-database-integration.md)
- [Redis Caching](../02-containers/06-redis-cache.md)

## Day 8: API Testing

Goal:

- Test each API in Postman.
- Optionally run the small Python API checks.

Do:

- [Postman API Testing](../03-api-testing/01-postman-api-testing.md)
- [Python API Testing](../03-api-testing/02-python-api-testing.md)

## Day 9: Local Kubernetes

Goal:

- Enable Docker Desktop Kubernetes.
- Deploy and test the stack with `kubectl`.

Do:

- [Enable Kubernetes](../04-kubernetes/01-docker-desktop-kubernetes.md)
- [Deploy To Local Kubernetes](../04-kubernetes/02-local-kubernetes-deployment.md)

## Day 10: GitHub And CI

Goal:

- Push the project to GitHub.
- Add GitHub Actions.
- Confirm CI runs.

Do:

- [Git And GitHub](../05-ci-cd/01-git-github.md)
- [GitHub Actions CI](../05-ci-cd/02-github-actions-ci.md)

## Day 11: AWS First Deployment

Goal:

- Prepare AWS safely.
- Push an image to ECR.
- Run the first ECS Fargate task.
- Clean up resources.

Do:

- [AWS Foundation](../06-aws/01-aws-foundation.md)
- [ECR And ECS Fargate](../06-aws/02-ecr-and-ecs-fargate.md)
- [AWS Cleanup](../06-aws/04-cleanup.md)

## Day 12: Managed Services

Goal:

- Understand how the local PostgreSQL, Redis, and `.env` values become AWS managed services.

Do:

- [RDS, ElastiCache, And Secrets](../06-aws/03-rds-elasticache-secrets.md)
- [AWS Cleanup](../06-aws/04-cleanup.md)

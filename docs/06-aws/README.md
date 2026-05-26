# ☁️ AWS Deployment Path

This section shows how the local project can grow into an AWS deployment.

Before starting AWS, complete the local Kubernetes section:

[../04-kubernetes/README.md](../04-kubernetes/README.md)

## 🎯 Goal

By the end of this section, you will understand:

- AWS account preparation
- Cost safety basics
- ECR image repositories
- ECS Fargate container deployment
- RDS PostgreSQL
- ElastiCache Redis
- Secrets Manager
- CloudWatch logs
- Cleanup steps

## 📖 Files In This Section

| Order | File | Hands-On Result |
| --- | --- | --- |
| 1 | [01-aws-foundation.md](01-aws-foundation.md) | AWS CLI, region, identity, budget |
| 2 | [02-ecr-and-ecs-fargate.md](02-ecr-and-ecs-fargate.md) | Push images and run first ECS service |
| 3 | [03-rds-elasticache-secrets.md](03-rds-elasticache-secrets.md) | Move database, cache, and secrets to AWS |
| 4 | [04-cleanup.md](04-cleanup.md) | Delete resources to stop costs |

## 🧪 Matching Lab

- [Lab 09: First AWS Deployment](../../hands-on/09-aws-first-deployment-lab.md)

## ⚠️ Cost Reminder

AWS can charge money while resources are running. Always finish practice by following:

[04-cleanup.md](04-cleanup.md)

# 🧹 Phase 20: AWS Cleanup

Goal: remove AWS resources when you finish practicing.

Cleanup is part of DevOps. A running unused resource can keep charging your account.

## 🪜 Delete In This Order

1. ECS services
2. ECS tasks
3. Application Load Balancer listeners
4. Application Load Balancer
5. Target groups
6. ECS cluster
7. RDS database
8. ElastiCache cluster
9. Secrets Manager secrets
10. CloudWatch log groups
11. ECR repositories
12. Extra NAT gateways or Elastic IPs if you created them

## 🚀 ECS Cleanup

Scale service to zero:

```powershell
aws ecs update-service `
  --cluster microservices-dev `
  --service <service-name> `
  --desired-count 0 `
  --region $env:AWS_REGION
```

Delete service:

```powershell
aws ecs delete-service `
  --cluster microservices-dev `
  --service <service-name> `
  --force `
  --region $env:AWS_REGION
```

Delete cluster after services are gone:

```powershell
aws ecs delete-cluster `
  --cluster microservices-dev `
  --region $env:AWS_REGION
```

## 📦 ECR Cleanup

Delete repositories and images:

```powershell
aws ecr delete-repository `
  --repository-name microservices/auth-service `
  --force `
  --region $env:AWS_REGION

aws ecr delete-repository `
  --repository-name microservices/product-service `
  --force `
  --region $env:AWS_REGION

aws ecr delete-repository `
  --repository-name microservices/order-service `
  --force `
  --region $env:AWS_REGION

aws ecr delete-repository `
  --repository-name microservices/frontend `
  --force `
  --region $env:AWS_REGION

aws ecr delete-repository `
  --repository-name microservices/gateway `
  --force `
  --region $env:AWS_REGION
```

## 🐘 RDS Cleanup

In the RDS console:

1. Select the database.
2. Choose delete.
3. For practice projects, skip final snapshot only if you do not need the data.
4. Confirm deletion.

Production projects should usually keep a final snapshot.

## ⚡ ElastiCache Cleanup

In the ElastiCache console:

1. Select the cache.
2. Delete it.
3. Confirm subnet groups and security groups if you created custom ones.

## 📜 CloudWatch Logs Cleanup

List log groups:

```powershell
aws logs describe-log-groups `
  --log-group-name-prefix /ecs `
  --region $env:AWS_REGION
```

Delete a log group:

```powershell
aws logs delete-log-group `
  --log-group-name <log-group-name> `
  --region $env:AWS_REGION
```

## 💰 Final Billing Check

After cleanup:

1. Open AWS Billing.
2. Check current month costs.
3. Check Cost Explorer after a few hours.
4. Confirm no unexpected resources are still running.

## ✅ Checkpoint

You are done when:

- No ECS services are running.
- No RDS or ElastiCache resources remain for this project.
- No ALB, NAT Gateway, or Elastic IP remains accidentally.
- ECR repositories are deleted if you no longer need them.

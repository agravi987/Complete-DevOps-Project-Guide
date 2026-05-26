# 🚢 Phase 18: ECR And ECS Fargate

Goal: push Docker images to Amazon ECR and run containers on ECS Fargate.

Start with one service first. After that works, expand to the full stack.

## 🔧 Set Variables

Run in PowerShell:

```powershell
$env:AWS_REGION="ap-south-1"
$env:AWS_ACCOUNT_ID=(aws sts get-caller-identity --query Account --output text)
$env:ECR_REGISTRY="$env:AWS_ACCOUNT_ID.dkr.ecr.$env:AWS_REGION.amazonaws.com"
```

Change the region if needed.

## 📦 Create ECR Repositories

```powershell
aws ecr create-repository `
  --repository-name microservices/auth-service `
  --image-scanning-configuration scanOnPush=true `
  --region $env:AWS_REGION

aws ecr create-repository `
  --repository-name microservices/product-service `
  --image-scanning-configuration scanOnPush=true `
  --region $env:AWS_REGION

aws ecr create-repository `
  --repository-name microservices/order-service `
  --image-scanning-configuration scanOnPush=true `
  --region $env:AWS_REGION

aws ecr create-repository `
  --repository-name microservices/frontend `
  --image-scanning-configuration scanOnPush=true `
  --region $env:AWS_REGION

aws ecr create-repository `
  --repository-name microservices/gateway `
  --image-scanning-configuration scanOnPush=true `
  --region $env:AWS_REGION
```

If a repository already exists, AWS returns an error. That is okay; continue.

## 🔐 Login Docker To ECR

```powershell
aws ecr get-login-password --region $env:AWS_REGION |
  docker login --username AWS --password-stdin $env:ECR_REGISTRY
```

The login token is temporary.

## 🏗️ Build, Tag, And Push Images

Auth service:

```powershell
docker build -t auth-service:local .\services\auth-service
docker tag auth-service:local "$env:ECR_REGISTRY/microservices/auth-service:v1"
docker push "$env:ECR_REGISTRY/microservices/auth-service:v1"
```

Product service:

```powershell
docker build -t product-service:local .\services\product-service
docker tag product-service:local "$env:ECR_REGISTRY/microservices/product-service:v1"
docker push "$env:ECR_REGISTRY/microservices/product-service:v1"
```

Order service:

```powershell
docker build -t order-service:local .\services\order-service
docker tag order-service:local "$env:ECR_REGISTRY/microservices/order-service:v1"
docker push "$env:ECR_REGISTRY/microservices/order-service:v1"
```

Frontend:

```powershell
docker build -t microservices-frontend:local .\frontend
docker tag microservices-frontend:local "$env:ECR_REGISTRY/microservices/frontend:v1"
docker push "$env:ECR_REGISTRY/microservices/frontend:v1"
```

Gateway:

```powershell
docker build -t microservices-gateway:local .\gateway
docker tag microservices-gateway:local "$env:ECR_REGISTRY/microservices/gateway:v1"
docker push "$env:ECR_REGISTRY/microservices/gateway:v1"
```

## 🚀 Create ECS Cluster

```powershell
aws ecs create-cluster `
  --cluster-name microservices-dev `
  --region $env:AWS_REGION
```

Create a CloudWatch log group for the first service:

```powershell
aws logs create-log-group `
  --log-group-name /ecs/auth-service `
  --region $env:AWS_REGION
```

If it already exists, continue.

## 🔑 Create ECS Task Execution Role

Create `templates/aws/ecs-task-execution-assume-role.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "ecs-tasks.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Create role:

```powershell
aws iam create-role `
  --role-name ecsTaskExecutionRole `
  --assume-role-policy-document file://templates/aws/ecs-task-execution-assume-role.json
```

Attach AWS managed policy:

```powershell
aws iam attach-role-policy `
  --role-name ecsTaskExecutionRole `
  --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy
```

If the role already exists, keep using it.

## 🪜 Beginner First Deployment

For the first AWS run, deploy only the auth service.

Use ECS console:

1. Open Amazon ECS.
2. Choose `Clusters`.
3. Open `microservices-dev`.
4. Create a task definition.
5. Launch type: `AWS Fargate`.
6. Container image: `$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/microservices/auth-service:v1`.
7. Container port: `3001`.
8. CPU: `0.25 vCPU`.
9. Memory: `0.5 GB`.
10. Task execution role: `ecsTaskExecutionRole`.
11. Enable CloudWatch logs.
12. Create a service from the task definition.

For the first practice service only:

- You may use public subnets.
- Enable public IP.
- Security group inbound can allow port `3001` from your IP only.

This is a learning-only shortcut. For a more production-like setup, put tasks in private subnets and expose only an Application Load Balancer.

## 🧪 Test First Service

After ECS starts the task, find its public IP in the ECS task networking details.

Open:

```text
http://<task-public-ip>:3001/health
```

Expected:

```json
{
  "service": "auth-service",
  "status": "OK"
}
```

## 🌐 Production-Like Next Step: Application Load Balancer

After one service works, move to an Application Load Balancer.

Create target groups:

| Target group | Port | Health check |
| --- | --- | --- |
| auth-tg | 3001 | `/health` |
| product-tg | 3002 | `/health` |
| order-tg | 3003 | `/health` |
| frontend-tg | 5173 | `/` |

Create listener rules:

| Path | Target |
| --- | --- |
| `/api/auth/*` | auth service |
| `/api/products*` | product service |
| `/api/orders*` | order service |
| `/*` | frontend or gateway |

In a production-style setup:

- ALB is public.
- ECS tasks are private.
- RDS and ElastiCache are private.
- Security groups allow only the needed traffic.

## 📜 Check Logs

Open CloudWatch Logs and find the log group created by ECS.

Good logs should show:

```text
Auth service running on port 3001
```

## ✅ Checkpoint

You are ready when:

- Images exist in ECR.
- ECS cluster exists.
- At least one service runs on Fargate.
- `/health` works from the public endpoint or load balancer.

## Next Phase

[Phase 19: RDS, ElastiCache, And Secrets](03-rds-elasticache-secrets.md)

# 🧪 Lab 08: First AWS Deployment

## 🎯 Objective

Push one Docker image to Amazon ECR and run it on ECS Fargate.

This lab starts with only the auth service so the first cloud step stays understandable.

## ⚠️ Cost Warning

AWS resources can cost money.

Before starting:

- Create a budget alert.
- Use one region.
- Delete resources after the lab.
- Follow [../docs/05-aws/04-cleanup.md](../docs/05-aws/04-cleanup.md).

## 🧰 Tools

- AWS CLI v2
- Docker Desktop
- Amazon ECR
- Amazon ECS Fargate
- CloudWatch Logs

## 🪜 Steps

Set variables:

```powershell
$env:AWS_REGION="ap-south-1"
$env:AWS_ACCOUNT_ID=(aws sts get-caller-identity --query Account --output text)
$env:ECR_REGISTRY="$env:AWS_ACCOUNT_ID.dkr.ecr.$env:AWS_REGION.amazonaws.com"
```

Create ECR repository:

```powershell
aws ecr create-repository `
  --repository-name microservices/auth-service `
  --image-scanning-configuration scanOnPush=true `
  --region $env:AWS_REGION
```

Login Docker to ECR:

```powershell
aws ecr get-login-password --region $env:AWS_REGION |
  docker login --username AWS --password-stdin $env:ECR_REGISTRY
```

Build and push image:

```powershell
docker build -t auth-service:local .\services\auth-service
docker tag auth-service:local "$env:ECR_REGISTRY/microservices/auth-service:v1"
docker push "$env:ECR_REGISTRY/microservices/auth-service:v1"
```

Create ECS cluster:

```powershell
aws ecs create-cluster `
  --cluster-name microservices-dev `
  --region $env:AWS_REGION
```

Continue the ECS task and service setup from:

[../docs/05-aws/02-ecr-and-ecs-fargate.md](../docs/05-aws/02-ecr-and-ecs-fargate.md)

## ✅ Expected Output

ECR should contain:

```text
microservices/auth-service:v1
```

ECS should show:

```text
Cluster: microservices-dev
Service: running
Task: running
```

## 🧪 Verification

Open the auth service health endpoint:

```text
http://<task-public-ip>:3001/health
```

Expected response:

```json
{
  "service": "auth-service",
  "status": "OK"
}
```

Check CloudWatch logs and confirm the service started.

## 🧠 What You Learned

- How a Docker image moves from laptop to ECR
- How ECS Fargate runs a container
- Why CloudWatch logs matter
- Why cleanup is part of the lab

## 🧹 Cleanup

Follow:

[../docs/05-aws/04-cleanup.md](../docs/05-aws/04-cleanup.md)

Do not leave practice resources running.

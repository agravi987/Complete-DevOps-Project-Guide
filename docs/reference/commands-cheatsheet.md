# Commands Cheat Sheet

Use this file when you forget a command.

## Project

```powershell
cd C:\dev\microservices-project
code .
```

## Node.js

```powershell
npm install
npm run dev
npm start
```

## Docker

```powershell
docker --version
docker images
docker ps
docker ps -a
docker logs <container-name>
docker stop <container-name>
docker rm <container-name>
```

## Docker Build And Run

```powershell
docker build -t auth-service:local .\services\auth-service
docker run --rm -p 3001:3001 auth-service:local
```

## Docker Compose

```powershell
docker compose up --build
docker compose up --build -d
docker compose ps
docker compose logs -f
docker compose logs -f auth-service
docker compose down
docker compose down -v
```

## PostgreSQL In Container

```powershell
docker exec -it microservices-postgres psql -U app_user -d microservices_db
```

Inside `psql`:

```sql
\dt
SELECT * FROM users;
SELECT * FROM products;
SELECT * FROM orders;
\q
```

## Git

```powershell
git status
git add .
git commit -m "feat: add useful change"
git push
git pull
git log --oneline
```

## AWS

```powershell
aws --version
aws sts get-caller-identity
$env:AWS_REGION="ap-south-1"
$env:AWS_ACCOUNT_ID=(aws sts get-caller-identity --query Account --output text)
```

## ECR Login

```powershell
$env:ECR_REGISTRY="$env:AWS_ACCOUNT_ID.dkr.ecr.$env:AWS_REGION.amazonaws.com"

aws ecr get-login-password --region $env:AWS_REGION |
  docker login --username AWS --password-stdin $env:ECR_REGISTRY
```

# 🧰 Commands Cheat Sheet

Use this file when you forget a command.

## 🗂️ Project

```powershell
cd C:\dev\microservices-project
code .
```

## 🟢 Node.js

```powershell
npm install
npm run dev
npm start
```

## 🐳 Docker

```powershell
docker --version
docker images
docker ps
docker ps -a
docker logs <container-name>
docker stop <container-name>
docker rm <container-name>
```

## 🏗️ Docker Build And Run

```powershell
docker build -t auth-service:local .\services\auth-service
docker run --rm -p 3001:3001 auth-service:local
```

## 🧩 Docker Compose

```powershell
docker compose up --build
docker compose up --build -d
docker compose ps
docker compose logs -f
docker compose logs -f auth-service
docker compose down
docker compose down -v
```

## 🐘 PostgreSQL In Container

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

## 📬 Postman

Create one request at a time:

```text
GET http://localhost:3001/health
POST http://localhost:3001/auth/register
POST http://localhost:3001/auth/login
GET http://localhost:3002/products
POST http://localhost:3003/orders
GET http://localhost:8080/api/products
```

## ☸️ Kubernetes

```powershell
kubectl config use-context docker-desktop
kubectl get nodes
kubectl apply -f .\kubernetes\local
kubectl get pods -n microservices-local
kubectl get svc -n microservices-local
kubectl logs deployment/gateway -n microservices-local
kubectl delete namespace microservices-local
```

## 🐍 Python API Tests

```powershell
py -m pip install requests
py templates\python-api-tests\01_auth_health.py
py templates\python-api-tests\02_auth_register.py
py templates\python-api-tests\03_auth_login.py
py templates\python-api-tests\04_product_list.py
py templates\python-api-tests\05_create_order.py
py templates\python-api-tests\06_gateway_products.py
```

## 💾 Git

```powershell
git status
git add .
git commit -m "feat: add useful change"
git push
git pull
git log --oneline
```

## ☁️ AWS

```powershell
aws --version
aws sts get-caller-identity
$env:AWS_REGION="ap-south-1"
$env:AWS_ACCOUNT_ID=(aws sts get-caller-identity --query Account --output text)
```

## 🔐 ECR Login

```powershell
$env:ECR_REGISTRY="$env:AWS_ACCOUNT_ID.dkr.ecr.$env:AWS_REGION.amazonaws.com"

aws ecr get-login-password --region $env:AWS_REGION |
  docker login --username AWS --password-stdin $env:ECR_REGISTRY
```

# 🧪 Lab 03: Docker Compose Stack

## 🎯 Objective

Run backend services, PostgreSQL, Redis, and frontend using Docker Compose.

## 🧰 Tools

- Docker Desktop
- Docker Compose
- PostgreSQL container
- Redis container

## 🪜 Steps

Make sure Docker Desktop is running.

From project root, build and start:

```powershell
docker compose up --build
```

Open another PowerShell window and check containers:

```powershell
docker compose ps
```

Test services:

```powershell
Invoke-RestMethod http://localhost:3001/health
Invoke-RestMethod http://localhost:3002/health
Invoke-RestMethod http://localhost:3003/health
```

Connect to PostgreSQL:

```powershell
docker exec -it microservices-postgres psql -U app_user -d microservices_db
```

Inside `psql`:

```sql
\dt
SELECT * FROM products;
\q
```

## ✅ Expected Output

`docker compose ps` should show containers running for:

```text
postgres
redis
auth-service
product-service
order-service
frontend
```

The health endpoints should return `status: OK`.

## 🧪 Verification

Run:

```powershell
docker compose logs auth-service
docker compose logs postgres
docker compose logs redis
```

You should see normal startup logs and no crash loop.

## 🧠 What You Learned

- How Compose starts multiple services together
- Why containers use service names for networking
- How to inspect logs
- How to enter the PostgreSQL container

## 💾 Commit

```powershell
git add .
git commit -m "feat: run local stack with docker compose"
```

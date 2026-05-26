# 🧪 Lab 05: Database And Cache

## 🎯 Objective

Store data in PostgreSQL and cache product data in Redis.

## 🧰 Tools

- PostgreSQL
- Redis
- Node.js `pg`
- Node.js `ioredis`
- Docker Compose

## 🪜 Steps

Install PostgreSQL client package in backend services:

```powershell
cd services\auth-service
npm install pg

cd ..\product-service
npm install pg ioredis

cd ..\order-service
npm install pg

cd ..\..
```

Add database integration from:

[../docs/02-containers/05-database-integration.md](../docs/02-containers/05-database-integration.md)

Add Redis caching from:

[../docs/02-containers/06-redis-cache.md](../docs/02-containers/06-redis-cache.md)

Start the stack:

```powershell
docker compose up --build
```

## ✅ Expected Output

Products should come from PostgreSQL:

```powershell
Invoke-RestMethod http://localhost:3002/products
```

Orders should persist after restart:

```powershell
Invoke-RestMethod `
  -Uri http://localhost:3003/orders `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"userId":1,"productId":1,"quantity":2}'
```

Restart:

```powershell
docker compose down
docker compose up
```

List orders:

```powershell
Invoke-RestMethod http://localhost:3003/orders
```

The order should still exist.

## 🧪 Redis Verification

Call products once:

```powershell
Invoke-RestMethod http://localhost:3002/products
```

Open Redis CLI:

```powershell
docker exec -it microservices-redis redis-cli
```

Inside Redis:

```text
KEYS *
GET products:all
TTL products:all
exit
```

## 🧠 What You Learned

- Why in-memory arrays are not enough
- How service code connects to PostgreSQL
- How Redis caching works
- How data can survive container restarts

## 💾 Commit

```powershell
git add .
git commit -m "feat: persist data and cache products"
```

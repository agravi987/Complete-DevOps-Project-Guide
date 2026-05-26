# Phase 11: Add Redis Caching

Goal: use Redis for a real application behavior.

The product service will cache the product list for 60 seconds. This teaches the basic DevOps idea behind cache containers and managed cache services.

## Install Redis Client

Run from project root:

```powershell
cd services\product-service
npm install ioredis
cd ..\..
```

## Add Cache Helper

Create `services/product-service/src/cache.js`:

```javascript
const Redis = require("ioredis");

const redis = new Redis({
  host: process.env.REDIS_HOST || "localhost",
  port: Number(process.env.REDIS_PORT || 6379),
});

module.exports = redis;
```

## Update Product Service

In `services/product-service/src/app.js`, add this import:

```javascript
const redis = require("./cache");
```

Replace the `/products` route with:

```javascript
app.get("/products", async (req, res) => {
  const cacheKey = "products:all";
  const cachedProducts = await redis.get(cacheKey);

  if (cachedProducts) {
    return res.json(JSON.parse(cachedProducts));
  }

  const result = await db.query("SELECT id, name, price FROM products ORDER BY id");

  await redis.setex(cacheKey, 60, JSON.stringify(result.rows));

  return res.json(result.rows);
});
```

What this does:

1. Check Redis first.
2. If products are cached, return them immediately.
3. If Redis does not have the data, read PostgreSQL.
4. Save the result in Redis for 60 seconds.

## Rebuild And Test

Run from project root:

```powershell
docker compose up --build
```

Call products:

```powershell
Invoke-RestMethod http://localhost:3002/products
```

Check Redis key:

```powershell
docker exec -it microservices-redis redis-cli
```

Inside Redis CLI:

```text
KEYS *
GET products:all
TTL products:all
exit
```

## Cache Invalidation Note

This beginner project only reads products. In real applications, when a product is created or updated, you must delete or refresh the cache.

Example:

```javascript
await redis.del("products:all");
```

## Commit

```powershell
git add .
git commit -m "feat: cache products with redis"
```

## Checkpoint

You are ready when:

- Product service starts with Redis.
- `/products` still returns products.
- Redis contains the `products:all` key after the first request.

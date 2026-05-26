# 🐘 Phase 10: Connect Services To PostgreSQL

Goal: replace in-memory data with PostgreSQL so data survives service restarts.

This phase uses the PostgreSQL container from the Docker Compose phase.

## 📦 Install pg In Each Backend Service

Run from project root:

```powershell
cd services\auth-service
npm install pg

cd ..\product-service
npm install pg

cd ..\order-service
npm install pg

cd ..\..
```

## 🔐 Add Database Helper To Auth Service

Create `services/auth-service/src/db.js`:

```powershell
New-Item -ItemType File -Path .\services\auth-service\src\db.js
```

```javascript
const { Pool } = require("pg");

const pool = new Pool({
  host: process.env.POSTGRES_HOST || "localhost",
  port: Number(process.env.POSTGRES_PORT || 5432),
  database: process.env.POSTGRES_DB || "microservices_db",
  user: process.env.POSTGRES_USER || "app_user",
  password: process.env.POSTGRES_PASSWORD || "change_me_for_local_only",
});

function query(text, params) {
  return pool.query(text, params);
}

module.exports = {
  query,
};
```

Replace `services/auth-service/src/controllers/auth.controller.js`:

```javascript
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const db = require("../db");

async function register(req, res) {
  const { name, email, password } = req.body;

  if (!name || !email || !password) {
    return res.status(400).json({ message: "name, email, and password are required" });
  }

  const existingUser = await db.query("SELECT id FROM users WHERE email = $1", [email]);

  if (existingUser.rows.length > 0) {
    return res.status(409).json({ message: "user already exists" });
  }

  const passwordHash = await bcrypt.hash(password, 10);

  const result = await db.query(
    "INSERT INTO users (name, email, password_hash) VALUES ($1, $2, $3) RETURNING id, name, email",
    [name, email, passwordHash]
  );

  return res.status(201).json(result.rows[0]);
}

async function login(req, res) {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ message: "email and password are required" });
  }

  const result = await db.query(
    "SELECT id, name, email, password_hash FROM users WHERE email = $1",
    [email]
  );

  if (result.rows.length === 0) {
    return res.status(401).json({ message: "invalid credentials" });
  }

  const user = result.rows[0];
  const passwordMatches = await bcrypt.compare(password, user.password_hash);

  if (!passwordMatches) {
    return res.status(401).json({ message: "invalid credentials" });
  }

  const token = jwt.sign(
    { sub: user.id, email: user.email },
    process.env.JWT_SECRET,
    { expiresIn: "1h" }
  );

  return res.json({ token });
}

module.exports = {
  register,
  login,
};
```

## 📦 Add Database Helper To Product Service

Create `services/product-service/src/db.js`:

```powershell
New-Item -ItemType File -Path .\services\product-service\src\db.js
```

```javascript
const { Pool } = require("pg");

const pool = new Pool({
  host: process.env.POSTGRES_HOST || "localhost",
  port: Number(process.env.POSTGRES_PORT || 5432),
  database: process.env.POSTGRES_DB || "microservices_db",
  user: process.env.POSTGRES_USER || "app_user",
  password: process.env.POSTGRES_PASSWORD || "change_me_for_local_only",
});

function query(text, params) {
  return pool.query(text, params);
}

module.exports = {
  query,
};
```

Replace `services/product-service/src/app.js`:

```javascript
require("dotenv").config();

const express = require("express");
const db = require("./db");

const app = express();

app.use(express.json());

app.get("/", (req, res) => {
  res.json({ message: "Product Service Running" });
});

app.get("/health", (req, res) => {
  res.status(200).json({
    service: process.env.SERVICE_NAME || "product-service",
    status: "OK",
  });
});

app.get("/products", async (req, res) => {
  const result = await db.query("SELECT id, name, price FROM products ORDER BY id");
  res.json(result.rows);
});

app.get("/products/:id", async (req, res) => {
  const result = await db.query(
    "SELECT id, name, price FROM products WHERE id = $1",
    [req.params.id]
  );

  if (result.rows.length === 0) {
    return res.status(404).json({ message: "product not found" });
  }

  return res.json(result.rows[0]);
});

const port = Number(process.env.PORT || 3002);

app.listen(port, "0.0.0.0", () => {
  console.log(`Product service running on port ${port}`);
});
```

## 🧾 Add Database Helper To Order Service

Create `services/order-service/src/db.js`:

```powershell
New-Item -ItemType File -Path .\services\order-service\src\db.js
```

```javascript
const { Pool } = require("pg");

const pool = new Pool({
  host: process.env.POSTGRES_HOST || "localhost",
  port: Number(process.env.POSTGRES_PORT || 5432),
  database: process.env.POSTGRES_DB || "microservices_db",
  user: process.env.POSTGRES_USER || "app_user",
  password: process.env.POSTGRES_PASSWORD || "change_me_for_local_only",
});

function query(text, params) {
  return pool.query(text, params);
}

module.exports = {
  query,
};
```

Replace `services/order-service/src/app.js`:

```javascript
require("dotenv").config();

const express = require("express");
const db = require("./db");

const app = express();

app.use(express.json());

app.get("/", (req, res) => {
  res.json({ message: "Order Service Running" });
});

app.get("/health", (req, res) => {
  res.status(200).json({
    service: process.env.SERVICE_NAME || "order-service",
    status: "OK",
  });
});

app.get("/orders", async (req, res) => {
  const result = await db.query(
    "SELECT id, user_id, product_id, quantity, status, created_at FROM orders ORDER BY id"
  );

  res.json(result.rows);
});

app.post("/orders", async (req, res) => {
  const { userId, productId, quantity } = req.body;

  if (!userId || !productId || !quantity) {
    return res.status(400).json({
      message: "userId, productId, and quantity are required",
    });
  }

  const result = await db.query(
    "INSERT INTO orders (user_id, product_id, quantity) VALUES ($1, $2, $3) RETURNING id, user_id, product_id, quantity, status, created_at",
    [userId, productId, quantity]
  );

  return res.status(201).json(result.rows[0]);
});

const port = Number(process.env.PORT || 3003);

app.listen(port, "0.0.0.0", () => {
  console.log(`Order service running on port ${port}`);
});
```

## 🧪 Rebuild And Test

Run from project root:

```powershell
docker compose down
docker compose up --build
```

Test through direct service ports:

```powershell
Invoke-RestMethod http://localhost:3002/products
```

Register:

```powershell
Invoke-RestMethod `
  -Uri http://localhost:3001/auth/register `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"name":"Ravi","email":"ravi@example.com","password":"password123"}'
```

Create order:

```powershell
Invoke-RestMethod `
  -Uri http://localhost:3003/orders `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"userId":1,"productId":1,"quantity":2}'
```

Restart containers:

```powershell
docker compose down
docker compose up
```

List orders again:

```powershell
Invoke-RestMethod http://localhost:3003/orders
```

The order should still exist because it is stored in PostgreSQL.

## 💾 Commit

```powershell
git add .
git commit -m "feat: persist service data in postgres"
```

## ✅ Checkpoint

You are ready when:

- Products come from PostgreSQL.
- Users are stored in PostgreSQL.
- Orders remain after containers restart.

## Next Phase

[Phase 11: Add Redis Caching](06-redis-cache.md)

# 📦 Phase 4: Product And Order Services

Goal: add two more services so the project starts to feel like a real microservice system.

You will create:

- Product service on port `3002`
- Order service on port `3003`

For now both services use in-memory data. PostgreSQL is added later.

## 📦 Product Service

Run from project root:

```powershell
cd services\product-service
npm init -y
npm install express dotenv
npm install --save-dev nodemon
mkdir src
New-Item src\app.js
New-Item .env
```

Add `services/product-service/.env`:

```env
PORT=3002
SERVICE_NAME=product-service
```

Add `services/product-service/src/app.js`:

```javascript
require("dotenv").config();

const express = require("express");

const app = express();

app.use(express.json());

const products = [
  { id: 1, name: "Laptop", price: 75000 },
  { id: 2, name: "Keyboard", price: 2500 },
  { id: 3, name: "Mouse", price: 1200 },
];

app.get("/", (req, res) => {
  res.json({ message: "Product Service Running" });
});

app.get("/health", (req, res) => {
  res.status(200).json({
    service: process.env.SERVICE_NAME || "product-service",
    status: "OK",
  });
});

app.get("/products", (req, res) => {
  res.json(products);
});

app.get("/products/:id", (req, res) => {
  const product = products.find((item) => item.id === Number(req.params.id));

  if (!product) {
    return res.status(404).json({ message: "product not found" });
  }

  return res.json(product);
});

const port = Number(process.env.PORT || 3002);

app.listen(port, "0.0.0.0", () => {
  console.log(`Product service running on port ${port}`);
});
```

Update `services/product-service/package.json`:

```json
"scripts": {
  "start": "node src/app.js",
  "dev": "nodemon src/app.js"
}
```

Test:

```powershell
npm run dev
```

Open:

```text
http://localhost:3002/health
http://localhost:3002/products
```

### 📬 Test Product APIs In Postman

Test health first:

| Field | Value |
| --- | --- |
| Method | `GET` |
| URL | `http://localhost:3002/health` |
| Body | None |

Expected:

```json
{
  "service": "product-service",
  "status": "OK"
}
```

Then test product list:

| Field | Value |
| --- | --- |
| Method | `GET` |
| URL | `http://localhost:3002/products` |
| Body | None |

Expected:

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 75000
  }
]
```

Your response will include more products. That is correct.

Stop with `Ctrl+C`.

Optional Python test:

```powershell
py templates\python-api-tests\04_product_list.py
```

## 🧾 Order Service

Run from project root:

```powershell
cd services\order-service
npm init -y
npm install express dotenv
npm install --save-dev nodemon
mkdir src
New-Item src\app.js
New-Item .env
```

Add `services/order-service/.env`:

```env
PORT=3003
SERVICE_NAME=order-service
```

Add `services/order-service/src/app.js`:

```javascript
require("dotenv").config();

const express = require("express");

const app = express();

app.use(express.json());

const orders = [];

app.get("/", (req, res) => {
  res.json({ message: "Order Service Running" });
});

app.get("/health", (req, res) => {
  res.status(200).json({
    service: process.env.SERVICE_NAME || "order-service",
    status: "OK",
  });
});

app.get("/orders", (req, res) => {
  res.json(orders);
});

app.post("/orders", (req, res) => {
  const { userId, productId, quantity } = req.body;

  if (!userId || !productId || !quantity) {
    return res.status(400).json({
      message: "userId, productId, and quantity are required",
    });
  }

  const order = {
    id: orders.length + 1,
    userId,
    productId,
    quantity,
    status: "CREATED",
    createdAt: new Date().toISOString(),
  };

  orders.push(order);

  return res.status(201).json(order);
});

const port = Number(process.env.PORT || 3003);

app.listen(port, "0.0.0.0", () => {
  console.log(`Order service running on port ${port}`);
});
```

Update `services/order-service/package.json`:

```json
"scripts": {
  "start": "node src/app.js",
  "dev": "nodemon src/app.js"
}
```

Test:

```powershell
npm run dev
```

Create an order:

```powershell
Invoke-RestMethod `
  -Uri http://localhost:3003/orders `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"userId":1,"productId":1,"quantity":2}'
```

List orders:

```powershell
Invoke-RestMethod http://localhost:3003/orders
```

### 📬 Test Order APIs In Postman

Test health first:

| Field | Value |
| --- | --- |
| Method | `GET` |
| URL | `http://localhost:3003/health` |
| Body | None |

Expected:

```json
{
  "service": "order-service",
  "status": "OK"
}
```

Create order:

| Field | Value |
| --- | --- |
| Method | `POST` |
| URL | `http://localhost:3003/orders` |
| Body type | `raw` -> `JSON` |

Body:

```json
{
  "userId": 1,
  "productId": 1,
  "quantity": 2
}
```

Expected status:

```text
201 Created
```

List orders:

| Field | Value |
| --- | --- |
| Method | `GET` |
| URL | `http://localhost:3003/orders` |
| Body | None |

Expected:

```json
[
  {
    "id": 1,
    "userId": 1,
    "productId": 1,
    "quantity": 2,
    "status": "CREATED"
  }
]
```

Stop with `Ctrl+C`.

Optional Python test:

```powershell
py templates\python-api-tests\05_create_order.py
```

## ▶️ Run All Three Services

Open three PowerShell windows.

Terminal 1:

```powershell
cd C:\dev\microservices-project\services\auth-service
npm run dev
```

Terminal 2:

```powershell
cd C:\dev\microservices-project\services\product-service
npm run dev
```

Terminal 3:

```powershell
cd C:\dev\microservices-project\services\order-service
npm run dev
```

Test:

```text
http://localhost:3001/health
http://localhost:3002/health
http://localhost:3003/health
```

## 💾 Commit

Run from project root:

```powershell
git add .
git commit -m "feat: add product and order services"
```

## ✅ Checkpoint

You are ready when all three services start and each `/health` endpoint returns `OK`.

## Next Phase

[Phase 5: Frontend](05-frontend.md)

# 🧪 Phase 12: Postman API Testing

Goal: learn how to test APIs one request at a time in Postman.

This phase is not about running every test at once. That can feel overwhelming when you are starting.

The beginner flow is:

```text
Create one API
  -> Start the service
  -> Open Postman
  -> Send one request
  -> Check status code and response
  -> Fix errors
  -> Then move to the next API
```

## 🧠 Why Test While Building APIs?

When you build APIs, test immediately.

Example:

1. You create `/health`.
2. Test `/health`.
3. You create `/auth/register`.
4. Test `/auth/register`.
5. You create `/auth/login`.
6. Test `/auth/login`.

This is easier than building ten things and then trying to debug everything at once.

## 🧰 What You Need

- Postman installed
- Auth service running for auth tests
- Product service running for product tests
- Order service running for order tests
- Docker Compose running for gateway tests

## 🪜 Step 1: Test Auth Health

Start auth service:

```powershell
cd services\auth-service
npm run dev
```

In Postman:

| Field | Value |
| --- | --- |
| Method | `GET` |
| URL | `http://localhost:3001/health` |
| Body | None |

Expected:

```json
{
  "service": "auth-service",
  "status": "OK"
}
```

If this fails, do not test register yet. First fix service startup.

## 🪜 Step 2: Test Register

In Postman:

| Field | Value |
| --- | --- |
| Method | `POST` |
| URL | `http://localhost:3001/auth/register` |
| Body type | `raw` -> `JSON` |

Body:

```json
{
  "name": "Ravi",
  "email": "ravi@example.com",
  "password": "password123"
}
```

Expected:

```text
201 Created
```

If you get `409 Conflict`, the user already exists. Continue with login or change the email.

## 🪜 Step 3: Test Login

In Postman:

| Field | Value |
| --- | --- |
| Method | `POST` |
| URL | `http://localhost:3001/auth/login` |
| Body type | `raw` -> `JSON` |

Body:

```json
{
  "email": "ravi@example.com",
  "password": "password123"
}
```

Expected:

```json
{
  "token": "long.jwt.token"
}
```

## 🪜 Step 4: Test Product APIs

Open a new PowerShell window from project root.

Start product service:

```powershell
cd services\product-service
npm run dev
```

Test product health:

| Field | Value |
| --- | --- |
| Method | `GET` |
| URL | `http://localhost:3002/health` |

Test product list:

| Field | Value |
| --- | --- |
| Method | `GET` |
| URL | `http://localhost:3002/products` |

Expected:

```text
200 OK
```

The response should be an array of products.

## 🪜 Step 5: Test Order APIs

Open a new PowerShell window from project root.

Start order service:

```powershell
cd services\order-service
npm run dev
```

Test order health:

| Field | Value |
| --- | --- |
| Method | `GET` |
| URL | `http://localhost:3003/health` |

Create an order:

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

List orders:

| Field | Value |
| --- | --- |
| Method | `GET` |
| URL | `http://localhost:3003/orders` |

Expected:

```text
200 OK
```

The response should be an array of orders.

## 🪜 Step 6: Test Through Gateway

Start the full Docker Compose stack:

```powershell
docker compose up --build
```

Now test through Nginx:

| API | Method | URL |
| --- | --- | --- |
| Auth health | `GET` | `http://localhost:8080/api/auth/health` |
| Products | `GET` | `http://localhost:8080/api/products` |
| Orders | `GET` | `http://localhost:8080/api/orders` |

Only after these work, test POST requests through the gateway.

## 🧭 Beginner Debugging Rule

If a request fails, check in this order:

1. Is the service running?
2. Is the port correct?
3. Is the method correct?
4. Is the URL correct?
5. Did you select `raw` and `JSON` for POST body?
6. What does the service log say?

## 💾 Commit

After adding or updating Postman files:

```powershell
git add .
git commit -m "test: add postman api testing guide"
```

## ✅ Checkpoint

You are ready when you can manually test:

- Auth health
- Register
- Login
- Product list
- Create order
- Gateway products

# 🧪 Lab 06: Postman API Testing

## 🎯 Objective

Test APIs in Postman one request at a time.

This lab is intentionally slow and simple. Do not run the whole collection first.

## 🧰 Tools

- Postman
- PowerShell
- Local services or Docker Compose

## 🪜 Part 1: Test Auth Service

Start auth service:

```powershell
cd services\auth-service
npm run dev
```

### Test 1: Health

In Postman:

| Field | Value |
| --- | --- |
| Method | `GET` |
| URL | `http://localhost:3001/health` |

Expected:

```text
200 OK
```

Response should show:

```json
{
  "service": "auth-service",
  "status": "OK"
}
```

### Test 2: Register

In Postman:

| Field | Value |
| --- | --- |
| Method | `POST` |
| URL | `http://localhost:3001/auth/register` |
| Body | `raw` -> `JSON` |

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

If you get `409 Conflict`, it means the user already exists. That is okay.

### Test 3: Login

In Postman:

| Field | Value |
| --- | --- |
| Method | `POST` |
| URL | `http://localhost:3001/auth/login` |
| Body | `raw` -> `JSON` |

Body:

```json
{
  "email": "ravi@example.com",
  "password": "password123"
}
```

Expected:

```text
200 OK
```

You should see a `token` in the response.

## 🪜 Part 2: Test Product Service

Open a new PowerShell window from project root.

Start product service:

```powershell
cd services\product-service
npm run dev
```

Test product list:

| Field | Value |
| --- | --- |
| Method | `GET` |
| URL | `http://localhost:3002/products` |

Expected:

```text
200 OK
```

Response should be an array of products.

## 🪜 Part 3: Test Order Service

Open a new PowerShell window from project root.

Start order service:

```powershell
cd services\order-service
npm run dev
```

Create order:

| Field | Value |
| --- | --- |
| Method | `POST` |
| URL | `http://localhost:3003/orders` |
| Body | `raw` -> `JSON` |

Body:

```json
{
  "userId": 1,
  "productId": 1,
  "quantity": 2
}
```

Expected:

```text
201 Created
```

Then list orders:

| Field | Value |
| --- | --- |
| Method | `GET` |
| URL | `http://localhost:3003/orders` |

Expected:

```text
200 OK
```

## 🪜 Part 4: Test Gateway

Start full Docker Compose stack:

```powershell
docker compose up --build
```

Test products through gateway:

| Field | Value |
| --- | --- |
| Method | `GET` |
| URL | `http://localhost:8080/api/products` |

Expected:

```text
200 OK
```

## 📦 Optional: Import Ready Collection Later

After you test manually, you can import:

```text
postman/microservices-devops-api-tests.postman_collection.json
postman/microservices-local.postman_environment.json
```

Then run one request at a time.

Only run full folders after you understand what each request does.

## 🧠 What You Learned

- How to test one API at a time
- How to set method, URL, and JSON body in Postman
- How to read status codes
- Why testing immediately after creating an API is easier

## 💾 Commit

```powershell
git add .
git commit -m "test: add beginner postman api testing"
```

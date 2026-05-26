# 📬 API Endpoints

Use this page when you want to quickly check which API route to test.

Beginner rule:

Test only the API you just created. Do not try to test the whole project at once.

## 💻 Direct Local Service URLs

These work when services are exposed directly from Docker Compose or local Node.js.

| Service | Method | URL | Purpose |
| --- | --- | --- | --- |
| Auth | `GET` | `http://localhost:3001/health` | Auth health check |
| Auth | `POST` | `http://localhost:3001/auth/register` | Register user |
| Auth | `POST` | `http://localhost:3001/auth/login` | Login user |
| Product | `GET` | `http://localhost:3002/health` | Product health check |
| Product | `GET` | `http://localhost:3002/products` | List products |
| Product | `GET` | `http://localhost:3002/products/1` | Get one product |
| Order | `GET` | `http://localhost:3003/health` | Order health check |
| Order | `POST` | `http://localhost:3003/orders` | Create order |
| Order | `GET` | `http://localhost:3003/orders` | List orders |

## 🌐 Gateway URLs

These work through Nginx.

| Service | Method | URL | Purpose |
| --- | --- | --- | --- |
| Frontend | `GET` | `http://localhost:8080` | React app |
| Auth | `GET` | `http://localhost:8080/api/auth/health` | Auth health through gateway |
| Auth | `POST` | `http://localhost:8080/api/auth/register` | Register through gateway |
| Auth | `POST` | `http://localhost:8080/api/auth/login` | Login through gateway |
| Product | `GET` | `http://localhost:8080/api/products` | List products through gateway |
| Order | `POST` | `http://localhost:8080/api/orders` | Create order through gateway |
| Order | `GET` | `http://localhost:8080/api/orders` | List orders through gateway |

## 🧪 Example Request Bodies

Register:

```json
{
  "name": "Ravi",
  "email": "ravi@example.com",
  "password": "password123"
}
```

Login:

```json
{
  "email": "ravi@example.com",
  "password": "password123"
}
```

Create order:

```json
{
  "userId": 1,
  "productId": 1,
  "quantity": 2
}
```

## 📬 Postman Files

Use these instead of creating requests manually:

```text
postman/microservices-devops-api-tests.postman_collection.json
postman/microservices-local.postman_environment.json
```

# 🧪 Lab 04: Nginx Gateway

## 🎯 Objective

Route frontend and API traffic through one gateway.

## 🧰 Tools

- Nginx
- Docker Compose
- Browser
- PowerShell

## 🪜 Steps

Add `gateway/Dockerfile` and `gateway/nginx.conf` from:

[../docs/02-containers/03-nginx-gateway.md](../docs/02-containers/03-nginx-gateway.md)

Start everything:

```powershell
docker compose up --build
```

Open:

```text
http://localhost:8080
```

Test gateway routes:

```powershell
Invoke-RestMethod http://localhost:8080/api/auth/health
Invoke-RestMethod http://localhost:8080/api/products
Invoke-RestMethod http://localhost:8080/api/orders
```

## ✅ Expected Output

Gateway health route:

```json
{
  "service": "auth-service",
  "status": "OK"
}
```

Products route should return product JSON.

Orders route should return an array.

## 🧪 Verification

Check gateway logs:

```powershell
docker compose logs microservices-gateway
```

If you see `502 Bad Gateway`, check:

```powershell
docker compose ps
docker compose logs product-service
```

## 🧠 What You Learned

- Why an API gateway is useful
- How Nginx forwards requests
- Why frontend should call one API base URL
- How to debug gateway routing problems

## 💾 Commit

```powershell
git add .
git commit -m "feat: route traffic through nginx gateway"
```

# 🧪 Lab 02: Build First Microservice

## 🎯 Objective

Build and test the auth service locally.

## 🧰 Tools

- Node.js
- Express
- PowerShell
- Browser or API client

## 🪜 Steps

Create folders from project root:

```powershell
mkdir services
mkdir services\auth-service
cd services\auth-service
```

Initialize Node.js:

```powershell
npm init -y
npm install express dotenv jsonwebtoken bcryptjs
npm install --save-dev nodemon
```

Create files:

```powershell
mkdir src
mkdir src\routes
mkdir src\controllers
New-Item src\app.js
New-Item src\routes\auth.routes.js
New-Item src\controllers\auth.controller.js
New-Item .env
```

Follow the complete code in:

[../docs/01-local-development/03-auth-service.md](../docs/01-local-development/03-auth-service.md)

Run the service:

```powershell
npm run dev
```

## ✅ Expected Output

```text
Auth service running on port 3001
```

## 🧪 Verification

Open:

```text
http://localhost:3001/health
```

Expected response:

```json
{
  "service": "auth-service",
  "status": "OK"
}
```

Register a user:

```powershell
Invoke-RestMethod `
  -Uri http://localhost:3001/auth/register `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"name":"Ravi","email":"ravi@example.com","password":"password123"}'
```

Login:

```powershell
Invoke-RestMethod `
  -Uri http://localhost:3001/auth/login `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"email":"ravi@example.com","password":"password123"}'
```

You should receive a token.

## 🧠 What You Learned

- How to create an Express service
- Why health endpoints matter
- How API testing works from PowerShell
- Why environment variables are useful

## 💾 Commit

Run from project root:

```powershell
git add .
git commit -m "feat: add auth service"
```

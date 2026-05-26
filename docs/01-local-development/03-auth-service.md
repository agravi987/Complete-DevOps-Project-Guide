# 🔐 Phase 3: Auth Service

Goal: create the first microservice and run it directly on Windows without Docker.

The auth service starts simple:

- `GET /` returns a welcome message.
- `GET /health` returns service health.
- `POST /register` creates a demo user in memory.
- `POST /login` returns a demo token.

Database and Redis are added in a later phase.

## 📍 Enter The Service Folder

Run from project root:

```powershell
cd services\auth-service
```

## 🟢 Initialize Node.js

```powershell
npm init -y
npm install express dotenv jsonwebtoken bcryptjs
npm install --save-dev nodemon
```

## 🗂️ Create Folders And Files

```powershell
mkdir src
mkdir src\routes
mkdir src\controllers
New-Item src\app.js
New-Item src\routes\auth.routes.js
New-Item src\controllers\auth.controller.js
New-Item .env
```

## 🔐 Add Environment Variables

In `services/auth-service/.env`:

```env
PORT=3001
SERVICE_NAME=auth-service
JWT_SECRET=local_auth_secret_change_later
```

## 🧠 Add Auth Controller

In `services/auth-service/src/controllers/auth.controller.js`:

```javascript
const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");

const users = [];

async function register(req, res) {
  const { name, email, password } = req.body;

  if (!name || !email || !password) {
    return res.status(400).json({ message: "name, email, and password are required" });
  }

  const existingUser = users.find((user) => user.email === email);

  if (existingUser) {
    return res.status(409).json({ message: "user already exists" });
  }

  const passwordHash = await bcrypt.hash(password, 10);

  const user = {
    id: users.length + 1,
    name,
    email,
    passwordHash,
  };

  users.push(user);

  return res.status(201).json({
    id: user.id,
    name: user.name,
    email: user.email,
  });
}

async function login(req, res) {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ message: "email and password are required" });
  }

  const user = users.find((item) => item.email === email);

  if (!user) {
    return res.status(401).json({ message: "invalid credentials" });
  }

  const passwordMatches = await bcrypt.compare(password, user.passwordHash);

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

## 🛣️ Add Routes

In `services/auth-service/src/routes/auth.routes.js`:

```javascript
const express = require("express");
const { login, register } = require("../controllers/auth.controller");

const router = express.Router();

router.post("/register", register);
router.post("/login", login);

module.exports = router;
```

## 🚀 Add Express App

In `services/auth-service/src/app.js`:

```javascript
require("dotenv").config();

const express = require("express");
const authRoutes = require("./routes/auth.routes");

const app = express();

app.use(express.json());

app.get("/", (req, res) => {
  res.json({ message: "Auth Service Running" });
});

app.get("/health", (req, res) => {
  res.status(200).json({
    service: process.env.SERVICE_NAME || "auth-service",
    status: "OK",
  });
});

app.use("/auth", authRoutes);

const port = Number(process.env.PORT || 3001);

app.listen(port, "0.0.0.0", () => {
  console.log(`Auth service running on port ${port}`);
});
```

Why `0.0.0.0`?

When this service later runs inside Docker, binding to `0.0.0.0` allows traffic from outside the container. Binding only to `localhost` can make a container look broken.

## 📦 Update package.json Scripts

In `services/auth-service/package.json`, replace the `scripts` section:

```json
"scripts": {
  "start": "node src/app.js",
  "dev": "nodemon src/app.js"
}
```

## ▶️ Run The Service

```powershell
npm run dev
```

Expected output:

```text
Auth service running on port 3001
```

## 🌐 Test In Browser

Open:

```text
http://localhost:3001
http://localhost:3001/health
```

## 📬 Test In Postman: Health API

Do this before testing register or login.

In Postman:

| Field | Value |
| --- | --- |
| Method | `GET` |
| URL | `http://localhost:3001/health` |
| Body | None |

Click `Send`.

Expected response:

```json
{
  "service": "auth-service",
  "status": "OK"
}
```

If this does not work, do not continue yet. First check that `npm run dev` is still running.

## 📬 Test In Postman: Register API

Create a new Postman request:

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

Expected status:

```text
201 Created
```

Expected response:

```json
{
  "id": 1,
  "name": "Ravi",
  "email": "ravi@example.com"
}
```

If you run the same request again, you may get:

```text
409 Conflict
```

That means the user already exists. That is okay.

## 📬 Test In Postman: Login API

Create another Postman request:

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

Expected status:

```text
200 OK
```

Expected response:

```json
{
  "token": "long.jwt.token"
}
```

You do not need to understand JWT deeply yet. For now, just confirm that a token is returned.

## 🧪 Optional: Test With PowerShell

Register:

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

Beginner tip:

Use Postman while learning. Use PowerShell later when you want faster terminal testing.

## 🐍 Optional: Test Auth APIs With Python

If you want to test with Python, run only one script at a time:

```powershell
py templates\python-api-tests\01_auth_health.py
py templates\python-api-tests\02_auth_register.py
py templates\python-api-tests\03_auth_login.py
```

Full Python testing guide:

[../03-api-testing/02-python-api-testing.md](../03-api-testing/02-python-api-testing.md)

## 💾 Commit

Stop the server with `Ctrl+C`, then run from project root:

```powershell
cd ..\..
git add .
git commit -m "feat: add local auth service"
```

## ✅ Checkpoint

You are ready when:

- `npm run dev` starts the auth service.
- `/health` returns `status: OK`.
- Register and login both work.

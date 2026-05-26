# 🐳 Phase 6: Dockerize Services

Goal: package each app into a Docker image.

Docker gives each service a repeatable runtime. If it works in the container locally, it is much closer to working in CI and AWS.

## 🧠 Important Concepts

| Term | Meaning |
| --- | --- |
| Image | The packaged application template |
| Container | A running instance of an image |
| Dockerfile | Instructions for building an image |
| .dockerignore | Files Docker should not copy into the image |

## 📦 Backend Service Dockerfile

Create this file in each backend service:

```text
services/auth-service/Dockerfile
services/product-service/Dockerfile
services/order-service/Dockerfile
```

Add the same content to each:

```dockerfile
FROM node:24-alpine

WORKDIR /app

COPY package*.json ./

RUN npm ci --omit=dev

COPY src ./src

ENV NODE_ENV=production

EXPOSE 3001

CMD ["npm", "start"]
```

For `product-service`, change:

```dockerfile
EXPOSE 3001
```

to:

```dockerfile
EXPOSE 3002
```

For `order-service`, use:

```dockerfile
EXPOSE 3003
```

## 🚫 Backend .dockerignore

Create this file in each backend service:

```text
services/auth-service/.dockerignore
services/product-service/.dockerignore
services/order-service/.dockerignore
```

Add:

```dockerignore
node_modules
npm-debug.log
.env
.git
.gitignore
Dockerfile
```

Why ignore `.env`?

Images should not contain local secrets. Environment variables are passed when the container runs.

## 🔐 Build Auth Service Image

Run from project root:

```powershell
docker build -t auth-service:local .\services\auth-service
```

Run it:

```powershell
docker run --rm -p 3001:3001 `
  -e PORT=3001 `
  -e SERVICE_NAME=auth-service `
  -e JWT_SECRET=local_dev_secret `
  auth-service:local
```

Test:

```powershell
Invoke-RestMethod http://localhost:3001/health
```

Stop the container with `Ctrl+C`.

## 📦 Build Product Service Image

```powershell
docker build -t product-service:local .\services\product-service
docker run --rm -p 3002:3002 `
  -e PORT=3002 `
  -e SERVICE_NAME=product-service `
  product-service:local
```

Test:

```powershell
Invoke-RestMethod http://localhost:3002/products
```

Stop with `Ctrl+C`.

## 🧾 Build Order Service Image

```powershell
docker build -t order-service:local .\services\order-service
docker run --rm -p 3003:3003 `
  -e PORT=3003 `
  -e SERVICE_NAME=order-service `
  order-service:local
```

Test:

```powershell
Invoke-RestMethod http://localhost:3003/health
```

Stop with `Ctrl+C`.

## ⚛️ Frontend Dockerfile

Create `frontend/Dockerfile`:

```dockerfile
FROM node:24-alpine

WORKDIR /app

COPY package*.json ./

RUN npm ci

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
```

Create `frontend/.dockerignore`:

```dockerignore
node_modules
dist
npm-debug.log
.env
.git
```

Build:

```powershell
docker build -t microservices-frontend:local .\frontend
```

Run:

```powershell
docker run --rm -p 5173:5173 `
  -e VITE_API_BASE_URL=http://localhost:8080/api `
  microservices-frontend:local
```

Open:

```text
http://localhost:5173
```

## 💾 Commit

Run from project root:

```powershell
git add .
git commit -m "feat: add dockerfiles for local services"
```

## ✅ Checkpoint

You are ready when every service image builds and each container starts successfully.

## Next Phase

[Phase 7: Docker Compose Stack](02-docker-compose-postgres-redis.md)

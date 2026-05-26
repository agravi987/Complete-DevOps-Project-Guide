# 🛠️ Troubleshooting

Use this when something does not work.

## 🐳 Docker Desktop Not Running

Error:

```text
Cannot connect to the Docker daemon
```

Fix:

1. Start Docker Desktop.
2. Wait for the engine to finish starting.
3. Run the command again.

## 🚧 Port Already Allocated

Error:

```text
Bind for 0.0.0.0:3001 failed: port is already allocated
```

Find what is running:

```powershell
docker ps
netstat -ano | findstr :3001
```

Stop old container:

```powershell
docker stop <container-name>
```

## 📦 npm ci Fails In Docker

Cause:

`npm ci` requires `package-lock.json`.

Fix:

```powershell
cd services\auth-service
npm install
```

Commit `package-lock.json`.

## 🐘 Service Cannot Connect To PostgreSQL

Check container status:

```powershell
docker compose ps
docker compose logs postgres
docker compose logs auth-service
```

Check environment values:

```powershell
docker exec -it auth-service env
```

Inside Docker Compose, the host should be:

```text
POSTGRES_HOST=postgres
```

Not:

```text
POSTGRES_HOST=localhost
```

## 🌐 Nginx Route Returns 502

Cause:

Nginx cannot reach the upstream service.

Check:

```powershell
docker compose ps
docker compose logs microservices-gateway
docker compose logs product-service
```

Make sure service names in `nginx.conf` match names in `docker-compose.yml`.

## ⚛️ React Shows Gateway Not Running Yet

Check:

```powershell
docker compose ps
Invoke-RestMethod http://localhost:8080/api/products
```

Make sure `VITE_API_BASE_URL` is:

```env
VITE_API_BASE_URL=http://localhost:8080/api
```

Rebuild frontend after changing Vite environment variables:

```powershell
docker compose build frontend
docker compose up -d frontend
```

## 🔐 AWS ECR Login Fails

Check:

```powershell
aws sts get-caller-identity
aws --version
```

Login again:

```powershell
aws ecr get-login-password --region $env:AWS_REGION |
  docker login --username AWS --password-stdin $env:ECR_REGISTRY
```

## 🚀 ECS Task Stops Immediately

Check CloudWatch logs first.

Common causes:

- Wrong container port
- Missing environment variable
- Wrong image URI
- App crashes on startup
- Task cannot read Secrets Manager value
- Security group blocks database connection

## 🧠 Best Debugging Habit

Read the first real error. The first error usually tells you the cause. Later errors often only describe side effects.

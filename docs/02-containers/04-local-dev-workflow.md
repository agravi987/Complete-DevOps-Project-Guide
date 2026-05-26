# 🛠️ Phase 9: Local Development Workflow

Goal: learn the normal commands you will use every day.

## ▶️ Start The Full Stack

```powershell
docker compose up --build
```

## 🌙 Start In Background

```powershell
docker compose up --build -d
```

Use background mode when you want your terminal free.

## 👀 View Running Containers

```powershell
docker compose ps
```

## 📜 Follow Logs

All services:

```powershell
docker compose logs -f
```

One service:

```powershell
docker compose logs -f auth-service
```

## 🔁 Rebuild One Service

```powershell
docker compose build auth-service
docker compose up -d auth-service
```

## 🐚 Open A Shell Inside A Container

```powershell
docker exec -it auth-service sh
```

Exit:

```powershell
exit
```

## 🐘 Connect To PostgreSQL

```powershell
docker exec -it microservices-postgres psql -U app_user -d microservices_db
```

Useful commands inside `psql`:

```sql
\dt
SELECT * FROM users;
SELECT * FROM products;
SELECT * FROM orders;
\q
```

## 🛑 Stop Containers

Keep database volume:

```powershell
docker compose down
```

Delete database volume:

```powershell
docker compose down -v
```

## ♻️ Reset Everything Local

Use this when your local database is messy and you want a clean start:

```powershell
docker compose down -v
docker compose up --build
```

## 🔎 Check Ports

If a port is already used:

```powershell
netstat -ano | findstr :8080
```

Then find the process:

```powershell
tasklist /FI "PID eq <PID>"
```

## 🧭 Beginner Debugging Order

When something fails, check in this order:

1. Is Docker Desktop running?
2. Did `docker compose ps` show the container as running?
3. What do `docker compose logs <service-name>` say?
4. Is the port already used?
5. Did you edit `.env` correctly?
6. Did you rebuild after changing Dockerfile or package files?

## 💾 Commit Habit

After each working phase:

```powershell
git status
git add .
git commit -m "short meaningful message"
```

Good messages:

```text
feat: add product service
feat: add docker compose stack
fix: correct gateway route for orders
docs: update local setup notes
```

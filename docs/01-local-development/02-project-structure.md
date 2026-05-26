# 🗂️ Phase 2: Project Structure

Goal: create a clean monorepo structure that can grow from local development to Docker and AWS.

## 🧱 Final Folder Layout

```text
microservices-project/
  frontend/
  gateway/
    nginx.conf
    Dockerfile
  services/
    auth-service/
    product-service/
    order-service/
  database/
    init/
      01-create-tables.sql
  scripts/
  docker-compose.yml
  .env.example
  .gitignore
  README.md
```

## 🪜 Create The Project

Run from your working folder, for example `C:\dev`.

```powershell
mkdir microservices-project
cd microservices-project
```

Create folders:

```powershell
mkdir frontend,gateway,services,database,scripts
mkdir services\auth-service
mkdir services\product-service
mkdir services\order-service
mkdir database\init
```

Create root files:

```powershell
New-Item docker-compose.yml
New-Item .env.example
New-Item .gitignore
New-Item README.md
```

## 🚫 Add Root .gitignore

Open `.gitignore` and add:

```gitignore
node_modules/
.env
.env.*
!.env.example
dist/
build/
coverage/
npm-debug.log*
.DS_Store
Thumbs.db
```

Why this matters:

- `node_modules` can be rebuilt with `npm install`.
- `.env` files often contain passwords.
- Build output should not be committed unless there is a special reason.

## 🔐 Add .env.example

Open `.env.example` and add:

```env
POSTGRES_DB=microservices_db
POSTGRES_USER=app_user
POSTGRES_PASSWORD=change_me_for_local_only
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

REDIS_HOST=redis
REDIS_PORT=6379

JWT_SECRET=replace_with_a_long_random_value
```

This file is safe to commit because it contains example values. Later each developer creates a real `.env` from it.

## 💻 Create Your Local .env

```powershell
Copy-Item .env.example .env
```

Do not commit `.env`.

## 💾 Initialize Git

```powershell
git init
git status
git add .
git commit -m "chore: create project structure"
```

If your repository already exists on GitHub, connect it:

```powershell
git remote add origin https://github.com/<your-username>/<your-repo>.git
```

## ✅ Checkpoint

You are ready when:

- The folder tree matches the layout above.
- `.env.example` exists.
- `.env` exists locally but is ignored by Git.
- `git status` is clean after your commit.

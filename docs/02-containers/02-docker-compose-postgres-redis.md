# Phase 7: Docker Compose With PostgreSQL And Redis

Goal: run the full local stack with one command.

Docker Compose starts multiple containers together and creates a private network so they can find each other by service name.

## Add Database Initialization SQL

Create `database/init/01-create-tables.sql`:

```sql
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(120) NOT NULL,
  email VARCHAR(160) NOT NULL UNIQUE,
  password_hash TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(160) NOT NULL UNIQUE,
  price INTEGER NOT NULL CHECK (price >= 0),
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS orders (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  product_id INTEGER NOT NULL,
  quantity INTEGER NOT NULL CHECK (quantity > 0),
  status VARCHAR(40) NOT NULL DEFAULT 'CREATED',
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

INSERT INTO products (name, price)
VALUES
  ('Laptop', 75000),
  ('Keyboard', 2500),
  ('Mouse', 1200)
ON CONFLICT DO NOTHING;
```

## Root .env

Make sure project root `.env` exists:

```env
POSTGRES_DB=microservices_db
POSTGRES_USER=app_user
POSTGRES_PASSWORD=change_me_for_local_only
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

REDIS_HOST=redis
REDIS_PORT=6379

JWT_SECRET=local_compose_secret_change_later
```

## Add docker-compose.yml

Replace project root `docker-compose.yml`:

```yaml
services:
  postgres:
    image: postgres:17-alpine
    container_name: microservices-postgres
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    ports:
      - "5432:5432"
    volumes:
      - postgres-data:/var/lib/postgresql/data
      - ./database/init:/docker-entrypoint-initdb.d:ro
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB"]
      interval: 10s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7.4-alpine
    container_name: microservices-redis
    ports:
      - "6379:6379"
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5

  auth-service:
    build: ./services/auth-service
    container_name: auth-service
    env_file:
      - .env
    environment:
      PORT: 3001
      SERVICE_NAME: auth-service
      POSTGRES_HOST: postgres
    ports:
      - "3001:3001"
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy

  product-service:
    build: ./services/product-service
    container_name: product-service
    env_file:
      - .env
    environment:
      PORT: 3002
      SERVICE_NAME: product-service
      POSTGRES_HOST: postgres
    ports:
      - "3002:3002"
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy

  order-service:
    build: ./services/order-service
    container_name: order-service
    env_file:
      - .env
    environment:
      PORT: 3003
      SERVICE_NAME: order-service
      POSTGRES_HOST: postgres
    ports:
      - "3003:3003"
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy

  frontend:
    build: ./frontend
    container_name: microservices-frontend
    environment:
      VITE_API_BASE_URL: http://localhost:8080/api
    ports:
      - "5173:5173"
    depends_on:
      - product-service

volumes:
  postgres-data:
```

## Start The Stack

Run from project root:

```powershell
docker compose up --build
```

Compose will:

1. Build local images.
2. Start PostgreSQL.
3. Start Redis.
4. Start the backend services.
5. Start the frontend.

## Test Services

Open a second PowerShell window and run:

```powershell
Invoke-RestMethod http://localhost:3001/health
Invoke-RestMethod http://localhost:3002/health
Invoke-RestMethod http://localhost:3003/health
```

Check database:

```powershell
docker exec -it microservices-postgres psql -U app_user -d microservices_db
```

Inside `psql`:

```sql
\dt
SELECT * FROM products;
\q
```

## Stop The Stack

Stop containers but keep database data:

```powershell
docker compose down
```

Stop containers and delete database volume:

```powershell
docker compose down -v
```

Only use `-v` when you are okay deleting local database data.

## Commit

```powershell
git add .
git commit -m "feat: add docker compose stack with postgres and redis"
```

## Checkpoint

You are ready when:

- `docker compose up --build` starts all containers.
- PostgreSQL and Redis health checks pass.
- All three services return health responses.
- You can query the `products` table in PostgreSQL.

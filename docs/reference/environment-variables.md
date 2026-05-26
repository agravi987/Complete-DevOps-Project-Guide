# Environment Variables

Environment variables let you change configuration without changing code.

## Root .env

Used by Docker Compose.

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

## Backend Service Variables

| Variable | Used By | Example | Notes |
| --- | --- | --- | --- |
| `PORT` | All services | `3001` | Container listens on this port |
| `SERVICE_NAME` | All services | `auth-service` | Returned by health endpoint |
| `POSTGRES_HOST` | Backend services | `postgres` | Docker Compose service name |
| `POSTGRES_PORT` | Backend services | `5432` | PostgreSQL port |
| `POSTGRES_DB` | Backend services | `microservices_db` | Database name |
| `POSTGRES_USER` | Backend services | `app_user` | Database username |
| `POSTGRES_PASSWORD` | Backend services | local password | Secret in AWS |
| `REDIS_HOST` | Backend services | `redis` | Docker Compose service name |
| `REDIS_PORT` | Backend services | `6379` | Redis port |
| `JWT_SECRET` | Auth service | long random value | Secret in AWS |

## Frontend Variables

In `frontend/.env`:

```env
VITE_API_BASE_URL=http://localhost:8080/api
```

Vite only exposes browser variables that start with `VITE_`.

## Local vs Docker Values

When running directly on Windows:

```env
POSTGRES_HOST=localhost
REDIS_HOST=localhost
```

When running inside Docker Compose:

```env
POSTGRES_HOST=postgres
REDIS_HOST=redis
```

This difference exists because `localhost` inside a container means the container itself.

## AWS Values

On AWS:

```env
POSTGRES_HOST=<rds-endpoint>
REDIS_HOST=<elasticache-endpoint>
```

Store passwords and JWT secrets in Secrets Manager, not plain environment variables in Git.

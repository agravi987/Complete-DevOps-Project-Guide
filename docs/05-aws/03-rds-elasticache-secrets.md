# 🔐 Phase 17: RDS, ElastiCache, And Secrets

Goal: replace local development dependencies with managed AWS services.

Local:

```text
Docker Compose PostgreSQL + Docker Compose Redis
```

AWS:

```text
RDS PostgreSQL + ElastiCache Redis + Secrets Manager
```

## 🧠 Why Managed Services

Managed AWS services handle much of the operational work:

- Backups
- Patching
- Monitoring
- Storage management
- Failover options
- Access control

You still need to configure them carefully.

## 🐘 RDS PostgreSQL

Create an RDS PostgreSQL database.

Recommended beginner settings:

| Setting | Value |
| --- | --- |
| Engine | PostgreSQL |
| Environment | Dev/Test |
| Public access | No |
| Database name | `microservices_db` |
| Username | `app_user` |
| Password | Store in Secrets Manager |
| Backup retention | Keep small for learning |

Security group rule:

```text
Allow inbound PostgreSQL 5432 only from ECS task security group.
```

Do not open PostgreSQL to the whole internet.

## ⚡ ElastiCache Redis

Create an ElastiCache Redis-compatible cache.

Recommended beginner settings:

| Setting | Value |
| --- | --- |
| Engine | Redis-compatible |
| Network | Same VPC as ECS |
| Public access | No |
| Security group | Allow 6379 only from ECS task security group |

## 🔐 Secrets Manager

Store sensitive values in Secrets Manager:

| Secret name | Example value |
| --- | --- |
| `microservices/dev/postgres-password` | RDS password |
| `microservices/dev/jwt-secret` | Long random JWT secret |

Generate a strong local value:

```powershell
[System.Web.Security.Membership]::GeneratePassword(48,8)
```

If that command is unavailable, use a password manager.

## 🧩 ECS Task Environment Variables

Use plain environment variables for non-secret values:

```text
POSTGRES_HOST=<rds-endpoint>
POSTGRES_PORT=5432
POSTGRES_DB=microservices_db
POSTGRES_USER=app_user
REDIS_HOST=<elasticache-endpoint>
REDIS_PORT=6379
```

Use ECS secrets for secret values:

```text
POSTGRES_PASSWORD=<Secrets Manager ARN>
JWT_SECRET=<Secrets Manager ARN>
```

## 📄 Task Definition Secrets Example

In an ECS task definition container, secrets look like this:

```json
"secrets": [
  {
    "name": "POSTGRES_PASSWORD",
    "valueFrom": "arn:aws:secretsmanager:REGION:ACCOUNT_ID:secret:microservices/dev/postgres-password"
  },
  {
    "name": "JWT_SECRET",
    "valueFrom": "arn:aws:secretsmanager:REGION:ACCOUNT_ID:secret:microservices/dev/jwt-secret"
  }
]
```

The ECS task execution role needs permission to read the secrets.

## 🗄️ Database Tables On RDS

You need to run the same SQL from:

```text
database/init/01-create-tables.sql
```

For beginner practice, the simplest options are:

- Use a temporary database client from a secure network path.
- Run a one-off ECS task that executes migrations.
- Use a migration tool later, such as Prisma, Knex, Sequelize, or Flyway.

For a real team project, use repeatable migrations instead of manually running SQL.

## 🛡️ Security Group Flow

Use this mental model:

```text
Internet
  |
  v
Application Load Balancer SG
  |
  v
ECS Task SG
  |
  +--> RDS SG on 5432
  +--> ElastiCache SG on 6379
```

Rules:

- ALB accepts public HTTP/HTTPS.
- ECS accepts traffic only from ALB.
- RDS accepts traffic only from ECS.
- Redis accepts traffic only from ECS.

## ✅ Checkpoint

You are ready when:

- ECS services use RDS endpoint instead of local `postgres`.
- ECS services use ElastiCache endpoint instead of local `redis`.
- Passwords come from Secrets Manager.
- RDS and Redis are not publicly open.

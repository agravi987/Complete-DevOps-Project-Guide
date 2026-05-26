# 🗂️ Project Folder Map

Use this as your mental map of the real hands-on project.

## 🧱 Final Project Structure

```text
microservices-project/
  frontend/
    src/
    Dockerfile
    .dockerignore
    package.json

  gateway/
    Dockerfile
    nginx.conf

  services/
    auth-service/
      src/
        controllers/
        routes/
        app.js
        db.js
      Dockerfile
      .dockerignore
      package.json

    product-service/
      src/
        app.js
        db.js
        cache.js
      Dockerfile
      .dockerignore
      package.json

    order-service/
      src/
        app.js
        db.js
      Dockerfile
      .dockerignore
      package.json

  database/
    init/
      01-create-tables.sql

  postman/
    microservices-devops-api-tests.postman_collection.json
    microservices-local.postman_environment.json

  .github/
    workflows/
      ci.yml

  docker-compose.yml
  .env
  .env.example
  .gitignore
  README.md
```

## 📁 What Each Folder Means

| Folder | Purpose |
| --- | --- |
| `frontend/` | React app shown in the browser |
| `gateway/` | Nginx reverse proxy and API entry point |
| `services/` | All backend microservices |
| `database/init/` | SQL scripts used when PostgreSQL starts |
| `postman/` | Ready Postman collection and local environment |
| `.github/workflows/` | GitHub Actions CI workflows |

## 📄 What Each Root File Means

| File | Purpose |
| --- | --- |
| `docker-compose.yml` | Starts the full local stack |
| `.env.example` | Safe example environment variables |
| `.env` | Real local values, not committed |
| `.gitignore` | Prevents unwanted files from entering Git |
| `README.md` | Project overview |

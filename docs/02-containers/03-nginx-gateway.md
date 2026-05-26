# 🌐 Phase 8: Nginx Gateway

Goal: put one entry point in front of the frontend and APIs.

Instead of opening separate ports for every service, the browser will use:

```text
http://localhost:8080
```

Nginx will route requests to the correct container.

## 🐳 Create Gateway Dockerfile

Create `gateway/Dockerfile`:

```dockerfile
FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
```

## 🛣️ Create Nginx Config

Create `gateway/nginx.conf`:

```nginx
events {}

http {
  upstream frontend {
    server frontend:5173;
  }

  upstream auth_service {
    server auth-service:3001;
  }

  upstream product_service {
    server product-service:3002;
  }

  upstream order_service {
    server order-service:3003;
  }

  server {
    listen 80;

    location = /api/auth/health {
      proxy_pass http://auth_service/health;
    }

    location = /api/products/health {
      proxy_pass http://product_service/health;
    }

    location = /api/orders/health {
      proxy_pass http://order_service/health;
    }

    location /api/auth/ {
      rewrite ^/api/auth/(.*)$ /auth/$1 break;
      proxy_pass http://auth_service;
    }

    location = /api/products {
      proxy_pass http://product_service/products;
    }

    location /api/products/ {
      rewrite ^/api/products/(.*)$ /products/$1 break;
      proxy_pass http://product_service;
    }

    location = /api/orders {
      proxy_pass http://order_service/orders;
    }

    location /api/orders/ {
      rewrite ^/api/orders/(.*)$ /orders/$1 break;
      proxy_pass http://order_service;
    }

    location / {
      proxy_pass http://frontend;
      proxy_http_version 1.1;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection "upgrade";
      proxy_set_header Host $host;
    }
  }
}
```

## 🧩 Add Gateway To docker-compose.yml

Add this service under `services`:

```yaml
  gateway:
    build: ./gateway
    container_name: microservices-gateway
    ports:
      - "8080:80"
    depends_on:
      - frontend
      - auth-service
      - product-service
      - order-service
```

## ▶️ Start Everything

Run from project root:

```powershell
docker compose up --build
```

## 🧪 Test Through Gateway

Open:

```text
http://localhost:8080
http://localhost:8080/api/auth/health
http://localhost:8080/api/products
http://localhost:8080/api/orders
```

Register through gateway:

```powershell
Invoke-RestMethod `
  -Uri http://localhost:8080/api/auth/register `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"name":"Ravi","email":"ravi@example.com","password":"password123"}'
```

Create order through gateway:

```powershell
Invoke-RestMethod `
  -Uri http://localhost:8080/api/orders `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"userId":1,"productId":1,"quantity":2}'
```

## 🧠 Why The Gateway Matters

Without a gateway:

```text
Frontend -> localhost:3001
Frontend -> localhost:3002
Frontend -> localhost:3003
```

With a gateway:

```text
Frontend -> localhost:8080/api/auth
Frontend -> localhost:8080/api/products
Frontend -> localhost:8080/api/orders
```

Later on AWS, the gateway/load balancer is what makes the system easier to expose safely.

## 💾 Commit

```powershell
git add .
git commit -m "feat: add nginx gateway routing"
```

## ✅ Checkpoint

You are ready when the frontend and all APIs work through `http://localhost:8080`.

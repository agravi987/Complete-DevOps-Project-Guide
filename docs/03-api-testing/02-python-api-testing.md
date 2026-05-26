# 🐍 Phase 12B: Python API Testing

Goal: test APIs with small Python scripts, one endpoint at a time.

Use this only if you want code-based testing. If you are a beginner, Postman is still easier for the first attempt.

## 🧠 Beginner Rule

Do not run all Python scripts together.

Run only the script for the API you just created.

```text
Create /health
  -> run 01_auth_health.py

Create /auth/register
  -> run 02_auth_register.py

Create /auth/login
  -> run 03_auth_login.py
```

## 🧰 Step 1: Install requests

Open PowerShell from your actual project root:

```powershell
py -m pip install requests
```

If `py` does not work, try:

```powershell
python -m pip install requests
```

## 🪜 Step 2: Copy The Script You Need

Templates are available here:

[../../templates/python-api-tests](../../templates/python-api-tests)

For learning, copy only the script you need into your project.

Example folder in your real project:

```text
microservices-project/
  api-tests/
    python/
      01_auth_health.py
```

## 🪜 Step 3: Test Auth Health

Start auth service:

```powershell
cd services\auth-service
npm run dev
```

Open another PowerShell window from project root:

```powershell
py templates\python-api-tests\01_auth_health.py
```

Expected:

```text
Status: 200
Auth health test passed.
```

If this fails, do not test register yet.

## 🪜 Step 4: Test Register

Run:

```powershell
py templates\python-api-tests\02_auth_register.py
```

Expected:

```text
Status: 201
Register test passed.
```

If the user already exists, status `409` is also okay for repeated testing.

## 🪜 Step 5: Test Login

Run:

```powershell
py templates\python-api-tests\03_auth_login.py
```

Expected:

```text
Status: 200
Login test passed.
```

## 🪜 Step 6: Test Products

Start product service:

```powershell
cd services\product-service
npm run dev
```

Run:

```powershell
py templates\python-api-tests\04_product_list.py
```

## 🪜 Step 7: Test Orders

Start order service:

```powershell
cd services\order-service
npm run dev
```

Run:

```powershell
py templates\python-api-tests\05_create_order.py
```

## 🪜 Step 8: Test Gateway

Start Docker Compose:

```powershell
docker compose up --build
```

Run:

```powershell
py templates\python-api-tests\06_gateway_products.py
```

## ✅ Checkpoint

You are good when you can run one Python script for the API you just built and understand the response.

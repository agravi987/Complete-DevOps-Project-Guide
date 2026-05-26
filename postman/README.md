# 📬 Postman API Tests

This folder contains ready-to-import Postman files for the microservices project.

Beginner note:

Use the manual testing steps in the guide first. Import these files later when you understand what each request does.

## 📦 Files

| File | Purpose |
| --- | --- |
| `microservices-devops-api-tests.postman_collection.json` | Collection with API requests and tests |
| `microservices-local.postman_environment.json` | Local URLs, user data, and saved variables |

## 🪜 How To Use

1. Start the local stack:

```powershell
docker compose up --build
```

2. Open Postman.
3. Import both JSON files.
4. Select environment:

```text
Microservices Local
```

5. Run one request first.
6. Later, run folders in this order:

```text
01 Direct Local Services
02 Gateway Routes
03 Negative Tests
```

## ✅ What Should Pass

- Health checks return `OK`.
- Register user returns `201` or `409`.
- Login returns a token.
- Products return an array.
- Order creation returns `201`.
- Negative tests return expected error status codes.

## 🛠️ If Tests Fail

Open:

[../docs/03-api-testing/01-postman-api-testing.md](../docs/03-api-testing/01-postman-api-testing.md)

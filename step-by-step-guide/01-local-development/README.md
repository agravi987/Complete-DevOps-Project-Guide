# Local Development

Build the application directly on Windows before using Docker or cloud tools.

Finish this section before opening the container section.

## Phases

| Phase | Open | Finish with |
| --- | --- | --- |
| 1 | [Windows Prerequisites](01-prerequisites.md) | Node.js, Git, Docker Desktop, VS Code, Postman, Python, and AWS CLI verified |
| 2 | [Project Structure](02-project-structure.md) | Clean project folders, `.gitignore`, `.env.example`, and Git initialized |
| 3 | [Auth Service](03-auth-service.md) | Auth API running locally with health, register, and login endpoints |
| 4 | [Product And Order Services](04-product-and-order-services.md) | Product and order APIs running beside auth |
| 5 | [Frontend](05-frontend.md) | React UI running locally |

## Section Checkpoint

Before moving to Docker, these URLs should work:

```text
http://localhost:3001/health
http://localhost:3002/health
http://localhost:3003/health
http://localhost:5173
```

If any URL fails, stay in this section and fix it first.

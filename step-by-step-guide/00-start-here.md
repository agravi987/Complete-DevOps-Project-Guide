# Start Here

This repo teaches DevOps by building one complete microservice project from local development to AWS.

There is one path through the repo:

```text
Local app
  -> Docker
  -> Docker Compose
  -> Nginx gateway
  -> PostgreSQL and Redis
  -> API testing
  -> local Kubernetes
  -> GitHub Actions
  -> AWS
  -> cleanup
```

Do not treat the repo like a collection of random notes. Treat it like a workbook.

## What You Need Before Starting

You should be comfortable with:

- Opening PowerShell
- Creating folders
- Editing files in VS Code
- Running commands
- Reading basic JavaScript

You do not need to know Docker, Kubernetes, CI/CD, or AWS yet. The guide introduces those pieces only after the local app works.

## Project Folder Name

The guide uses this project folder name:

```powershell
microservices-project
```

Beginners should use the same name. Changing names is possible, but it creates extra mental work when following commands.

## How To Use Every Phase

Use this exact rhythm:

1. Read the phase goal.
2. Run commands from the folder shown in the phase.
3. Create or edit only the files listed.
4. Run the verification commands.
5. Do not move forward until verification passes.
6. Commit after the phase works.

If something fails, open [reference/troubleshooting.md](reference/troubleshooting.md), fix the issue, and rerun the verification step.

## What Success Looks Like

At the end, you should be able to explain:

- What each microservice does
- Why a gateway sits in front of services
- How containers make the app portable
- How Docker Compose runs the local system
- How PostgreSQL and Redis support the services
- How to test APIs before deploying
- How Kubernetes runs the same app differently from Compose
- How GitHub Actions checks the project
- How images move from your laptop to AWS
- Why cleanup is part of cloud work

## First Action

Start here:

[01-local-development/01-prerequisites.md](01-local-development/01-prerequisites.md)

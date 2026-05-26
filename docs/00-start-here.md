# Start Here

This guide teaches DevOps through one complete project. You will start with a simple local application and slowly add the real-world pieces around it.

## Before You Begin

You should be comfortable with:

- Creating folders
- Opening PowerShell
- Running commands
- Editing files in VS Code
- Reading simple JavaScript

You do not need to already know Docker, AWS, Nginx, or CI/CD. Those are explained step by step.

## How To Follow This Guide

Use this rhythm for every phase:

1. Read the goal.
2. Run the commands.
3. Create or edit the files.
4. Test the result.
5. Commit your work.
6. Move to the next phase only when the current phase works.

## The Project Name

The guide uses this folder name:

```powershell
microservices-project
```

You can choose a different name, but beginners should keep the same name to avoid confusion.

## Local First, Cloud Later

Do not start with AWS. A good DevOps workflow is:

1. Make the app work on your laptop.
2. Containerize it.
3. Run all services together locally.
4. Add CI checks.
5. Deploy to AWS.
6. Add monitoring, security, and cleanup.

That order keeps the learning clear.

## What Success Looks Like

At the end, you should be able to explain:

- What each microservice does
- Why containers are useful
- How services talk to each other in Docker Compose
- Why an API gateway exists
- How CI catches mistakes
- How container images move from your laptop to AWS
- Why AWS managed services are used for database, cache, secrets, and logs

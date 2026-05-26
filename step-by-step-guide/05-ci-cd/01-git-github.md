# 💾 Phase 15: Git And GitHub

Goal: save your project history locally and push it to GitHub.

## 🧠 Why Git Matters In DevOps

Git is the source of truth for:

- Application code
- Dockerfiles
- Compose files
- CI/CD workflows
- Infrastructure as code later
- Documentation

In DevOps, almost everything starts from a Git commit.

## 🔎 Check Git Status Often

Run from project root:

```powershell
git status
```

Use it before and after every commit.

## ✍️ Commit Meaningfully

Good commit messages are short and specific:

```text
feat: add auth service
feat: add docker compose stack
fix: correct product gateway route
docs: add aws cleanup steps
```

Avoid vague messages:

```text
update
changes
final
new
```

## 🌐 Create A GitHub Repository

On GitHub:

1. Create a new repository.
2. Do not add a README if you already have one locally.
3. Copy the repository URL.

Example URL:

```text
https://github.com/<your-username>/microservices-project.git
```

## 🔗 Connect Local Repo To GitHub

Run from project root:

```powershell
git remote add origin https://github.com/<your-username>/microservices-project.git
git branch -M main
git push -u origin main
```

If the remote already exists:

```powershell
git remote -v
git remote set-url origin https://github.com/<your-username>/microservices-project.git
```

Then push:

```powershell
git push -u origin main
```

## 🔁 Normal Workflow

Every time you finish a small working change:

```powershell
git status
git add .
git commit -m "meaningful message"
git push
```

## 🌿 Beginner Branch Workflow

For practice:

```powershell
git checkout -b feature/add-health-checks
```

Make changes, then:

```powershell
git add .
git commit -m "feat: add service health checks"
git push -u origin feature/add-health-checks
```

Open a Pull Request on GitHub.

## 🔐 Do Not Commit Secrets

Never commit:

- `.env`
- AWS access keys
- Database passwords
- JWT secrets
- Private keys

If you accidentally commit a real secret, deleting it in a later commit is not enough. Rotate the secret immediately.

## ✅ Checkpoint

You are ready when:

- The local project is committed.
- The remote GitHub repo exists.
- `git push` works.
- `.env` is not tracked.

## Next Phase

[Phase 16: GitHub Actions CI](02-github-actions-ci.md)

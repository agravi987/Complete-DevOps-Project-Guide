# 🧪 Lab 06: CI/CD With GitHub Actions

## 🎯 Objective

Create a GitHub Actions workflow that checks Node.js apps and Docker builds.

## 🧰 Tools

- Git
- GitHub
- GitHub Actions
- Docker build

## 🪜 Steps

Create workflow folders:

```powershell
mkdir .github
mkdir .github\workflows
New-Item .github\workflows\ci.yml
```

Copy the workflow from:

[../templates/github-actions/ci.yml](../templates/github-actions/ci.yml)

Commit:

```powershell
git add .
git commit -m "ci: add github actions workflow"
git push
```

## ✅ Expected Output

On GitHub:

1. Open your repository.
2. Click `Actions`.
3. Open the latest `ci` workflow.
4. Jobs should become green.

## 🧪 Verification

The workflow should run:

```text
Node checks
Docker build
```

If it fails, open the failed job and read the first real error.

## 🧠 What You Learned

- Why CI runs on push
- How GitHub Actions checks multiple apps
- How Docker build failures are caught before deployment
- Why logs matter in automation

## 💾 Commit

Already done in the steps above.

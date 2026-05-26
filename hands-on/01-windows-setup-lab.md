# 🧪 Lab 01: Windows Setup

## 🎯 Objective

Prepare your Windows machine for local DevOps development.

## 🧰 Tools

- PowerShell
- VS Code
- Git
- Node.js
- Docker Desktop

## 🪜 Steps

Open PowerShell and run:

```powershell
node --version
npm --version
git --version
docker --version
docker compose version
```

Run Docker test:

```powershell
docker run hello-world
```

Create a clean workspace:

```powershell
mkdir C:\dev
cd C:\dev
mkdir microservices-project
cd microservices-project
code .
```

## ✅ Expected Output

You should see:

```text
Hello from Docker!
```

VS Code should open the empty project folder.

## 🧪 Verification

Run:

```powershell
Get-Location
```

Expected path:

```text
C:\dev\microservices-project
```

## 🧠 What You Learned

- How to verify installed tools
- How to confirm Docker Desktop works
- How to create a clean project workspace

## 💾 Commit

There may be nothing to commit yet. Start committing after files are created in the next lab.

# 🪟 Phase 1: Windows Prerequisites

Goal: install the tools needed to build and run the project locally on Windows.

## 🧰 Tools To Install

Install these first:

| Tool | Why You Need It |
| --- | --- |
| VS Code | Code editor |
| Git | Version control |
| Node.js 24 LTS | Runtime for React and Express services |
| Docker Desktop | Run containers locally |
| kubectl | Control local Kubernetes from PowerShell |
| Postman or Thunder Client | Test APIs from a friendly UI |
| GitHub account | Store your code and run CI later |

Recommended later:

| Tool | Why You Need It |
| --- | --- |
| AWS CLI v2 | Manage AWS from terminal |
| AWS account | Deploy the project to cloud |

## ✅ Verify Local Tools

Open PowerShell and run:

```powershell
node --version
npm --version
git --version
docker --version
docker compose version
kubectl version --client
code --version
```

Expected result:

- `node --version` should show Node.js 24.x or another current even-numbered LTS version.
- `docker compose version` should work with a space between `docker` and `compose`.
- Docker Desktop must be running before Docker commands work.
- `kubectl` is used later for Docker Desktop Kubernetes.

## 🐳 Docker Desktop On Windows

Use Docker Desktop with the WSL 2 backend when possible. It is the normal local setup for Windows developers.

Basic checks:

```powershell
wsl --version
docker run hello-world
```

If `docker run hello-world` succeeds, Docker is ready.

## 🗂️ Create A Working Folder

Use a simple path while learning. Spaces in folder names are allowed, but short paths reduce beginner mistakes.

Example:

```powershell
mkdir C:\dev
cd C:\dev
```

## 🛠️ Common Windows Issues

### Docker daemon error

Error:

```text
Cannot connect to the Docker daemon
```

Fix:

1. Open Docker Desktop.
2. Wait until it says the engine is running.
3. Run the Docker command again.

### Port already used

Error:

```text
port is already allocated
```

Check running containers:

```powershell
docker ps
```

Stop the container using that port:

```powershell
docker stop <container-name>
```

### PowerShell command not found after install

Close PowerShell and open it again. Some installers update `PATH`, and a new terminal session is needed.

## ✅ Checkpoint

Before continuing, these commands should work:

```powershell
node --version
npm --version
git --version
docker run hello-world
```

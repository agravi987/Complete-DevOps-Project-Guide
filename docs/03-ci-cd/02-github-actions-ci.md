# Phase 13: GitHub Actions CI

Goal: make GitHub automatically check your project when code is pushed.

CI means Continuous Integration. It catches problems before they reach deployment.

## What This CI Will Do

The first CI pipeline will:

1. Install Node.js.
2. Install dependencies for each service.
3. Run tests if they exist.
4. Build Docker images to catch Dockerfile errors.

## Create Workflow Folder

Run from project root:

```powershell
mkdir .github
mkdir .github\workflows
New-Item .github\workflows\ci.yml
```

## Add ci.yml

Add this to `.github/workflows/ci.yml`:

```yaml
name: ci

on:
  push:
    branches:
      - main
  pull_request:

jobs:
  node-checks:
    name: Node checks
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        app:
          - services/auth-service
          - services/product-service
          - services/order-service
          - frontend

    defaults:
      run:
        working-directory: ${{ matrix.app }}

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 24
          cache: npm
          cache-dependency-path: ${{ matrix.app }}/package-lock.json

      - name: Install dependencies
        run: npm ci

      - name: Run tests if present
        run: npm test --if-present

  docker-build:
    name: Docker build
    runs-on: ubuntu-latest
    needs: node-checks
    strategy:
      fail-fast: false
      matrix:
        image:
          - name: auth-service
            context: services/auth-service
          - name: product-service
            context: services/product-service
          - name: order-service
            context: services/order-service
          - name: frontend
            context: frontend
          - name: gateway
            context: gateway

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Build image
        run: docker build -t ${{ matrix.image.name }}:ci ./${{ matrix.image.context }}
```

## Commit And Push

```powershell
git add .github\workflows\ci.yml
git commit -m "ci: add node and docker build workflow"
git push
```

## View The Workflow

On GitHub:

1. Open your repository.
2. Click `Actions`.
3. Open the latest `ci` run.
4. Check each job.

## If CI Fails

Do not panic. CI failures are useful.

Common causes:

| Problem | Fix |
| --- | --- |
| `package-lock.json` missing | Run `npm install` locally and commit the lock file |
| Docker build fails | Check Dockerfile path and `COPY` commands |
| Tests fail | Run the same command locally |
| Wrong Node version | Match local and CI Node versions |

## Add Real Tests Later

Right now `npm test --if-present` allows the workflow to pass even before tests exist.

Later you can add:

- Unit tests for controllers
- API tests for routes
- Docker Compose integration tests
- Security scanning
- Image push to Amazon ECR

## Checkpoint

You are ready when:

- GitHub Actions starts after push.
- Node checks pass.
- Docker image builds pass.

# DevOps Project Workbook

This folder is the workbook. Start at phase 0 and move forward one phase at a time.

You do not need to choose between multiple routes. Each phase is written as a build guide with explanation, commands, verification, and commit steps.

## Workbook Sections

| Section | Open | Purpose |
| --- | --- | --- |
| 0 | [Start Here](00-start-here.md) | Learn the rules for following the repo |
| 1 | [Local Development](01-local-development/README.md) | Build the app directly on Windows |
| 2 | [Containers And Local Infrastructure](02-containers/README.md) | Add Docker, Compose, PostgreSQL, Redis, and Nginx |
| 3 | [API Testing](03-api-testing/README.md) | Test APIs manually and with small scripts |
| 4 | [Local Kubernetes](04-kubernetes/README.md) | Deploy the same app to Docker Desktop Kubernetes |
| 5 | [CI/CD](05-ci-cd/README.md) | Push to GitHub and add GitHub Actions |
| 6 | [AWS](06-aws/README.md) | Push images, run ECS Fargate, and clean up |
| Reference | [Reference Library](reference/README.md) | Look up commands, endpoints, terms, and fixes |

## The Rule

Open one phase. Finish it. Verify it. Commit it. Then move to the next phase.

That rhythm keeps the project understandable and prevents half-working infrastructure from piling up.

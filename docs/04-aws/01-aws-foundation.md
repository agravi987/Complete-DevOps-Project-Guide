# ☁️ Phase 14: AWS Foundation

Goal: prepare AWS safely before deploying anything.

Do not skip this phase. AWS resources can cost money if left running.

## 🧰 What You Need

- AWS account
- AWS CLI v2 installed
- Docker Desktop running
- GitHub repository pushed
- Local Docker Compose project working

## ⚠️ Safety Rules

- Do not use the AWS root user for daily work.
- Do not create long-lived root access keys.
- Create a budget before deploying.
- Use one AWS Region for the whole practice project.
- Delete resources after practice.
- Never commit AWS keys or secrets.

## 🌍 Choose A Region

Pick one region and keep it consistent.

Examples:

```powershell
$env:AWS_REGION="ap-south-1"
```

or:

```powershell
$env:AWS_REGION="us-east-1"
```

Use the region closest to you or the region your course/team requires.

## 🧩 Install AWS CLI v2

Verify:

```powershell
aws --version
```

If it is missing, install AWS CLI v2 from the official AWS CLI documentation.

## 🔐 Configure Authentication

Recommended for beginners using a personal AWS account:

```powershell
aws configure
```

It asks for:

- Access key ID
- Secret access key
- Default region
- Output format

For teams or serious production work, prefer IAM Identity Center and short-lived credentials:

```powershell
aws configure sso
```

## ✅ Verify AWS Access

```powershell
aws sts get-caller-identity
```

Expected result includes:

```json
{
  "Account": "123456789012",
  "Arn": "arn:aws:iam::123456789012:user/your-user"
}
```

Save account ID for later commands:

```powershell
$env:AWS_ACCOUNT_ID=(aws sts get-caller-identity --query Account --output text)
```

## 💰 Create A Budget

Create a small monthly budget in the AWS Billing console before launching resources.

Suggested learning budget:

```text
5 USD to 10 USD
```

This is not a guarantee that AWS will stop resources. A budget alerts you so you can act quickly.

## 🧱 Services Used Later

| Service | Purpose |
| --- | --- |
| ECR | Store Docker images |
| ECS Fargate | Run containers without managing servers |
| Application Load Balancer | Route public traffic to services |
| RDS PostgreSQL | Managed PostgreSQL database |
| ElastiCache Redis | Managed Redis-compatible cache |
| Secrets Manager | Store passwords and tokens |
| CloudWatch Logs | View container logs |
| IAM | Permissions and service roles |

## 🪜 Beginner Deployment Order

Deploy in this order:

1. Push Docker images to ECR.
2. Run one simple service on ECS Fargate.
3. Add Application Load Balancer routing.
4. Add all services.
5. Replace local PostgreSQL with RDS.
6. Replace local Redis with ElastiCache.
7. Move secrets to Secrets Manager.
8. Add monitoring and cleanup.

## ✅ Checkpoint

You are ready when:

- `aws --version` works.
- `aws sts get-caller-identity` works.
- You know your chosen region.
- You created a budget or billing alert.

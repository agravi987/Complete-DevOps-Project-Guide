# API Testing

Test the app before moving to Kubernetes or AWS.

This section is part of the main workbook path. It is not optional if you want a reliable project. Python testing is optional, but Postman testing is required.

## Phases

| Phase | Open | Finish with |
| --- | --- | --- |
| 12 | [Postman API Testing](01-postman-api-testing.md) | Health, auth, product, order, and gateway requests tested manually |
| 12B | [Python API Testing](02-python-api-testing.md) | Optional one-file-at-a-time scripted checks |

## Section Checkpoint

Before moving to Kubernetes:

- Auth health works.
- Register returns `201 Created`.
- Login returns a token.
- Products can be listed.
- Orders can be created and listed.
- Gateway routes work through `localhost:8080`.

If a Postman request fails, fix the app or container stack before continuing.

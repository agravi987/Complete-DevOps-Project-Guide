import requests

BASE_URL = "http://localhost:3001"


def main():
    payload = {
        "name": "Ravi",
        "email": "ravi@example.com",
        "password": "password123",
    }

    response = requests.post(f"{BASE_URL}/auth/register", json=payload, timeout=10)
    print("Status:", response.status_code)
    print("Response:", response.json())

    assert response.status_code in (201, 409)

    print("Register test passed.")


if __name__ == "__main__":
    main()

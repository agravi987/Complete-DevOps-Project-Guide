import requests

BASE_URL = "http://localhost:3001"


def main():
    payload = {
        "email": "ravi@example.com",
        "password": "password123",
    }

    response = requests.post(f"{BASE_URL}/auth/login", json=payload, timeout=10)
    print("Status:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200
    assert response.json()["token"]

    print("Login test passed.")


if __name__ == "__main__":
    main()

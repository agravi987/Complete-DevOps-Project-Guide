import requests

BASE_URL = "http://localhost:3003"


def main():
    payload = {
        "userId": 1,
        "productId": 1,
        "quantity": 2,
    }

    response = requests.post(f"{BASE_URL}/orders", json=payload, timeout=10)
    print("Status:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 201
    assert response.json()["id"]

    print("Create order test passed.")


if __name__ == "__main__":
    main()

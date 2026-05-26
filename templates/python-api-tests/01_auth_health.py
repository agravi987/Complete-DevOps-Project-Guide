import requests

BASE_URL = "http://localhost:3001"


def main():
    response = requests.get(f"{BASE_URL}/health", timeout=10)
    print("Status:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200
    assert response.json()["status"] == "OK"

    print("Auth health test passed.")


if __name__ == "__main__":
    main()

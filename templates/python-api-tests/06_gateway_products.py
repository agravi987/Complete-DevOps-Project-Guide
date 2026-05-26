import requests

BASE_URL = "http://localhost:8080"


def main():
    response = requests.get(f"{BASE_URL}/api/products", timeout=10)
    print("Status:", response.status_code)
    print("Response:", response.json())

    products = response.json()

    assert response.status_code == 200
    assert isinstance(products, list)
    assert len(products) > 0

    print("Gateway products test passed.")


if __name__ == "__main__":
    main()

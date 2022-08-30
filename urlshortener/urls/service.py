import requests

class UrlService:
    def get_key(self):
        response = requests.get(f"http://keygenerator:8000/keys")
        assert response.status_code == 200

        return response.json()["key"]

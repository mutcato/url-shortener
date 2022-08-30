import requests

from urls.models import Url


class UrlService:
    def create_url(self, long_url: str):
        return Url.objects.create(long_url=long_url, key=self._get_key())

    @staticmethod
    def _get_key():
        response = requests.get(f"http://keygenerator:8000/keys")
        assert response.status_code == 200

        return response.json()["key"]

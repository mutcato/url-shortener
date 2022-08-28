from unittest import result

from django.test import TestCase
from model_bakery import baker


class UrlWiewsetTestCase(TestCase):
    def setUp(self) -> None:
        self.viewset_endpoint = "/urls"
        return super().setUp()

    def test_short_to_long_redirect(self):
        url = baker.make("urls.Url")
        redirect_endpoint = "/" + url.key
        response = self.client.get(redirect_endpoint)
        self.assertEqual(response.status_code, 302)
        old_hit = url.hit
        url.refresh_from_db()
        new_hit = url.hit
        self.assertEqual((new_hit - old_hit), 1)

    def test_create_url(self):
        payload = {"long_url": "https://example.com/some/example/path"}
        response = self.client.post(self.viewset_endpoint, data=payload)
        self.assertEqual(response.status_code, 201)
        result = response.json()
        self.assertEqual(result["long_url"], payload["long_url"])
        self.assertEqual(result["hit"], 0)

    def test_retrieve_url(self):
        url = baker.make("urls.Url")
        response = self.client.get(f"{self.viewset_endpoint}/{url.key}")
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result["key"], url.key)
        self.assertEqual(result["long_url"], url.long_url)
        self.assertEqual(result["hit"], url.hit)

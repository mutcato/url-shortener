from unittest import result

from django.test import TestCase
from model_bakery import baker


class UrlWiewsetTestCase(TestCase):
    def test_short_to_long_redirect(self):
        url = baker.make("urls.Url")
        redirect_endpoint = "/" + url.key
        response = self.client.get(redirect_endpoint)
        self.assertEqual(response.status_code, 302)
        old_hit = url.hit
        url.refresh_from_db()
        new_hit = url.hit
        self.assertEqual((new_hit - old_hit), 1)


from django.test import TestCase
from keys.tasks import generate_keys


class KeyViewTestCase(TestCase):
    def test_get_key_view(self):
        endpoint = "/keys"
        generate_keys(number=10)
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(type(response.json()), dict)
        self.assertIn("key", result)

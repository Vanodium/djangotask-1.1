from django.test import Client, TestCase


class StaticURLTestsCatalog(TestCase):
    def test_catalog(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_item(self):
        response = Client().get('/catalog/123')
        self.assertEqual(response.status_code, 301)

        response = Client().get('/catalog/123/')
        self.assertEqual(response.status_code, 200)

        response = Client().get('/catalog/i-want-to-rest-finally-123/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/-123')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/string')
        self.assertEqual(response.status_code, 404)

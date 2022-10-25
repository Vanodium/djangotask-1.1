from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_homepage(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_catalog(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_item(self):
        response = Client().get('/catalog/123')
        self.assertEqual(response.status_code, 200)

        response = Client().get('/catalog/-123')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/string')
        self.assertEqual(response.status_code, 404)

from django.test import Client, TestCase


class StaticURLTestsHomepage(TestCase):
    def test_homepage(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

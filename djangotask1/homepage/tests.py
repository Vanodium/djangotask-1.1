from django.test import Client, TestCase
from django.urls import reverse


class StaticURLTestsHomepage(TestCase):
    def test_homepage(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)


class TaskPagesTests(TestCase):
    def test_home_show_correct_context(self):
        response = Client().get(reverse('homepage:home'))
        self.assertIn('items', response.context)

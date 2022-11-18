from django.test import Client, TestCase

from .models import Category, Tag  # , Item


class StaticURLTestsCatalog(TestCase):
    def test_catalog(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_item(self):
        response = Client().get('/catalog/i-want-to-rest-finally-123/')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/-123')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/0')
        self.assertEqual(response.status_code, 404)

        response = Client().get('/catalog/string')
        self.assertEqual(response.status_code, 404)


class ModelsTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(name='Тест категория',
                                               slug='text-category-slug',
                                               )
        cls.tag = Tag.objects.create(is_published=True,
                                     name='Тэст тэг',
                                     slug='test-tag-slug'
                                     )

from django.test import Client, TestCase

from .models import Category, Item, Tag


class StaticURLTestsCatalog(TestCase):
    def test_catalog(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_catalog_item(self):
        response = Client().get('/catalog/123')
        self.assertEqual(response.status_code, 301)

        response = Client().get('/catalog/10/')
        self.assertEqual(response.status_code, 200)

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

    def test_able_create_one_letter(self):
        item_count = Item.objects.count()

        # with self.assertRaises(ValidationError):
        self.item = Item(name='Тест айтэм',
                         category=self.category,
                         text='test превосходно'
                         )
        self.item.full_clean()
        self.item.save()
        self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count + 1)

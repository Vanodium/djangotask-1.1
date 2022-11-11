from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from .validators import validate_desc, validate_slug, validate_weight


class Tag(models.Model):
    name = models.CharField(max_length=150, default='your name')
    is_published = models.BooleanField(default=True)
    slug = models.CharField(
        max_length=200, validators=[validate_slug], default='slug')


class Category(models.Model):
    is_published = models.BooleanField(default=True)
    name = models.CharField(max_length=150, default='your name')
    slug = models.CharField(
        max_length=200, validators=[validate_slug], default='slug')
    weight = models.IntegerField(default=100, validators=[validate_weight])


class Item(models.Model):
    is_published = models.BooleanField(default=True)
    name = models.CharField(max_length=150, default='your name')
    text = models.TextField(default='your desc', validators=[validate_desc])
    category = models.ForeignKey(
        'Category', on_delete=models.DO_NOTHING, null=True)
    images = models.ForeignKey(
        'DescriptionImages', on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField('Tag')

    class Meta:
        verbose_name = 'товар'
        verbose_name = 'товары'
        default_related_name = 'items'

    upload = models.ImageField(upload_to='uploads/%Y/%m', default='nothing')

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True


class DescriptionImages(models.Model):
    is_published = models.BooleanField(default=True)
    pictures = models.ImageField(upload_to='uploads/%Y/%m', default='nothing')

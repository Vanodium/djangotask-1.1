from django.db import models
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
    tags = models.ManyToManyField('Tag')

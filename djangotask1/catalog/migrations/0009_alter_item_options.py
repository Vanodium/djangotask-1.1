# Generated by Django 3.2.4 on 2022-11-17 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_item_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'default_related_name': 'items', 'ordering': ('category__name',), 'verbose_name': 'товары'},
        ),
    ]

# Generated by Django 3.2 on 2022-11-10 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20221110_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='upload',
            field=models.ImageField(default='nothing', upload_to='uploads/%Y/%m'),
        ),
    ]

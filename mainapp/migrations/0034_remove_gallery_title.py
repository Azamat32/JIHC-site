# Generated by Django 3.1.3 on 2021-12-20 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0033_auto_20211217_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='title',
        ),
    ]

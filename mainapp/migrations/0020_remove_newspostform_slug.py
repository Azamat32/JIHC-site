# Generated by Django 3.1.3 on 2021-12-17 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_auto_20211217_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspostform',
            name='slug',
        ),
    ]

# Generated by Django 3.1.3 on 2021-12-17 08:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_newspostform_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspostform',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]

# Generated by Django 3.1.3 on 2021-12-17 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_newspostform_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspostform',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]

# Generated by Django 3.1.3 on 2021-12-17 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_remove_navlist_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navlist',
            name='name',
        ),
        migrations.AddField(
            model_name='navlist',
            name='description',
            field=models.TextField(default='', max_length=255),
        ),
    ]

# Generated by Django 3.1.3 on 2021-12-16 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20211216_2328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentpageform',
            name='video',
        ),
    ]
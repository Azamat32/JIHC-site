# Generated by Django 3.1.3 on 2021-12-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_studentpageform_video_descriptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentpageform',
            name='description2',
            field=models.TextField(default=None, max_length=255),
        ),
    ]

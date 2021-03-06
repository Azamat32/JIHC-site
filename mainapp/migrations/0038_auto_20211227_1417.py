# Generated by Django 3.1.3 on 2021-12-27 08:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0037_auto_20211224_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='clubs_page_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])], verbose_name='Основной плеер страницы')),
                ('title', models.CharField(default='', max_length=20)),
                ('club_description', models.TextField(default='', max_length=500)),
                ('img', models.ImageField(upload_to='gallery')),
            ],
        ),
        migrations.AddField(
            model_name='talapkerpagetable',
            name='table_description2',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='talapkerpagetable',
            name='table_description',
            field=models.TextField(max_length=100),
        ),
    ]

# Generated by Django 3.1.3 on 2021-12-17 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20211217_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navlist',
            name='slug',
        ),
        migrations.AlterField(
            model_name='navlist',
            name='description',
            field=models.TextField(default='', max_length=600, verbose_name=' Первый абзац'),
        ),
        migrations.AlterField(
            model_name='navlist',
            name='description_second',
            field=models.TextField(default='', max_length=600, verbose_name=' Второй абзац'),
        ),
    ]

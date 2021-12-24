# Generated by Django 3.1.3 on 2021-12-24 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0035_auto_20211220_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='students_life',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='gallery')),
                ('description', models.TextField(default='', max_length=600)),
            ],
        ),
        migrations.AlterField(
            model_name='newsbigpost',
            name='description',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='newslongpost',
            name='description',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='newspostform',
            name='description',
            field=models.TextField(max_length=900),
        ),
        migrations.AlterField(
            model_name='newspostform',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='newsshortpost',
            name='description',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='talapkerpost',
            name='description',
            field=models.TextField(max_length=400),
        ),
    ]
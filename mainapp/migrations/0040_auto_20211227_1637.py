# Generated by Django 3.1.3 on 2021-12-27 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0039_auto_20211227_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubs_page_form',
            name='img',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='clubImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='gallery')),
                ('club', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainapp.clubs_page_form')),
            ],
        ),
    ]

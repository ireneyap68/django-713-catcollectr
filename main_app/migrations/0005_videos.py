# Generated by Django 3.1.1 on 2020-09-29 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_cat_cattoys'),
    ]

    operations = [
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=32)),
                ('file_name', models.CharField(max_length=500)),
            ],
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-24 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cat_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatToy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
    ]

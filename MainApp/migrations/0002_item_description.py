# Generated by Django 4.2.4 on 2023-09-06 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='Базовое описание', max_length=200),
        ),
    ]
# Generated by Django 3.1 on 2020-08-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0005_auto_20200817_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(upload_to='category', verbose_name='Obrazek'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='assets/img/products/', verbose_name='Obrazek'),
        ),
    ]

# Generated by Django 3.1 on 2020-08-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0015_auto_20200826_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Cena'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vat',
            field=models.FloatField(verbose_name='Vat'),
        ),
    ]

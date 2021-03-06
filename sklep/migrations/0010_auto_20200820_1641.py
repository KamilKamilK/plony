# Generated by Django 3.1 on 2020-08-20 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0009_auto_20200820_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='description',
            field=models.TextField(default='', verbose_name='Opis'),
        ),
        migrations.AddField(
            model_name='season',
            name='img',
            field=models.ImageField(default=1, upload_to='season', verbose_name='Obrazek'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='season',
            name='name',
            field=models.CharField(default='', max_length=64, verbose_name='Nazwa'),
        ),
    ]

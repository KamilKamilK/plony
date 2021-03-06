# Generated by Django 3.1 on 2020-08-20 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0008_auto_20200818_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='season',
            name='slug',
            field=models.SlugField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='employee',
            name='img',
            field=models.ImageField(upload_to='team', verbose_name='Zdjęcie'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='occupation',
            field=models.CharField(max_length=64, verbose_name='Stanowisko'),
        ),
        migrations.AlterField(
            model_name='season',
            name='name',
            field=models.CharField(default='', max_length=64),
        ),
    ]

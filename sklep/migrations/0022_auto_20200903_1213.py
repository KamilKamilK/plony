# Generated by Django 3.1 on 2020-09-03 12:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0021_season_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='season', verbose_name='Obrazek'),
            preserve_default=False,
        ),
    ]

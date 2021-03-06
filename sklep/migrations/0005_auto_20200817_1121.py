# Generated by Django 3.1 on 2020-08-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0004_auto_20200816_1333'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Services',
        ),
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(default=0, upload_to='assets/img/category/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='img',
            field=models.ImageField(default=1, upload_to='assets/img/team/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default=1, upload_to='assets/img/products/'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.2 on 2021-11-15 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211115_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='i_stock',
            name='label',
        ),
        migrations.AlterField(
            model_name='i_stock',
            name='image',
            field=models.ImageField(max_length=255, upload_to='pictures/%Y/%m/%d'),
        ),
    ]

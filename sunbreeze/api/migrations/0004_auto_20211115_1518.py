# Generated by Django 3.1.2 on 2021-11-15 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211115_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='i_stock',
            name='image',
            field=models.ImageField(upload_to='pictures/%Y/%m/%d'),
        ),
    ]

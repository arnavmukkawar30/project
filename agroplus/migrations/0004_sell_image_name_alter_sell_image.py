# Generated by Django 4.0 on 2022-06-08 19:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('agroplus', '0003_alter_sell_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='Image_Name',
            field=models.CharField(default='image', max_length=20),
        ),
        migrations.AlterField(
            model_name='sell',
            name='Image',
            field=models.ImageField(default=datetime.datetime(2022, 6, 8, 19, 26, 16, 33374, tzinfo=utc), upload_to='static/Sell_images'),
        ),
    ]
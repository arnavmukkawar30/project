# Generated by Django 4.0 on 2022-06-09 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agroplus', '0011_alter_sell_price_alter_sell_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='Image',
            field=models.ImageField(blank=True, default='static/Sell_images/AGROPLUS.png', null=True, upload_to='static/Sell_images'),
        ),
    ]

# Generated by Django 4.0 on 2022-06-10 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agroplus', '0019_alter_sell_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell',
            name='Image',
            field=models.ImageField(upload_to=''),
        ),
    ]

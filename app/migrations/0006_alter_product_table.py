# Generated by Django 5.0.3 on 2024-03-24 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_product_product_information_product_slug_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='product',
            table='app_Product',
        ),
    ]
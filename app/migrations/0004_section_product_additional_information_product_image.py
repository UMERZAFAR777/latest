# Generated by Django 5.0 on 2024-02-13 04:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_main_categroy_categroy_sub_categroy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_Quantity', models.IntegerField()),
                ('Availbility', models.IntegerField()),
                ('Featured_Image', models.CharField(max_length=100)),
                ('Product_Name', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('Discount', models.IntegerField()),
                ('Product_Information', models.TextField()),
                ('Model_Name', models.CharField(max_length=100)),
                ('Tags', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Categroy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categroy')),
                ('Section', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.section')),
            ],
        ),
        migrations.CreateModel(
            name='Additional_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Specification', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=100)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image_url', models.CharField(max_length=100)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management', '0002_prices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockin',
            name='date_added',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='stockin',
            name='product',
            field=models.CharField(max_length=100),
        ),
    ]

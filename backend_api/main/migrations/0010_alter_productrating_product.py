# Generated by Django 5.0.3 on 2024-03-25 15:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_productrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrating',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_ratings', to='main.product'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-24 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_product_category_product_vendor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='details',
            new_name='detail',
        ),
    ]

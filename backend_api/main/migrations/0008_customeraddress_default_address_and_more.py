# Generated by Django 5.0.3 on 2024-03-25 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_customeraddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraddress',
            name='default_address',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customeraddress',
            name='address',
            field=models.TextField(),
        ),
    ]

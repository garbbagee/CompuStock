# Generated by Django 5.1.4 on 2025-01-17 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CompuStockApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]

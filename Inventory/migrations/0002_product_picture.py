# Generated by Django 4.2.20 on 2025-04-22 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(null=True, upload_to='imgaes/'),
        ),
    ]

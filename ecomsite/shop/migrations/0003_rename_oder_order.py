# Generated by Django 5.0 on 2024-01-05 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_oder'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oder',
            new_name='Order',
        ),
    ]

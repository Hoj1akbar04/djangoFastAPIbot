# Generated by Django 5.0.3 on 2024-06-18 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
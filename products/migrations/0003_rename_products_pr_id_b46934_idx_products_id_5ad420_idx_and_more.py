# Generated by Django 5.0.3 on 2024-06-17 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_count_alter_product_name'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='product',
            new_name='products_id_5ad420_idx',
            old_name='products_pr_id_b46934_idx',
        ),
        migrations.AlterModelTable(
            name='product',
            table='products',
        ),
    ]
# Generated by Django 5.1.4 on 2025-01-16 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_slug_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
    ]

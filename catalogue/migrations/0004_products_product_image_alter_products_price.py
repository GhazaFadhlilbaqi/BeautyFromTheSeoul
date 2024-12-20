# Generated by Django 5.1.2 on 2024-10-25 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_alter_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_image',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.IntegerField(),
        ),
    ]

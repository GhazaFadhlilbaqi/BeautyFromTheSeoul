# Generated by Django 5.1 on 2024-10-23 15:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="adentry",
            name="image",
            field=models.URLField(max_length=300),
        ),
    ]

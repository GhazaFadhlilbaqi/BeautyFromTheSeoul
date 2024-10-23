# Generated by Django 5.1 on 2024-10-22 14:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdEntry",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("brand_name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="ads/")),
            ],
        ),
    ]

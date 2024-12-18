# Generated by Django 5.1.3 on 2024-12-05 14:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("message", models.CharField(max_length=1000)),
                ("phone", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=254)),
                ("still_actual", models.BooleanField(default=True)),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-18 22:35

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userauth", "0004_rename_full_discription_story_full_description_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="LikePost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("post_id", models.CharField(max_length=500)),
                ("username", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="story",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("0999ffeb-17b8-40e7-b086-0dce3a6c1e6d"),
                primary_key=True,
                serialize=False,
            ),
        ),
    ]

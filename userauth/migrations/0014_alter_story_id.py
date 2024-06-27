# Generated by Django 5.0.6 on 2024-06-20 02:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userauth", "0013_alter_story_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="story",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("2ef3f9e7-3af1-4e9c-9024-37837dc3a82c"),
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
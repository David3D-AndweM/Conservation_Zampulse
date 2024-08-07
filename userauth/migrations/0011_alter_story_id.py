# Generated by Django 5.0.6 on 2024-06-20 01:56

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userauth", "0010_alter_story_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="story",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("850f2a01-4363-474e-9a1b-ebe3d1dac74b"),
                primary_key=True,
                serialize=False,
            ),
        ),
    ]

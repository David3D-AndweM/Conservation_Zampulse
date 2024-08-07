# Generated by Django 5.0.6 on 2024-06-24 01:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userauth", "0015_alter_story_id_followers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="story",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("f6722a38-639f-4e7f-a6b1-40e70cfe8d59"),
                primary_key=True,
                serialize=False,
            ),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-24 01:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userauth", "0018_alter_followers_user_alter_story_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="followers",
            name="created_at",
        ),
        migrations.AlterField(
            model_name="story",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("0a2b11db-b056-42ec-8572-2a19406e1bae"),
                primary_key=True,
                serialize=False,
            ),
        ),
    ]

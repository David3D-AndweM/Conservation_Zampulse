# Generated by Django 5.1b1 on 2024-07-19 17:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0023_alter_story_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='id',
            field=models.UUIDField(default=uuid.UUID('534a939d-2151-4b06-b511-a10afef97286'), primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 5.1b1 on 2024-07-19 18:01

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0024_alter_story_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='id',
            field=models.UUIDField(default=uuid.UUID('fdb1fa22-222c-43d9-a2b6-6524e4ba2c22'), primary_key=True, serialize=False),
        ),
    ]

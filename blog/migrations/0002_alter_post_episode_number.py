# Generated by Django 4.2.3 on 2023-07-20 06:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="episode_number",
            field=models.PositiveIntegerField(
                default=1, editable=False, unique=True
            ),
        ),
    ]

# Generated by Django 5.2.4 on 2025-07-16 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_initial"),
        ("tools", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tool",
            name="items",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="posts.idea",
                verbose_name="SW목록",
            ),
        ),
    ]

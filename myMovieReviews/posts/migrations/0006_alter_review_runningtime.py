# Generated by Django 5.2.4 on 2025-07-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_alter_review_runningtime"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="runningTime",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.1 on 2022-08-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("urls", "0003_remove_url_urls_url_key_59c420_idx_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="url",
            name="hit",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
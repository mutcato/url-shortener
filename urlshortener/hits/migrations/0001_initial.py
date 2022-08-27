# Generated by Django 4.1 on 2022-08-27 10:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("urls", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                ("ip_address", models.GenericIPAddressField()),
                ("user_agent", models.CharField(max_length=512)),
                (
                    "url",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hits",
                        related_query_name="hit",
                        to="urls.url",
                    ),
                ),
            ],
            options={
                "verbose_name": "hit",
                "verbose_name_plural": "hits",
                "ordering": ("-created_at",),
            },
        ),
        migrations.AddIndex(
            model_name="hit",
            index=models.Index(
                fields=["ip_address", "user_agent"], name="hits_hit_ip_addr_e2c70f_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="hit",
            index=models.Index(
                fields=["-created_at"], name="hits_hit_created_933423_idx"
            ),
        ),
    ]

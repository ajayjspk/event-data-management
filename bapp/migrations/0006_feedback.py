# Generated by Django 4.1.6 on 2023-02-22 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bapp", "0005_eve_register"),
    ]

    operations = [
        migrations.CreateModel(
            name="feedback",
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
                ("message", models.CharField(max_length=80)),
                ("fname", models.CharField(max_length=15)),
                ("lname", models.CharField(max_length=15)),
                ("email", models.CharField(max_length=40)),
            ],
        ),
    ]
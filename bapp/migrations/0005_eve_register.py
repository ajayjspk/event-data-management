# Generated by Django 4.1.6 on 2023-02-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bapp", "0004_alter_register_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="eve_register",
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
                ("userid", models.CharField(max_length=15)),
                ("event", models.CharField(max_length=20)),
            ],
        ),
    ]

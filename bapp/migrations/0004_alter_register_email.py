# Generated by Django 4.1.6 on 2023-02-15 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bapp", "0003_delete_login_rename_fname_register_userid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="register", name="email", field=models.CharField(max_length=40),
        ),
    ]

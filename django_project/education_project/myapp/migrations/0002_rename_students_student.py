# Generated by Django 4.2.1 on 2023-06-05 10:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Students",
            new_name="Student",
        ),
    ]
# Generated by Django 5.0.3 on 2024-05-07 21:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("normalpoll", "0002_choice"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="poll",
            name="owner",
        ),
        migrations.RemoveField(
            model_name="poll",
            name="voters",
        ),
        migrations.DeleteModel(
            name="Choice",
        ),
        migrations.DeleteModel(
            name="Poll",
        ),
    ]
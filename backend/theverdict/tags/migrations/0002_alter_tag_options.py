# Generated by Django 5.0.1 on 2024-01-18 14:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tags", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={"ordering": ["label"]},
        ),
    ]
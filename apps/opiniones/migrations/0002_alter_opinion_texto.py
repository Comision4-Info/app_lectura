# Generated by Django 4.2.2 on 2023-07-17 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("opiniones", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="opinion",
            name="texto",
            field=models.TextField(verbose_name="Opinion"),
        ),
    ]
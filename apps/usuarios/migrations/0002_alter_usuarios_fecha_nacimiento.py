# Generated by Django 4.2.2 on 2023-07-07 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuarios",
            name="fecha_nacimiento",
            field=models.DateField(default="2000-1-1", verbose_name="Fecha_nacimiento"),
        ),
    ]

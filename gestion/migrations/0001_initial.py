# Generated by Django 5.1.3 on 2024-11-18 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Supercomputadora",
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
                ("nombre", models.CharField(max_length=100)),
                ("pais", models.CharField(max_length=50)),
                ("numero_cores", models.IntegerField()),
                ("ram_tb", models.FloatField()),
                ("almacenamiento_tb", models.FloatField()),
                ("teraflops", models.FloatField()),
                ("sistema_operativo", models.CharField(max_length=100)),
            ],
        ),
    ]

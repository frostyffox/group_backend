# Generated by Django 4.2.17 on 2025-01-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="terminazioniOttiche",
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
                ("codice_tfo", models.CharField(max_length=50)),
                ("edificio_id", models.IntegerField()),
                ("piano", models.CharField(max_length=50)),
                ("scala", models.CharField(max_length=50)),
                ("interno", models.CharField(max_length=50)),
                ("posizione_dettagliata", models.TextField()),
            ],
        ),
    ]

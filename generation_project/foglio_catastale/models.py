

# Create your models here.
from django.contrib.gis.db import models
from django.utils.timezone import now

class FoglioCatastale(models.Model):
    codice_foglio = models.CharField(max_length=50, unique=True)  # ID del foglio catastale
    nome_foglio = models.CharField(max_length=100, blank=True, null=True)  # Nome descrittivo (opzionale)
    comune = models.CharField(max_length=100)  # Nome del comune
    geojson_perimetro = models.JSONField()  # GeoJSON per il perimetro del foglio
    geojson_edifici = models.JSONField()  # GeoJSON per gli edifici
    data_creazione = models.DateTimeField(default=now)  # Timestamp per la creazione
    data_modifica = models.DateTimeField(auto_now=True)  # Timestamp aggiornato automaticamente

    def __str__(self):
        return f"Foglio {self.codice_foglio} - {self.comune}"
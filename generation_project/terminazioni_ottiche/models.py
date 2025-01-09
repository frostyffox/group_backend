# Create your models here.
from django.contrib.gis.db import models
from django.utils.timezone import now

class terminazioniOttiche(models.Model):
    codice_tfo = models.CharField(max_length=50) 
    edificio_id = models.IntegerField()
    piano = models.CharField(max_length=50)  
    scala = models.CharField(max_length=50)  
    interno = models.CharField(max_length=50)  
    posizione_dettagliata = models.TextField()


def __str__(self):
        return f"terminazioni {self.codice_tfo} - {self.edificio_id}"
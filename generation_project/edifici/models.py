from django.db import models
from django.contrib.gis.db import models


class Edificio(models.Model):
    indirizzo = models.CharField(max_length=255)
    coordinate = models.PointField(geography=True, srid=4326)
    codice_catastale = models.CharField(max_length=50, unique=True)
    tipo_edificio = models.CharField(max_length=50)
    data_predisposizione = models.DateField

class Meta:
    db_table = 'edifici'

def __str__ (self):
    return f"{self.indirizzo} {self.coordinate} {self.codice_catastale} {self.tipo_edificio} {self.data_predisposizione}"
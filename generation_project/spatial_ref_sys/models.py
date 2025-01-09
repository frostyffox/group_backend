# Create your models here.

from django.db import models

class SpatialRefSys(models.Model):
    srid = models.IntegerField()
    auth_name = models.CharField(max_length=205)
    auth_srid = models.IntegerField()
    srtext = models.TextField()
    proj4text = models.TextField()

def __str__(self):
        return f"{self.srid} {self.auth_name} {self.auth_srid} {self.srtext} {self.proj4text}"
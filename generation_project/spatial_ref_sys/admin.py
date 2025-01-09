# Register your models here.
from django.contrib import admin
from .models import SpatialRefSys

@admin.register(SpatialRefSys)
class FoglioCatAdmin(admin.ModelAdmin):
    list_display = ('srid', 'auth_name')
    search_fields = ('srid','auth_name')
    list_filter = ('srid', 'auth_name')
    
    #auth_name = models.CharField(max_length=205)
    #auth_srid = models.IntegerField()
   # srtext = models.TextField()
   # proj4text = models.TextField()

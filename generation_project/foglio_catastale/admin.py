# Register your models here.
from django.contrib import admin
from .models import FoglioCatastale

@admin.register(FoglioCatastale)
class FoglioCatAdmin(admin.ModelAdmin):
    list_display = ('codice_foglio', 'comune', 'geojson_perimetro','geojson_edifici')
    search_fields = ('codice_foglio', 'comune','geojson_edifici')
    list_filter = ('codice_foglio','comune')
    

# Register your models here.
from django.contrib import admin
from .models import Edificio

@admin.register(Edificio)
class EdificioAdmin(admin.ModelAdmin):
    list_display = ('indirizzo', 'codice_catastale', 'tipo_edificio', 'data_predisposizione')
    search_fields = ('indirizzo', 'codice_catastale')
    list_filter = ('tipo_edificio',)
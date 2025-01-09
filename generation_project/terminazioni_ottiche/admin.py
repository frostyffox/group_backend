from django.contrib import admin
from .models import terminazioniOttiche

@admin.register(terminazioniOttiche)
class terminazioniOtticheAdmin(admin.ModelAdmin):
    list_display = ('codice_tfo', 'edificio_id','piano','scala', 'interno','posizione_dettagliata')
    search_fields = ('codice_tfo','edificio_id','piano')
    list_filter = ('codice_tfo', 'edificio_id')
    

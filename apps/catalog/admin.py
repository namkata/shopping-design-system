from django.contrib import admin
from .models import Catalog


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_updated', 'created_at', 'updated_at')
    search_fields = ('name',)
    readonly_fields = ('last_updated',)

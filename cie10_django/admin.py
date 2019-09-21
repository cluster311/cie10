from django.contrib import admin
from .models import CIE10, Source


@admin.register(CIE10)
class CIE10Admin(admin.ModelAdmin):
    list_display = ['code', 'source', 'description', 'level', 'depends_on']
    search_fields = ['code', 'description']
    list_filter = ['source', 'depends_on']


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

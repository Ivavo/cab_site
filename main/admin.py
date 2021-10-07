from django.contrib import admin
from .models import Blog, Procedures, Record, Records


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_name', 'short_text', 'posted_date', 'edit_date']


@admin.register(Procedures)
class ProceduresAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'procedure_time']


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number']


@admin.register(Records)
class RecordsAdmin(admin.ModelAdmin):
    list_display = ['day', 'hour', 'record']




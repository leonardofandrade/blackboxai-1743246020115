from django.contrib import admin
from .models import (
    ProcedureType,
    DocumentType,
    ExtractionRequest,
    ExtractionRequestProcedure,
    ExtractionRequestDocument
)

@admin.register(ProcedureType)
class ProcedureTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ExtractionRequestProcedureInline(admin.TabularInline):
    model = ExtractionRequestProcedure
    extra = 0

class ExtractionRequestDocumentInline(admin.TabularInline):
    model = ExtractionRequestDocument
    extra = 0

@admin.register(ExtractionRequest)
class ExtractionRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'request_date', 'requested_by')
    list_filter = ('request_date',)
    search_fields = ('requested_by', 'additional_info')
    inlines = [ExtractionRequestProcedureInline, ExtractionRequestDocumentInline]
    date_hierarchy = 'request_date'

@admin.register(ExtractionRequestProcedure)
class ExtractionRequestProcedureAdmin(admin.ModelAdmin):
    list_display = ('extraction_request', 'procedure_type', 'year', 'number')
    list_filter = ('procedure_type', 'year')
    search_fields = ('number', 'additional_info')
    autocomplete_fields = ['procedure_type']

@admin.register(ExtractionRequestDocument)
class ExtractionRequestDocumentAdmin(admin.ModelAdmin):
    list_display = ('extraction_request', 'document_type', 'year', 'number', 'attached_file')
    list_filter = ('document_type', 'year')
    search_fields = ('number', 'additional_info')
    autocomplete_fields = ['document_type']

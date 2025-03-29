from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .models import ExtractionRequest, ExtractionRequestProcedure, ExtractionRequestDocument
from .forms import ExtractionRequestForm, ExtractionRequestProcedureForm, ExtractionRequestDocumentForm

class ExtractionRequestListView(ListView):
    model = ExtractionRequest
    template_name = 'extraction/extraction_request_list.html'
    context_object_name = 'requests'
    ordering = ['-request_date']

class ExtractionRequestCreateView(CreateView):
    model = ExtractionRequest
    form_class = ExtractionRequestForm
    template_name = 'extraction/extraction_request_form.html'
    success_url = reverse_lazy('extraction:request_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Solicitação criada com sucesso!')
        return response

class ExtractionRequestDetailView(UpdateView):
    model = ExtractionRequest
    form_class = ExtractionRequestForm
    template_name = 'extraction/extraction_request_detail.html'
    success_url = reverse_lazy('extraction:request_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['procedures'] = self.object.procedures.all()
        context['documents'] = self.object.documents.all()
        context['procedure_form'] = ExtractionRequestProcedureForm()
        context['document_form'] = ExtractionRequestDocumentForm()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Solicitação atualizada com sucesso!')
        return response

def add_procedure(request, pk):
    extraction_request = get_object_or_404(ExtractionRequest, pk=pk)
    if request.method == 'POST':
        form = ExtractionRequestProcedureForm(request.POST)
        if form.is_valid():
            procedure = form.save(commit=False)
            procedure.extraction_request = extraction_request
            procedure.save()
            messages.success(request, 'Procedimento adicionado com sucesso!')
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'})

def edit_procedure(request, pk, procedure_id):
    procedure = get_object_or_404(ExtractionRequestProcedure, pk=procedure_id, extraction_request_id=pk)
    if request.method == 'POST':
        form = ExtractionRequestProcedureForm(request.POST, instance=procedure)
        if form.is_valid():
            form.save()
            messages.success(request, 'Procedimento atualizado com sucesso!')
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'})

def delete_procedure(request, pk, procedure_id):
    procedure = get_object_or_404(ExtractionRequestProcedure, pk=procedure_id, extraction_request_id=pk)
    if request.method == 'POST':
        procedure.delete()
        messages.success(request, 'Procedimento excluído com sucesso!')
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'})

def add_document(request, pk):
    extraction_request = get_object_or_404(ExtractionRequest, pk=pk)
    if request.method == 'POST':
        form = ExtractionRequestDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.extraction_request = extraction_request
            document.save()
            messages.success(request, 'Documento adicionado com sucesso!')
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'})

def edit_document(request, pk, document_id):
    document = get_object_or_404(ExtractionRequestDocument, pk=document_id, extraction_request_id=pk)
    if request.method == 'POST':
        form = ExtractionRequestDocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            messages.success(request, 'Documento atualizado com sucesso!')
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'})

def delete_document(request, pk, document_id):
    document = get_object_or_404(ExtractionRequestDocument, pk=document_id, extraction_request_id=pk)
    if request.method == 'POST':
        document.delete()
        messages.success(request, 'Documento excluído com sucesso!')
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'})

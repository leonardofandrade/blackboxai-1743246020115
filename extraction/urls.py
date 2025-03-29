from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'extraction'

urlpatterns = [
    # URLs para ExtractionRequest
    path('', views.ExtractionRequestListView.as_view(), name='request_list'),
    path('create/', views.ExtractionRequestCreateView.as_view(), name='request_create'),
    path('<int:pk>/', views.ExtractionRequestDetailView.as_view(), name='request_detail'),
    
    # URLs para Procedures
    path('<int:pk>/procedures/add/', views.add_procedure, name='add_procedure'),
    path('<int:pk>/procedures/<int:procedure_id>/edit/', views.edit_procedure, name='edit_procedure'),
    path('<int:pk>/procedures/<int:procedure_id>/delete/', views.delete_procedure, name='delete_procedure'),
    
    # URLs para Documents
    path('<int:pk>/documents/add/', views.add_document, name='add_document'),
    path('<int:pk>/documents/<int:document_id>/edit/', views.edit_document, name='edit_document'),
    path('<int:pk>/documents/<int:document_id>/delete/', views.delete_document, name='delete_document'),
]

# Adicionar URLs para servir arquivos de mídia em desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
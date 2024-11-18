from django.urls import path
from . import views

app_name = 'importer_export'

urlpatterns = [
    path('', views.ImportarDadosView.as_view(), name='importar_export_arquivo'),
    path('exporter/', views.exporter, name='exporter'),
    path('criar/', views.criar.as_view(), name='criar'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),   
]
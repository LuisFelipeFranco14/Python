from django.urls import path 
from Rent import views

app_name = 'rent'

urlpatterns = [
    path('list-location/', views.list_location, name='list-location'),  
    path('form-client/', views.form_client, name='client-create'),  
    path('form-immobile/', views.form_immobile, name='immobile-create'),
    path('form-location/<int:id>/', views.form_location, name='location-create'), 
    path('reports/', views.reports, name='reports'),
    path('report-client/', views.report_client, name='report-client'),
]
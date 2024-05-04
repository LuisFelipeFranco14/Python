from django.urls import path 
from Profile_rent import views

app_name = 'profile_rent'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
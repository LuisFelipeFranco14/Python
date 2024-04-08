from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show',
    ordering = 'id', #descrencete seria o -id
    # list_filter = 'create_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 5
    list_max_show_all = 10 #mostrar tudo 
    list_editable = 'first_name', 'last_name', 'show', #editar as informações
    list_display_links = 'id', 'phone', #cria link no campo para acessar o registro 

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id', #descrencete seria o -id
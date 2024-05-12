from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('retorna_qtd_vendas', views.retorna_qtd_vendas, name="retorna_qtd_vendas"),
    path('retorna_total_vendido', views.retorna_total_vendido, name="retorna_total_vendido"),
    path('retorna_media_venda', views.retorna_media_venda, name="retorna_media_venda"),
    path('relatorio_faturamento', views.relatorio_faturamento, name="relatorio_faturamento"),
    path('relatorio_produtos', views.relatorio_produtos, name="relatorio_produtos"),
    path('relatorio_funcionario', views.relatorio_funcionario, name="relatorio_funcionario")
]
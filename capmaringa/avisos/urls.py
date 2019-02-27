from django.urls import path

from avisos import views


app_name = 'avisos'

urlpatterns = [
    path('avisos/', views.listar_avisos, name='listar_avisos'),
    path('<int:aviso_id>/detalhes/', views.detalhes, name='detalhes'),
    path('criar_aviso/', views.criar_avisos, name='criar_avisos'),
]
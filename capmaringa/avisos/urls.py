from django.urls import path

from avisos import views


app_name = 'avisos'

urlpatterns = [
    path('avisos/', views.lista_avisos, name='lista_avisos'),
    path('<int:aviso_id>/detalhes/', views.aviso_detalhes, name='aviso_detalhes'),
    path('criar_aviso/', views.criar_aviso, name='criar_aviso'),
]
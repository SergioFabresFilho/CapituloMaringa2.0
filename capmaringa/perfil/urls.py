from django.urls import path

from perfil import views

app_name = 'perfil'

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('perfil_login/', views.perfil_login, name='perfil_login'),
    path('perfil_logout/', views.perfil_logout, name='perfil_logout'),
]
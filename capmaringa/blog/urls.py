from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('criar_post/', views.criar_post, name='criar_post'),
    path('posts/', views.lista_posts, name='lista_posts'),
    path('<int:post_id>/editar_post/', views.editar_post, name='editar_post'),
]
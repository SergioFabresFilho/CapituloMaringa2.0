from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('criar_post/', views.criar_posts, name='criar_posts'),
    path('posts/', views.listar_posts, name='listar_posts'),
    path('<int:post_id>/editar_post/', views.editar_posts, name='editar_posts'),
]
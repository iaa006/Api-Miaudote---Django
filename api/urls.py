from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_usuarios, name='get_all_usuarios'),
    path("usuario/<str:id>", views.get_by_id),
    path("data/", views.usuario_manager)
]

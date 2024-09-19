from django.urls import path
from . import views

app_name="api"

urlpatterns = [
    path('login/', views.logar, name="login"),
    path('logout/', views.logout),
    path('doacao/', view=views.animals),
    path('doacao/<int:id>', view=views.get_animal),
    path("", views.get_usuarios, name='get_all_usuarios'),
    path("usuario/<str:id>", views.get_by_id),
    path("data/", views.usuario_manager)
]
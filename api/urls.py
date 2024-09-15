from django.urls import path
from . import views

urlpatterns = [
    path('doacao/', view=views.animals),
    path('doacao/<int:id>', view=views.get_animal)
]
# audiolibros/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_audiolibros, name='lista_audiolibros'),
    path('crear/', views.crear_audiolibro, name='crear_audiolibro'),
    path('editar/<int:pk>/', views.editar_audiolibro, name='editar_audiolibro'),
    path('eliminar/<int:pk>/', views.eliminar_audiolibro, name='eliminar_audiolibro'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.clientes, name='cli'),
    path('listado/', views.listado_cli, name='list_cli'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.clientes, name='clientes'),
    path('listado/', views.listado_cli, name='list_clientes'),
]
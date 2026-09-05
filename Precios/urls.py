from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_precios, name='lista_precios'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicios/', views.servicios, name='servicios'),
    # Aquí está la ruta dinámica que te pidieron
    path('perfil/<str:nombre_usuario>/', views.perfiles, name='perfil'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('catalogo/', views.catalogo, name='catalogo_autos'),
    path('agregar/', views.crear_auto, name='crear_auto'),
    path('<int:id>/editar/', views.editar_auto, name='editar_auto'),
    path('<int:id>/eliminar/', views.eliminar_auto, name='eliminar_auto'),
]
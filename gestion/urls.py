from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_supercomputadoras, name='listar_supercomputadoras'),  # Lista supercomputadoras
    path('crear/', views.crear_supercomputadora, name='crear_supercomputadora'),  # Crear supercomputadora
    path('editar/<int:id>/', views.editar_supercomputadora, name='editar_supercomputadora'),
    path('eliminar/<int:id>/', views.eliminar_supercomputadora, name='eliminar_supercomputadora'),
]

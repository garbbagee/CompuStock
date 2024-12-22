from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.index, name='index'),
    
    # Quiénes somos
    path('nosotros/', views.nosotros, name='nosotros'),
    
    # Login (Acceso a la cuenta)
    path('login/', views.login_view, name='login'),
    
    # Registro de nuevo usuario
    path('registro/', views.register_view, name='register'),
    
    # Categorías
    path('hardware/', views.hardware, name='hardware'),
    path('perifericos/', views.perifericos, name='perifericos'),
    path('accesorios/', views.accesorios, name='accesorios'),
    
    # Ofertas
    path('ofertas/', views.ofertas, name='ofertas'),
    
    # Soporte
    path('soporte/', views.soporte, name='soporte'),
]

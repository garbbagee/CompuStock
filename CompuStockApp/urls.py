from django.urls import path
from . import views
from django.conf import settings  # Importa settings correctamente
from django.conf.urls.static import static

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

    # Inventario CRUD
    path('inventario/', views.inventario, name='inventario'),
]

# Solo agrega esta línea si estás en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

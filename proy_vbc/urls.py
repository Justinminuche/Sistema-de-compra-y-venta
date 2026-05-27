"""
URL configuration for proy_vbc project.
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
# Importamos la vista del Home que tienes en tu app core
from core.views import HomeTemplateView 

urlpatterns = [
    # 1. LA RAÍZ AHORA SÍ CARGA TU SITIO WEB (EL DASHBOARD HERMOSO)
    path('', HomeTemplateView.as_view(), name='home'),
    
    # 2. EL PANEL DE CONTROL DE ADMINISTRACIÓN
    path('admin/', admin.site.urls),
    
    # 3. LAS RUTAS DE TUS APLICACIONES (Mantenemos los includes nativos)
    path('core/', include('core.urls', namespace='core')),
    path('commerce/', include('commerce.urls', namespace='commerce')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
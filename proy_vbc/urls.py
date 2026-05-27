"""
URL configuration for proy_vbc project.
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.views.generic import RedirectView  # <-- AGREGAMOS ESTA IMPORTACIÓN

urlpatterns = [
    # 1. LA RAÍZ REAL AHORA REDIRIGE DIRECTO AL LOGIN DEL ADMIN
    path('', RedirectView.as_view(url='/admin/', permanent=False)),
    
    # 2. EL PANEL DE CONTROL
    path('admin/', admin.site.urls),
    
    # 3. LAS RUTAS DE TUS APPLICACIONES CON UN PREFIJO PARA QUE NO CHOQUEN CON LA RAÍZ
    path('sistema/', include('core.urls', namespace='core')),
    path('tienda/', include('commerce.urls', namespace='commerce')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
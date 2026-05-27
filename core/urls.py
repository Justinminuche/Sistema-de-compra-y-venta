from django.urls import path
from django.views.generic import RedirectView  # <-- AGREGA ESTA LÍNEA
from core import views

app_name = 'core'

urlpatterns = [
    # Cambiamos tu HomeTemplateView por una redirección al login del admin:
    path('', RedirectView.as_view(url='/admin/', permanent=False), name='home'),
    
    path('supplier_list/', views.SupplierListView.as_view(), name='supplier_list'),
    path('supplier_create/', views.SupplierCreateView.as_view(), name='supplier_create'),
    path('supplier_update/<int:pk>/', views.SupplierUpdateView.as_view(), name='supplier_update'),
    path('supplier_detail/<int:pk>/', views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('supplier_delete/<int:pk>/', views.SupplierDeleteView.as_view(), name='supplier_delete'),
]
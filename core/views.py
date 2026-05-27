from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
# QUITAMOS EL LOGINREQUIREDMIXIN DE AQUÍ
from core.mixins import TitleContextMixin
from core.forms import SupplierForm
from .models import Supplier, Product, Customer, Brand
from commerce.models import Invoice, Purchase
from django.db.models import Q
from django.urls import reverse_lazy


def home(request):
    data = {
        "title1": "Autor | TeacherCode",
        "title2": "Super Mercado Economico"
    }
    return render(request, 'home.html', data)


class HomeTemplateView(TitleContextMixin, TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["suppliers"] = Supplier.objects.count()
        context["brands"] = Brand.objects.count()
        context["products"] = Product.objects.count()
        context["customers"] = Customer.objects.count()
        context["invoices"] = Invoice.objects.count()
        context["purchases"] = Purchase.objects.count()
        return context


# 1. LE QUITAMOS EL LOGINREQUIREDMIXIN A LA LISTA
class SupplierListView(TitleContextMixin, ListView): 
    model = Supplier 
    template_name = 'supplier/list.html' 
    context_object_name = 'suppliers'     
    paginate_by = 10   
    title1 = "Autor | TeacherCode"
    title2 = "Listado de Proveedores mixings"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '')
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(ruc__icontains=query))
        return queryset
    

# 2. LE QUITAMOS EL LOGINREQUIREDMIXIN AL CREAR
class SupplierCreateView(TitleContextMixin, CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "supplier/form.html"
    success_url = reverse_lazy("core:supplier_list")  
    title1 = '"Proveedores"'
    title2 = 'Crear Nuevo Proveedor VBC'
          
    def form_valid(self, form):
        # Si el formulario te da error de usuario anónimo, usamos el primer usuario de la BD o lo dejamos libre
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)


# 3. LE QUITAMOS EL LOGINREQUIREDMIXIN AL EDITAR
class SupplierUpdateView(TitleContextMixin, UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "supplier/form.html"
    success_url = reverse_lazy("core:supplier_list")  
    title1 = '"Proveedores"'
    title2 = 'Editar Proveedor'
   
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super().form_valid(form)


# 4. LE QUITAMOS EL LOGINREQUIREDMIXIN AL DETALLE
class SupplierDetailView(TitleContextMixin, DetailView):
    model = Supplier
    template_name = "supplier/detail.html"
    context_object_name = "supplier"  
    title1 = "Proveedores"
    title2 = "Datos del Proveedor"
    success_url = reverse_lazy("core:supplier_list")


# 5. LE QUITAMOS EL LOGINREQUIREDMIXIN AL ELIMINAR
class SupplierDeleteView(TitleContextMixin, DeleteView):
    model = Supplier
    template_name = "supplier/delete.html"
    success_url = reverse_lazy("core:supplier_list") 
    title1 = "Eliminar"
    title2 = 'Eliminar Proveedor VBC'

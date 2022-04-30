from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView, UpdateView
from .models import Proveedor, ComprasDet, ComprasEnc
from .forms import ProveedorForm, ComprasEncForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import datetime
from django.http import HttpResponse
from bases.views import SinPrivilegios
from inv.models import Producto

# Create your views here.
class ProveedorView(SinPrivilegios, ListView):
    permission_required = 'cmp.view_proveedor'
    model = Proveedor
    template_name = 'cmp/proveedor_list.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'PROVEEDOR'
        context['list_url'] = reverse_lazy('cmp:proveedor_new')
        return context

class ProveedorNew(SinPrivilegios, CreateView):
    permission_required = 'cmp.add_proveedor'
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url = reverse_lazy('cmp:proveedor_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVO PROVEEDOR'
        context['list_url'] = self.success_url
        context['action'] = reverse_lazy('cmp:proveedor_new')
        return context

class ProveedorEdit(SinPrivilegios, UpdateView):
    permission_required = 'cmp.change_proveedor'
    model = Proveedor
    template_name = 'cmp/proveedor_form.html'
    context_object_name = 'obj'
    form_class = ProveedorForm

    success_url = reverse_lazy('cmp:proveedor_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'EDITAR PROVEEDOR'
        context['list_url'] = self.success_url
        return context

@login_required(login_url='bases:login')
@permission_required('inv.delete_proveedor', login_url='bases:sin_privilegios')   
@method_decorator(csrf_exempt)
def proveedor_inactivar(request, id):
    proveedor = Proveedor.objects.filter(pk=id).first()
    template_name = 'cmp/proveedor_del.html'
    context = {}

    if not proveedor:
        return HttpResponse('Proveedor no existe'+ str(id))

    if request.method == 'GET':
        context = {
            'obj':proveedor,
            'title':'Inhabilitar el proveedor',
            'list_url':reverse_lazy('cmp:proveedor_list'),
        }

    if request.method == 'POST':
        proveedor.estado = False
        proveedor.save()
        context={
            'obj':'ok',
        }
        return HttpResponse('Proveedor Inactivado')
    
    return render(request, template_name, context)

class ComprasView(SinPrivilegios, ListView):
    model = ComprasEnc
    template_name = 'cmp/compras_list.html'
    context_object_name = 'obj'
    permission_required = 'cmp.view_comprasenc'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'COMPRAS'
        # context['list_url'] = reverse_lazy('cmp:compras_new')
        return context

@login_required(login_url='bases:login')
@permission_required('cmp.change_comprasenc', login_url='bases:sin_privilegios')
def compras(request, compra_id=None):
    template_name = 'cmp/compras.html'
    prod = Producto.objects.filter(estado=True)
    form_compras={}
    context={}

    if request.method=='GET':        
        enc = ComprasEnc.objects.filter(pk=compra_id).first()

        if enc:
            det = ComprasDet.objects.filter(compras=enc)
            fecha_compra = datetime.date.isoformat(enc.fecha_compra)
            fecha_factura = datetime.date.isoformat(enc.fecha_factura)
            e ={
                'fecha_compra':fecha_compra,
                'proveedor':enc.proveedor,
                'observacion':enc.observacion,
                'no_factura':enc.no_factura,
                'fecha_factura':fecha_factura,
                'sub_total':enc.sub_total,
                'descuento':enc.descuento,
                'total':enc.total,
            }
            form_compras = ComprasEncForm(e)
        else:
            form_compras=ComprasEncForm()
            det=None
        
        context={
            'productos':prod,
            'encabezado':enc,
            'detalle':det,
            'form_enc':form_compras,
        }
        return render(request, template_name, context)

        
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView, UpdateView, DeleteView
from .models import Proveedor, ComprasDet, ComprasEnc
from .forms import ProveedorForm, ComprasEncForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.db.models import Sum
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
            det = ComprasDet.objects.filter(compra=enc.id)
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
    
    if request.method=='POST':
        fecha_compra = request.POST.get('fecha_compra')
        observacion = request.POST.get('observacion')
        no_factura = request.POST.get('no_factura')
        fecha_factura = request.POST.get('fecha_factura')
        proveedor = request.POST.get('proveedor')
        sub_total = 0
        descuento = 0

        prov = Proveedor.objects.get(pk=proveedor)

        if not compra_id:
            enc = ComprasEnc(
                fecha_compra=fecha_compra,
                observacion=observacion,
                no_factura=no_factura,
                fecha_factura=fecha_factura,
                proveedor=prov,
                uc = request.user
            )
            if enc:
                enc.save()
                compra_id = enc.id
            else:
                return redirect('cmp:compras_list')
            
        else:
            enc = ComprasEnc.objects.filter(pk=compra_id).first()
            if enc:
                enc.fecha_compra = fecha_compra
                enc.observacion = observacion
                enc.no_factura = no_factura
                enc.fecha_factura = fecha_factura
                enc.um = request.user.id  
                enc.save()
            
        producto = request.POST.get('id_id_producto')
        cantidad = request.POST.get('id_cantidad_detalle')
        precio = request.POST.get('id_precio_detalle')
        descuento_detalle = request.POST.get('id_descuento_detalle')

        prod = Producto.objects.get(pk=producto)

        det = ComprasDet(
            compra = enc,
            producto = prod,
            cantidad =  cantidad,
            precio_prv = precio,
            descuento = descuento_detalle,
            costo = 0,
            uc = request.user,
        )
        if det:
            det.save()
            sub_total = ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('sub_total'))
            descuento = ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('descuento'))
            enc.sub_total = sub_total['sub_total__sum']
            enc.descuento = descuento['descuento__sum']
            enc.save()

        return redirect('cmp:compras_edit', compra_id=compra_id)

    return render(request, template_name, context)


class CompraDetDelete(SinPrivilegios, DeleteView):
    permission_required = 'cmp.delete_comprasdet'
    model = ComprasDet
    template_name = 'cmp/compras_det_del.html'
    context_object_name = 'obj'

    def get_success_url(self):
        compra_id = self.kwargs['compra_id']
        return reverse_lazy('cmp:compras_edit', kwargs={'compra_id':compra_id})
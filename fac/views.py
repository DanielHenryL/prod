from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.http import HttpResponse
from bases.views import SinPrivilegios, VistaBaseEdit, VistaBaseNew
from django.views.generic import ListView
from fac.forms import ClienteForm
from inv.models import Producto
from .models import Cliente, FacturaDet, FacturaEnc
from datetime import datetime
import json
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from inv import views as inv

# Create your views here.
class ClienteView(SinPrivilegios, ListView):
    permission_required = 'fac.view_cliente'
    model = Cliente
    template_name = 'fac/cliente_list.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'CLIENTE'
        context['list_url'] = reverse_lazy('fac:cliente_new')
        return context

class ClienteNew(VistaBaseNew):
    permission_required = 'fac.add_cliente'
    model = Cliente
    template_name = 'fac/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('fac:cliente_list')
    success_message= 'Cliente creado exitosamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVO CLIENTE'
        context['list_url'] = self.success_url
        context['action'] = reverse_lazy('fac:cliente_new')
        return context

class ClienteEdit(VistaBaseEdit):
    permission_required = 'fac.change_cliente'
    model = Cliente
    template_name = 'fac/cliente_form.html'
    form_class = ClienteForm
    success_url = reverse_lazy('fac:cliente_list')
    success_message= 'Cliente actualizada exitosamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'EDITAR CLIENTE'
        context['list_url'] = self.success_url
        return context

@login_required(login_url='bases:login')
@permission_required('fac.change_cliente', login_url='bases:sin_privilegios')
def clienteInactivar(request, id):
    cliente = Cliente.objects.filter(pk=id).first()
    if request.method == 'POST':
        if cliente:
            cliente.estado = not cliente.estado
            cliente.save()
            return HttpResponse('OK')
        return HttpResponse('FAIL')
    
    return HttpResponse('FAIL')



class FacturaView(SinPrivilegios, ListView):
    permission_required = 'fac.view_facturaenc'
    model = FacturaEnc
    template_name = 'fac/factura_list.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'FACTURA'
        # context['list_url'] = reverse_lazy('fac:factura_new')
        return context


@login_required(login_url='/login/')
@permission_required('fac.change_facturaenc',login_url='bases:sin_privilegios')
def facturas(request, id=None):
    template_name = 'fac/facturas.html'
     
    detalle ={}
    clientes = Cliente.objects.filter(estado=True)
    
    if request.method =='GET':
        enc = FacturaEnc.objects.filter(pk=id).first()
        if not enc:
            encabezado = {
                'id':0,
                'fecha':datetime.today(),
                'cliente':0,
                'sub_total':0.00,
                'descuento':0.00,
                'total':0.00,
            }  
            detalle=None
        else:
            encabezado = {
                'id':enc.id,
                'fecha':enc.fecha,
                'cliente':enc.cliente,
                'sub_total':enc.sub_total,
                'descuento':enc.descuento,
                'total':enc.total,
            } 
            detalle = FacturaDet.objects.filter(factura = enc) 

        contexto ={
            'enc':encabezado,
            'det':detalle,
            'clientes':clientes,
        }
    if request.method=='POST':
        cliente = request.POST.get('enc_cliente')
        fecha = request.POST.get('fecha')
        cli = Cliente.objects.get(pk=cliente)

        if not id:
            enc = FacturaEnc(
                cliente = cli,
                fecha = fecha
            )
            if enc:
                enc.save()
                id = enc.id
        else:
            enc = FacturaEnc.objects.filter(pk = id).first()
            if enc:
                enc.cliente = cli
                enc.save()
        if not id:
            messages.error(request, "No pude detectar el No. de la factura")
            return redirect("fac:factura_list")
        
        codigo = request.POST.get('codigo')
        cantidad = request.POST.get('cantidad')
        precio = request.POST.get('precio')
        s_total = request.POST.get('sub_total_detalle')
        descuento = request.POST.get('descuento_detalle')
        total = request.POST.get('total_detalle')

        prod = Producto.objects.get(codigo=codigo)
        det=FacturaDet(
            factura = enc,
            producto = prod,
            cantidad = cantidad,
            precio = precio,
            sub_total = s_total,
            descuento = descuento,
            total = total,
        )
        if det:
            det.save()
        return redirect('fac:factura_edit',id=id)

    return render(request,template_name, contexto)


class ProductoView(inv.ProductoView):
    template_name='fac/buscar_producto.html'


def borrar_factura_detalle(request, id):
    template_name = "fac/factura_borrar_detalle.html"

    det = FacturaDet.objects.get(pk=id)

    if request.method == 'GET':
        context ={
            "det":det
        }
    if request.method == 'POST':
        usr = request.POST.get('usuario')
        pas = request.POST.get('password')
        user = authenticate(username=usr, password=pas)
        
        if not user:
            return HttpResponse('Usuario o Contraseña incorrecta')

        if not user.is_active:
            return HttpResponse('Usuario Inactivo')
        
        if user.is_superuser or user.has_perm('fac.sup_caja_facturadet'):
            det.id = None
            det.cantidad = (-1 * det.cantidad)
            det.sub_total = (-1 * det.sub_total)
            det.descuento = (-1 * det.descuento)
            det.total = (-1 * det.total)
            det.save()
            return HttpResponse('ok')

        return HttpResponse('Usuario no autorizado')

    return render(request, template_name, context)
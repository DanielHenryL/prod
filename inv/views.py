from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Categoria, Marca, Producto, SubCategoria, UnidadMedida
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView
from .forms import CategoriaForm, MarcaForm, ProductoForm, SubCategoriaForm, UMForm
from bases.views import SinPrivilegios, VistaBaseEdit, VistaBaseNew

class CategoriaView(SinPrivilegios, ListView):
    permission_required = 'inv.view_categoria'
    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'CATEGORIA'
        context['list_url'] = reverse_lazy('inv:categoria_new')
        return context
    
class CategoriaNew(VistaBaseNew):
    permission_required = 'inv.add_categoria'
    model = Categoria
    template_name = 'inv/categoria_form.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    success_message= 'Categoria creada exitosamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVA CATEGORIA'
        context['list_url'] = self.success_url
        context['action'] = reverse_lazy('inv:categoria_new')
        return context

class CategoriaEdit(VistaBaseEdit):
    permission_required = 'inv.change_categoria'
    model = Categoria
    template_name = 'inv/categoria_form.html'
    form_class = CategoriaForm
    success_message= 'Categoria actualizada exitosamente'
    success_url = reverse_lazy('inv:categoria_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'EDITAR CATEGORIA'
        context['list_url'] = self.success_url
        return context

@login_required(login_url='bases:login')
@permission_required('inv.delete_categoria', login_url='bases:sin_privilegios')
@method_decorator(csrf_exempt)
def categoria_inactivar(request, id):
    categoria = Categoria.objects.filter(pk=id).first()
    template_name = 'inv/categoria_del.html'
    context = {}

    if not categoria:
        return HttpResponse('Categoria no existe '+ str(id))

    if request.method == 'GET':
        context = {
            'obj':categoria,
            'title':'Inhabilitar la categoria',
            'list_url':reverse_lazy('inv:categoria_list'),
            }

    if request.method == 'POST':
        categoria.estado = False
        categoria.save()
        context={
            'OK':'OK',
        }
        
        return HttpResponse('Categoria Inactivado')
    
    return render(request, template_name, context)
##Categoria Fin


##Subcategoria Inico
class SubCategoriaView(SinPrivilegios, ListView):
    permission_required = 'inv.view_subcategoria'
    model = SubCategoria
    template_name = 'inv/subcategoria_list.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SUBCATEGORIA'
        context['list_url'] = reverse_lazy('inv:subcategoria_new')
        return context

class SubCategoriaNew(VistaBaseNew):
    permission_required = 'inv.add_subcategoria'
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    success_message= 'Sub categoria creada exitosamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVA SUBCATEGORIA'
        context['list_url'] = self.success_url
        context['action'] = reverse_lazy('inv:subcategoria_new')
        return context


class SubCategoriaEdit(VistaBaseEdit):
    permission_required = 'inv.change_subcategoria'
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    success_message= 'Sub categoria editada exitosamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'EDITAR SUBCATEGORIA'
        context['list_url'] = self.success_url
        return context

@login_required(login_url='bases:login')
@permission_required('inv.delete_subcategoria', login_url='bases:sin_privilegios')
@method_decorator(csrf_exempt)
def subcategoria_inactivar(request, id):
    subcategoria = SubCategoria.objects.filter(pk=id).first()
    template_name = 'inv/subcategoria_del.html'
    context = {}

    if not subcategoria:
        return HttpResponse('Sub categoria no existe '+ str(id))

    if request.method == 'GET':
        context = {
            'obj':subcategoria,
            'title':'Inhabilitar la subcategoria',
            'list_url':reverse_lazy('inv:subcategoria_list'),
            }

    if request.method == 'POST':
        subcategoria.estado = False
        subcategoria.save()
        context={
            'obj':'ok',
        }
        return HttpResponse('Sub categoris Inactivado')
    
    return render(request, template_name, context)
##SubCategoria Fin


##Marca Inico
class MarcaView(SinPrivilegios, ListView):
    permission_required = 'inv.view_marca'
    model = Marca
    template_name = 'inv/marca_list.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'MARCA'
        context['list_url'] = reverse_lazy('inv:marca_new')
        return context

class MarcaNew(VistaBaseNew):
    permission_required = 'inv.add_marca'
    model = Marca
    template_name = 'inv/marca_form.html'
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')
    success_message= 'Marca creada exitosamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVA MARCA'
        context['list_url'] = self.success_url
        context['action'] = reverse_lazy('inv:marca_new')
        return context

class MarcaEdit(VistaBaseEdit):
    permission_required = 'inv.change_marca'
    model = Marca
    template_name = 'inv/marca_form.html'
    form_class = MarcaForm
    success_message= 'Marca actualizada exitosamente'
    success_url = reverse_lazy('inv:marca_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'EDITAR MARCA'
        context['list_url'] = self.success_url
        return context

@login_required(login_url='bases:login')
@permission_required('inv.delete_marca', login_url='bases:sin_privilegios')
@method_decorator(csrf_exempt)
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    template_name = 'inv/marca_del.html'
    context = {}

    if not marca:
        return HttpResponse('Marca no existe '+ str(id))


    if request.method == 'GET':
        context = {
            'obj':marca,
            'title':'Inhabilitar la marca',
            'list_url':reverse_lazy('inv:marca_list'),
            }

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        context={
            'obj':'ok',
        }
        return HttpResponse('Marca Inactivado')
    
    return render(request, template_name, context)
##Marca Fin


##Unidad de Medida Inicio
class UMView(SinPrivilegios, ListView):
    permission_required = 'inv.view_unidadmedida'
    model = UnidadMedida
    template_name = 'inv/um_list.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'UNIDAD DE MEDIADA'
        context['list_url'] = reverse_lazy('inv:um_new')
        return context

class UMNew(VistaBaseNew):
    permission_required = 'inv.add_unidadmedida'
    model = UnidadMedida
    template_name = 'inv/um_form.html'
    form_class = UMForm
    success_url = reverse_lazy('inv:um_list')
    success_message= 'Unidad de medida creada exitosamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVA UNIDAD DE MEDIDA'
        context['list_url'] = self.success_url
        context['action'] = reverse_lazy('inv:um_new')
        return context

class UMEdit(VistaBaseEdit):
    permission_required = 'inv.change_unidadmedida'
    model = UnidadMedida
    template_name = 'inv/um_form.html'
    form_class = UMForm
    success_url = reverse_lazy('inv:um_list')
    success_message= 'Unidad de medida actualizada exitosamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'EDITAR UNIDAD DE MEDIDA'
        context['list_url'] = self.success_url
        return context

@login_required(login_url='bases:login')
@permission_required('inv.delete_unidadmedida', login_url='bases:sin_privilegios')
@method_decorator(csrf_exempt)
def um_inactivar(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    template_name = 'inv/um_del.html'
    context = {}

    if not um:
        return HttpResponse('Unidad de medida no existe '+ str(id))

    if request.method == 'GET':
        context = {
            'obj':um,
            'title':'Inhabilitar La Unidad de Medida',
            'list_url':reverse_lazy('inv:um_list'),
        }

    if request.method == 'POST':
        um.estado = False
        um.save()
        context={
            'obj':'ok',
        }
        return HttpResponse('Unidad de medida Inactivado')
    
    return render(request, template_name, context)
##Unidad de medida Fin


##Producto Inico
class ProductoView(SinPrivilegios, ListView):
    permission_required = 'inv.view_producto'
    model = Producto
    template_name = 'inv/producto_list.html'
    context_object_name = 'obj'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'PRODUCTOS'
        context['list_url'] = reverse_lazy('inv:producto_new')
        return context

class ProductoNew(VistaBaseNew):
    permission_required = 'inv.add_producto'
    model = Producto
    template_name = 'inv/producto_form.html'
    form_class = ProductoForm
    success_url = reverse_lazy('inv:producto_list')
    success_message= 'Producto creada exitosamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVO PRODUCTO'
        context['list_url'] = self.success_url
        context['action'] = reverse_lazy('inv:producto_new')
        context['categorias'] = Categoria.objects.all()
        context['subcategorias'] = SubCategoria.objects.all()
        return context 

class ProductoEdit(VistaBaseEdit):
    permission_required = 'inv.change_producto'
    model = Producto
    template_name = 'inv/producto_form.html'
    form_class = ProductoForm
    success_url = reverse_lazy('inv:producto_list')
    success_message= 'Producto actualizado exitosamente'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context['title'] = 'EDITAR PRODUCTO'
        context['list_url'] = self.success_url
        context['categorias'] = Categoria.objects.all()
        context['subcategorias'] = SubCategoria.objects.all()
        context['obj'] = Producto.objects.filter(pk=pk).first()
        return context


@login_required(login_url='bases:login')
@permission_required('inv.delete_producto', login_url='bases:sin_privilegios')      
@method_decorator(csrf_exempt)
def producto_inactivar(request, id):
    producto = Producto.objects.filter(pk=id).first()
    template_name = 'inv/producto_del.html'
    context = {}

    if not producto:
        return HttpResponse('Producto no existe '+ str(id))

    if request.method == 'GET':
        context = {
            'obj':producto,
            'title':'Inhabilitar el producto',
            'list_url':reverse_lazy('inv:producto_list'),
        }

    if request.method == 'POST':
        producto.estado = False
        producto.save()
        context={
            'obj':'ok',
        }
        return HttpResponse('Producto Inactivado')
    
    return render(request, template_name, context)
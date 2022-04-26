from audioop import reverse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Categoria, Marca, Producto, SubCategoria, UnidadMedida
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CategoriaForm, MarcaForm, ProductoForm, SubCategoriaForm, UMForm

class CategoriaView(LoginRequiredMixin,ListView):
    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'CATEGORIAS'
        context['list_url'] = reverse_lazy('inv:categoria_new')
        return context
    
    
class CategoriaNew(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVA CATEGORIA'
        context['list_url'] = self.success_url
        context['action'] = reverse_lazy('inv:categoria_new')
        return context

class CategoriaEdit(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name = 'inv/categoria_form.html'
    context_object_name = 'obj'
    form_class = CategoriaForm
    

    success_url = reverse_lazy('inv:categoria_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'EDITAR CATEGORIA'
        context['list_url'] = self.success_url
        return context

class CategoriaDel(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'inv/categoria_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:categoria_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'La Categoria'
        context['list_url'] = self.success_url
        return context
##Categoria Fin


##Subcategoria Inico
class SubCategoriaView(LoginRequiredMixin,ListView):
    model = SubCategoria
    template_name = 'inv/subcategoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'SUBCATEGORIA'
        context['list_url'] = reverse_lazy('inv:subcategoria_new')
        return context

class SubCategoriaNew(LoginRequiredMixin, CreateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm
    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVA SUBCATEGORIA'
        context['list_url'] = self.success_url
        context['action'] = reverse_lazy('inv:subcategoria_new')
        return context


class SubCategoriaEdit(LoginRequiredMixin, UpdateView):
    model = SubCategoria
    template_name = 'inv/subcategoria_form.html'
    context_object_name = 'obj'
    form_class = SubCategoriaForm

    success_url = reverse_lazy('inv:subcategoria_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'EDITAR SUBCATEGORIA'
        context['list_url'] = self.success_url
        return context


class SubCategoriaDel(LoginRequiredMixin, DeleteView):
    model = SubCategoria
    template_name = 'inv/subcategoria_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:subcategoria_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'La Sub Categoria'
        context['list_url'] = self.success_url
        return context
##SubCategoria Fin


##Marca Inico
class MarcaView(LoginRequiredMixin,ListView):
    model = Marca
    template_name = 'inv/marca_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'MARCA'
        context['list_url'] = reverse_lazy('inv:marca_new')
        return context

class MarcaNew(LoginRequiredMixin, CreateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm
    success_url = reverse_lazy('inv:marca_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVA MARCA'
        context['list_url'] = self.success_url
        context['action'] = reverse_lazy('inv:marca_new')
        return context

class MarcaEdit(LoginRequiredMixin, UpdateView):
    model = Marca
    template_name = 'inv/marca_form.html'
    context_object_name = 'obj'
    form_class = MarcaForm

    success_url = reverse_lazy('inv:marca_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'EDITAR MARCA'
        context['list_url'] = self.success_url
        return context

def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    template_name = 'inv/marca_del.html'
    context = {}

    if not marca:
        return redirect('inv:marca_list')

    if request.method == 'GET':
        context = {
            'obj':marca,
            'title':'LA MARCA',
            'list_url':reverse_lazy('inv:marca_list'),
            }

    if request.method == 'POST':
        marca.estado = False
        marca.save()
        return redirect('inv:marca_list')
    
    return render(request, template_name, context)
##Marca Fin


##Unidad de Medida Inicio
class UMView(LoginRequiredMixin,ListView):
    model = UnidadMedida
    template_name = 'inv/um_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Unidid de medida'
        context['list_url'] = reverse_lazy('inv:um_new')
        return context

class UMNew(LoginRequiredMixin, CreateView):
    model = UnidadMedida
    template_name = 'inv/um_form.html'
    context_object_name = 'obj'
    form_class = UMForm
    success_url = reverse_lazy('inv:um_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVA UNIDAD DE MEDIDA'
        context['list_url'] = self.success_url
        context['action'] = reverse_lazy('inv:um_new')
        return context

class UMEdit(LoginRequiredMixin, UpdateView):
    model = UnidadMedida
    template_name = 'inv/um_form.html'
    context_object_name = 'obj'
    form_class = UMForm

    success_url = reverse_lazy('inv:um_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'EDITAR UNIDAD DE MEDIDA'
        context['list_url'] = self.success_url
        return context

def um_inactivar(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    template_name = 'inv/um_del.html'
    context = {}

    if not um:
        return redirect('inv:um_list')

    if request.method == 'GET':
        context = {
            'obj':um,
            'title':'La Unidad de Medida',
            'list_url':reverse_lazy('inv:um_list'),
        }

    if request.method == 'POST':
        um.estado = False
        um.save()
        return redirect('inv:um_list')
    
    return render(request, template_name, context)
##Unidad de medida Fin


##Producto Inico
class ProductoView(LoginRequiredMixin,ListView):
    model = Producto
    template_name = 'inv/producto_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Producto'
        context['list_url'] = reverse_lazy('inv:producto_new')
        return context

class ProductoNew(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = 'obj'
    form_class = ProductoForm
    success_url = reverse_lazy('inv:producto_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVO PRODUCTO'
        context['list_url'] = self.success_url
        context['action'] = reverse_lazy('inv:producto_new')
        return context 

class ProductoEdit(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = 'inv/producto_form.html'
    context_object_name = 'obj'
    form_class = ProductoForm

    success_url = reverse_lazy('inv:producto_list')
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'EDITAR PRODUCTO'
        context['list_url'] = self.success_url
        return context

def producto_inactivar(request, id):
    um = Producto.objects.filter(pk=id).first()
    template_name = 'inv/producto_del.html'
    context = {}

    if not um:
        return redirect('inv:producto_list')

    if request.method == 'GET':
        context = {
            'obj':um,
            'title':'El producto',
            'list_url':reverse_lazy('inv:producto_list'),
        }

    if request.method == 'POST':
        um.estado = False
        um.save()
        return redirect('inv:producto_list')
    
    return render(request, template_name, context)
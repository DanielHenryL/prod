from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Categoria, SubCategoria
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CategoriaForm, SubCategoriaForm

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
        return context

class CategoriaDel(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'inv/categoria_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('inv:categoria_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'La Categoria'
        context['list_url'] = reverse_lazy('inv:categoria_list')
        return context




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
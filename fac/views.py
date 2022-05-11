from django.shortcuts import render
from django.urls import reverse_lazy
from bases.views import SinPrivilegios
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from fac.forms import ClienteForm
from .models import Cliente

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

class ClienteNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = 'fac.add_cliente'
    model = Cliente
    template_name = 'fac/cliente_form.html'
    context_object_name = 'obj'
    form_class = ClienteForm
    success_url = reverse_lazy('fac:cliente_list')
    login_url = 'bases:login'
    success_message= 'Cliente creado exitosamente'
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NUEVO CLIENTE'
        context['list_url'] = self.success_url
        context['action'] = reverse_lazy('fac:cliente_new')
        return context

class ClienteEdit(SuccessMessageMixin, SinPrivilegios, UpdateView):
    permission_required = 'fac.change_cliente'
    model = Cliente
    template_name = 'fac/cliente_form.html'
    context_object_name = 'obj'
    form_class = ClienteForm

    success_url = reverse_lazy('fac:cliente_list')
    login_url = 'bases:login'
    success_message= 'Cliente actualizada exitosamente'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'EDITAR CLIENTE'
        context['list_url'] = self.success_url
        return context
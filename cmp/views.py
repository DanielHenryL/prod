from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView, UpdateView
from .models import Proveedor
from .forms import ProveedorForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Create your views here.
class ProveedorView(LoginRequiredMixin, ListView):
    model = Proveedor
    template_name = 'cmp/proveedor_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'PROVEEDOR'
        context['list_url'] = reverse_lazy('cmp:proveedor_new')
        return context

class ProveedorNew(LoginRequiredMixin, CreateView):
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

class ProveedorEdit(LoginRequiredMixin, UpdateView):
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
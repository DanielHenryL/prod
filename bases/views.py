from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.models import AnonymousUser

class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'bases:login'
    raise_exception = False
    redirect_field_name = 'redirecto_to'

    def handle_no_permission(self):
        if not self.request.user == AnonymousUser():
            self.login_url = 'bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))

class Home(LoginRequiredMixin,TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'

class HomeSinPrivilegios(LoginRequiredMixin ,TemplateView):
    login_url = 'bases:login'
    template_name = 'bases/sin_privilegios.html'

class VistaBaseNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    context_object_name = 'obj'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

    def form_invalid(self,form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response
        

class VistaBaseEdit(SuccessMessageMixin, SinPrivilegios, UpdateView):
    context_object_name = 'obj'
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
    def form_invalid(self,form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response
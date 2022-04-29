from django.shortcuts import render
from django.http import HttpResponseRedirect
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
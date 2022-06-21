from django.urls import path
from .views import Home, HomeSinPrivilegios
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('favicon.ico/', LoginView.as_view(template_name='bases/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sin_privilegios/', HomeSinPrivilegios.as_view(), name='sin_privilegios'),
]
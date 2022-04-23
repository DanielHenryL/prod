from django.urls import path
from .views import Home
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='bases/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
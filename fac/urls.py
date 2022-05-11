from django.urls import path
from .views import *

urlpatterns = [
    path('cliente/list/',ClienteView.as_view(), name='cliente_list'),
    path('cliente/new/',ClienteNew.as_view(), name='cliente_new'),
    path('cliente/edit/<int:pk>/',ClienteEdit.as_view(), name='cliente_edit'),
]
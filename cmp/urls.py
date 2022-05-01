from django.urls import path
from .views import *

urlpatterns = [
    path('proveedor/list/', ProveedorView.as_view(), name='proveedor_list'),
    path('proveedor/new/', ProveedorNew.as_view(), name='proveedor_new'),
    path('proveedor/edit/<int:pk>/', ProveedorEdit.as_view(), name='proveedor_edit'),
    path('proveedor/inactivar/<int:id>/', proveedor_inactivar, name='proveedor_inactivar'),

    path('compras/list/', ComprasView.as_view(), name='compras_list'),
    path('compras/new/', compras, name='compras_new'),
    path('compras/edit/<int:compra_id>/', compras, name='compras_edit'),
]
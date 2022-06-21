from django.urls import path
from .views import *
from .reportes import imprimir_factura_recibo, imprimir_factura_list
urlpatterns = [
    path('cliente/list/',ClienteView.as_view(), name='cliente_list'),
    path('cliente/new/',ClienteNew.as_view(), name='cliente_new'),
    path('cliente/edit/<int:pk>/',ClienteEdit.as_view(), name='cliente_edit'),
    path('cliente/estado/<int:id>',clienteInactivar, name='cliente_inactivar'),

    path('facturas/list/', FacturaView.as_view(), name='factura_list'),
    path('facturas/new/', facturas, name='factura_new'),
    path('facturas/edit/<int:id>/', facturas, name='factura_edit'),
    path('facturas/buscar-producto/', ProductoView.as_view(), name='factura_producto'),

    path('facturas/borrar-detalle/<int:id>/', borrar_factura_detalle, name='factura_borrar_detalle'),
    
    path('facturas/imprimir/<int:id>/', imprimir_factura_recibo, name='factura_imprimir_one'),
    path('facturas/list/imprimir-todas/<str:f1>/<str:f2>/', imprimir_factura_list, name='factura_imprimir_all'),
]
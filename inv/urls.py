from django.urls import path
from .views import *

urlpatterns = [
    path('categoria/list/', CategoriaView.as_view(), name='categoria_list'),
    path('categoria/new/', CategoriaNew.as_view(), name='categoria_new'),
    path('categoria/edit/<int:pk>/', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categoria/inactivar/<int:id>/', categoria_inactivar, name='categoria_inactivar'),

    path('subcategoria/list/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategoria/new/', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategoria/edit/<int:pk>/', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategoria/inactivar/<int:id>/', subcategoria_inactivar, name='subcategoria_inactivar'),

    path('marca/list/', MarcaView.as_view(), name='marca_list'),
    path('marca/new/', MarcaNew.as_view(), name='marca_new'),
    path('marca/edit/<int:pk>/', MarcaEdit.as_view(), name='marca_edit'),
    path('marca/inactivar/<int:id>/', marca_inactivar, name='marca_inactivar'),

    path('unidadmediada/list/', UMView.as_view(), name='um_list'),
    path('unidadmediada/new/', UMNew.as_view(), name='um_new'),
    path('unidadmediada/edit/<int:pk>/', UMEdit.as_view(), name='um_edit'),
    path('unidadmediada/inactivar/<int:id>/', um_inactivar, name='um_inactivar'),
    
    path('productos/list/', ProductoView.as_view(), name='producto_list'),
    path('productos/new/', ProductoNew.as_view(), name='producto_new'),
    path('productos/edit/<int:pk>/', ProductoEdit.as_view(), name='producto_edit'),
    path('productos/inactivar/<int:id>/', producto_inactivar, name='producto_inactivar'),

]
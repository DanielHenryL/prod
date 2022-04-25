from django.urls import path
from .views import *

urlpatterns = [
    path('categoria/list/', CategoriaView.as_view(), name='categoria_list'),
    path('categoria/new/', CategoriaNew.as_view(), name='categoria_new'),
    path('categoria/edit/<int:pk>/', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categoria/del/<int:pk>/', CategoriaDel.as_view(), name='categoria_del'),

    path('subcategoria/list/', SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategoria/new/', SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategoria/edit/<int:pk>/', SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategoria/del/<int:pk>/', SubCategoriaDel.as_view(), name='subcategoria_del'),

    path('marca/list/', MarcaView.as_view(), name='marca_list'),
    path('marca/new/', MarcaNew.as_view(), name='marca_new'),
    path('marca/edit/<int:pk>/', MarcaEdit.as_view(), name='marca_edit'),
    path('marca/inactivar/<int:id>/', marca_inactivar, name='marca_inactivar'),

]
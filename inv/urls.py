from django.urls import path
from .views import CategoriaDel, CategoriaEdit, CategoriaView, CategoriaNew

urlpatterns = [
    path('categoria/list/', CategoriaView.as_view(), name='categoria_list'),
    path('categoria/new/', CategoriaNew.as_view(), name='categoria_new'),
    path('categoria/edit/<int:pk>/', CategoriaEdit.as_view(), name='categoria_edit'),
    path('categoria/del/<int:pk>/', CategoriaDel.as_view(), name='categoria_del'),
]
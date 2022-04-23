from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la Categoría',
        unique=True,
    )
    def __str__(self):
        return self.descripcion
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la SubCategoría',
    )
    def __str__(self):
        return ' {} : {}'.format(self.categoria.descripcion, self.descripcion )

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = 'Subs Categorias'
        # Hacer que la descrippcion se valida para una misma sub categoria y no para todas
        # Evitar categoria : Desarrollo y subcategoria: Web, Desarrollo y web nuevamente,
        # pero si deberia haber esto categoria: Desarrollo y subcategoria :Web , Aplicacion y Web 
        unique_together = ('categoria','descripcion')


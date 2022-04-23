from django.db import models
from django.contrib.auth.models import User

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)                      #estado
    fc = models.DateTimeField(auto_now_add=True)                    #fecha_creacion
    fm = models.DateTimeField(auto_now=True)                        #fecha_modificacion
    uc = models.ForeignKey(User, on_delete=models.CASCADE)          #Usuario que crea
    um = models.IntegerField(blank=True, null=True)                 #Usuario que modifica

    class Meta:
        abstract = True

from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey

class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)                      #estado
    fc = models.DateTimeField(auto_now_add=True)                    #fecha_creacion
    fm = models.DateTimeField(auto_now=True)                        #fecha_modificacion
    uc = models.ForeignKey(User, on_delete=models.CASCADE)          #Usuario que crea
    um = models.IntegerField(blank=True, null=True)                 #Usuario que modifica

    class Meta:
        abstract = True


class ClaseModelo2(models.Model):
    estado = models.BooleanField(default=True)                      #estado
    fc = models.DateTimeField(auto_now_add=True)                    #fecha_creacion
    fm = models.DateTimeField(auto_now=True)                        #fecha_modificacion
    # uc = models.ForeignKey(User, on_delete=models.CASCADE)          Usuario que crea
    # um = models.IntegerField(blank=True, null=True)                 Usuario que modifica
    uc = UserForeignKey(auto_user_add=True, related_name='+')
    um = UserForeignKey(auto_user=True, related_name='+')
    class Meta:
        abstract = True

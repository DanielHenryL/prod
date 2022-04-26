from django.forms import EmailField, ModelForm, TextInput
from .models import Proveedor

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['descripcion','direccion','contacto','telefono','email', 'estado']
        widgets = {
            'descripcion': TextInput(attrs={                
                'placeholder':'Ejm. asociacion de detergente',
                'autofocus':'on',
            }),
            'direccion': TextInput(attrs={
                'placeholder':'Ejm. avenida 2 de mayo',
            }),
            'contacto': TextInput(attrs={
                'placeholder':'Ejm. Luis',
            }),
            'telefono': TextInput(attrs={
                'placeholder':'Ejm. 5555555',
            }),
            'email': TextInput(attrs={
                'placeholder':'Ejm. ejemplo@bazar.com',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'autocomplete':'off',
            })
from django.forms import DateInput, ModelChoiceField, ModelForm, TextInput
from .models import Proveedor, ComprasEnc
from django import forms
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

    def clean(self):
        try:
            sc = Proveedor.objects.get(descripcion=self.cleaned_data['descripcion'].upper()) 
            if not self.instance.pk:
                raise forms.ValidationError('Registro Ya Existe')
            elif self.instance.pk!=sc.pk:
                raise forms.ValidationError('Cambio no permitido')
        except Proveedor.DoesNotExist:
            pass
        return self.cleaned_data
            

class ComprasEncForm(ModelForm):
    fecha_compra = DateInput()
    fecha_factura = DateInput()
    # proveedor = ModelChoiceField(
    #     queryset=Proveedor.objects.filter(estado=True).order_by('id')
    # )
    class Meta:
        model = ComprasEnc
        fields = ['proveedor','fecha_compra','observacion','no_factura',
                'fecha_factura','sub_total','descuento','total']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['fecha_compra'].widget.attrs['readonly'] = True
        self.fields['fecha_factura'].widget.attrs['readonly'] = True
        self.fields['sub_total'].widget.attrs['readonly'] = True
        self.fields['descuento'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True

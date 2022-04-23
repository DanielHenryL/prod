from django.forms import ModelForm, TextInput
from .models import Categoria

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion','estado']
        labels = {
            'descripcion':'Descripcion de la Categoria',
            'estado':'Estado',
        }
        widgets={
            'descripcion': TextInput(attrs={
                'autocomplete':'off'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                
            })
    

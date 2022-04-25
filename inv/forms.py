from msilib.schema import CheckBox, ComboBox
from django.forms import CheckboxInput, ModelChoiceField, ModelForm, TextInput
from .models import Categoria, Marca, SubCategoria, UnidadMedida

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
                'autocomplete':'off',
                'autofocus':'on',
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',   
            })


class SubCategoriaForm(ModelForm):
    categoria = ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True).order_by('id')
    )
    class Meta:
        model = SubCategoria
        fields = ['categoria','descripcion','estado']
        labels = {
            'descripcion':'Sub Categoria',
            'estado':'Estado'
        }
        widgets={
            'descripcion': TextInput(attrs={
                'placeholder':'Añade una descripcion',
                'autofocus':'on',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',  
            })
        self.fields['categoria'].empty_label = 'Seleccione categoria'


class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ['descripcion','estado']
        labels = {
            'descripcion':'Descripcion de la Categoria',
            'estado':'Estado',
        }
        widgets={
            'descripcion': TextInput(attrs={
                'autocomplete':'off',
                'autofocus':'on',
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',   
            }) 


class UMForm(ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ['descripcion','estado']
        labels = {
            'descripcion':'Descripcion de la Unidad de Medida',
            'estado':'Estado',
        }
        widgets={
            'descripcion': TextInput(attrs={
                'autocomplete':'off',
                'autofocus':'on',
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',   
            }) 

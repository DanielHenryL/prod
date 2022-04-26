from django.forms import ModelChoiceField, ModelForm, TextInput
from .models import Categoria, Marca, Producto, SubCategoria, UnidadMedida

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
                'placeholder':'Ejm. Productos de limpieza',
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
                'placeholder':'Ejm. Detergente',
                'autofocus':'on',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',  
            })
        self.fields['categoria'].empty_label = 'Selec. categoria'


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
                'placeholder':'Ejm. Sapolio',
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
                'placeholder':'Ejm. Unidad, Docena,...',
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


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo','codigo_barra','descripcion','estado','precio','existencia','ultima_compra', 'marca', 'subcategoria','unidad_medida']
        
        widgets={
            'codigo': TextInput(attrs={
                'placeholder':'ejm. 1AG48S0A',
            }),
            'codigo_barra': TextInput(attrs={
                'placeholder':'ejm. 1AG4-D8D8',
            }),
            'descripcion': TextInput(attrs={
                'placeholder':'ejm. 100g, 1kg',
            }),
            'precio': TextInput(attrs={
                'placeholder':'ejm. 1, 5.5',
            }),
            'existencia': TextInput(attrs={
                'placeholder':'',
            }),
            'ultima_compra': TextInput(attrs={
                'placeholder':'',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'autocomplete':'off',
            })
        self.fields['ultima_compra'].widget.attrs['readonly']= True
        self.fields['existencia'].widget.attrs['readonly']= True
        self.fields['marca'].empty_label = 'Seleccionar una marca'
        self.fields['subcategoria'].empty_label = 'Seleccione subcategoria'
        self.fields['unidad_medida'].empty_label = 'Selec. Unidad de medida'

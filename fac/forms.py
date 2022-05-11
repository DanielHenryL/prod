from django.forms import ModelForm, TextInput
from .models import Cliente

class ClienteForm(ModelForm):
    class Meta:
        model=Cliente
        fields=['nombres','apellidos','tipo','celular','estado']
        widgets = {
            'nombres': TextInput(attrs={                
                'placeholder':'Ejm. Carlos, Tania',
            }),
            'apellidos': TextInput(attrs={
                'placeholder':'Ejm. Suclupe, Montalvan',
            }),
            'celular': TextInput(attrs={
                'placeholder':'Ejm. 954863217',
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control',
                'autocomplete':'off',
            })

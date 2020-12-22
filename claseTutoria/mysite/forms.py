from django import forms

class Persona(forms.Form):
    
    nombre = forms.CharField(max_length=20,required = True, widget=forms.TextInput(attrs={'placeholder': 'Inserte Nombre'}))
    apellido = forms.CharField(max_length=20,required = True, widget=forms.TextInput(attrs={'placeholder': 'Inserte Apellido'}))
    
    class Meta:
        field = '__all__'
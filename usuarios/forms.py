from django import forms
from .models import Genero, Usuarios
from django.forms import ModelForm

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = ["genero",]
        labels = {'genero': 'Género',}

class UsuariosForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ["rut","nombre","apellido_paterno","apellido_materno","fecha_nacimiento","id_genero","telefono","email","direccion"]
        labels = {'rut': 'Rut', 'nombre': 'Nombre', 'apellido_paterno': 'Apellido Paterno', 'apellido_materno': 'Apellido Materno', 'fecha_nacimiento': 'Fecha de Nacimiento', 'id_genero': 'Género', 'telefono': 'Teléfono', 'email': 'Email', 'direccion': 'Dirección',}
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }
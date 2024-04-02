from django import forms

class Curso_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    especialidad = forms.CharField(max_length=50)

class AlumnoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

class EntregableFormulario(forms.Form):
    titulo = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea)
    fecha_de_entrega = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    entregado = forms.BooleanField(required=False)

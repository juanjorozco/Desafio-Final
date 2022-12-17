from django import forms

class PersonalForm(forms.Form):
    nombres=forms.CharField()
    apellidos=forms.CharField()
    edad=forms.IntegerField()
    nacionalidad=forms.CharField()
    correo=forms.CharField()

class EstudiosForm(forms.Form):
    carrera=forms.CharField()
    universidad=forms.CharField()
    idiomas=forms.CharField()
    correo=forms.CharField()

class ExperienciaForm(forms.Form):
    trabajos_anteriores=forms.CharField()
    años_experiencia=forms.IntegerField()
    correo=forms.CharField()

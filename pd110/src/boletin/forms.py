from django import forms
from .models import Registrado

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre", "email"]
    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, provedor = email.split("@")
        dominio, extension = provedor.split(".")
        if not extension == "edu":
            raise forms.ValidationError("utiliza un emial .edu")
        return email
    """def clean_nombre(self):
        #validaciones
        nombre = self.cleaned_data.get("nombre")
        primer_letra = nombre[0]
        if primer_letra != primer_letra.upper():
            raise forms.ValidationError("la primer letra debe ser una mayuscula")
        return nombre"""



class ContactForm(forms.Form):
    nombre = forms.CharField(required= False)
    email = forms.EmailField()
    mensaje = forms.CharField(widget= forms.Textarea)
    """class Meta:
        model = Contacto
        fields = ["nombre", "email", "mensaje"]"""
   
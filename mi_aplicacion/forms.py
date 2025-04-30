from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(max_length=100) #input
    correo = forms.EmailField() #input
    mensaje = forms.CharField(widget=forms.Textarea) #textarea
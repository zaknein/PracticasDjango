from django import forms

class ComentForm(forms.Form):
    name    = forms.CharField(label ='Escribe tu nombre')
    url     = forms.URLField(label='Tu sitio web', required=False)
    comment = forms.CharField()

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Nombre', 
        max_length=50,
        widget=forms.TextInput(attrs={'class':'input'}))
    email = forms.EmailField(label='Email', max_length=50)
    message = forms.CharField(label='Mensaje')
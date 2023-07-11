from django.forms import ModelForm
from .models import empleado
class EmpleadoForm(ModelForm):
    class Meta:
        model = empleado
        # fields = ['name', 'last_name', 'email']
        # Si quisieramos agregar todos los campos se realiza de la siguiente manera
        fields = '__all__'
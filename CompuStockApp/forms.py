from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile, Producto

# Formulario para registro de usuarios
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Ingresa un correo electrónico válido.")
    phone_number = forms.CharField(max_length=15, required=False, help_text="Número de teléfono (opcional).")
    
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

# Formulario para login de usuarios
class LoginForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password']

# Formulario para gestión de productos (ya lo tienes, lo incluyo aquí para referencia)
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'especificaciones', 'precio', 'imagen']

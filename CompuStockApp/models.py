from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    # Correo electrónico
    email = models.EmailField(unique=True)
    
    # Número de teléfono
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # Asegura que `REQUIRED_FIELDS` esté presente
    REQUIRED_FIELDS = ['email', 'phone_number']  # Agrega los campos que deseas como obligatorios

    def __str__(self):
        return self.username


#Modelo Productos
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    especificaciones = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    
    def __str__(self):
        return self.nombre
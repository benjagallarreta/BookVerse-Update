from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    foto_perfil = models.ImageField(upload_to='static/Usuario/default-user.png')
    username = models.CharField(max_length=50, unique=True)
    nombre_completo = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, blank=False)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    nacionalidad =  models.CharField(max_length=50, blank=False)
    provincia = models.CharField(max_length=50, blank=False)
    codigo_postal = models.CharField(max_length=5, blank=False)
    ciudad = models.CharField(max_length=50, blank=False)
    direccion = models.CharField(max_length=50, blank=False) 

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def _str_(self):
        return self.username
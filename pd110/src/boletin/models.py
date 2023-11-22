from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registrado(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __unicode__(self):
        return self.email
    
    def __str__(self) -> str:
        return self.email
   
   # lo siguiente sería si quisiera hacer una tabla para guardar los mensajes 
"""class Contacto(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    mensaje = models.TextField()
    
    def __unicode__(self):
    
    def __str__(self) -> str:
        return self.mensaje"""
from django.db import models

# Create your models here.
class Persona(models.Model):
    total_compras = models.DecimalField(max_digits=8, decimal_places=2)



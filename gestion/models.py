from django.db import models

class Supercomputadora(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    numero_cores = models.IntegerField()
    ram_tb = models.FloatField()
    almacenamiento_tb = models.FloatField()
    teraflops = models.FloatField()
    sistema_operativo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

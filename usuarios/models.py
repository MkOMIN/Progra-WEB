from django.db import models

# Create your models here.

class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True)
    genero = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.genero)


class Usuarios(models.Model):
    rut              = models.CharField(primary_key=True, max_length=20)
    nombre           = models.CharField(max_length=20, null=True)
    apellido_paterno = models.CharField(max_length=20, null=True)
    apellido_materno = models.CharField(max_length=20, null=True)
    fecha_nacimiento = models.DateField(blank=False, null=True) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero', null=True)  
    telefono         = models.CharField(max_length=45, null=True)
    email            = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)  

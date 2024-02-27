from django.db import models

class Usuarios(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres_apellidos = models.CharField(max_length=90, null=False)
    Perfil = models.CharField(max_length=50, null=False)  
    PERFIL_CHOICES = [
        ('administrativo', 'Administrativo'),
        ('aprendiz', 'Aprendiz'),
        ('estudiante', 'Estudiante'),
        ('docente', 'Docente'),
    ]
    Perfil = models.CharField(max_length=50, choices=PERFIL_CHOICES) 
    FACULTAD_CHOICES = [
        ('Psicología', 'Psicología'),
        ('Matemáticas', 'Matemáticas'),
        ('Física', 'Física'),
    ]
    Facultad = models.CharField(max_length=90, choices=FACULTAD_CHOICES)
    Telefono = models.BigIntegerField(null=False)

    Correo = models.CharField(max_length=90, null=False)    
    Nro_portatil = models.IntegerField(null=False)
    Fecha = models.DateTimeField(auto_now_add=True, null=True)
    Observaciones = models.CharField(max_length=100, null=False)
    

from django.db import models

# Create your models here.
class Project(models.Model):
    name= models.CharField(max_length=200)
    
class Form(models.Model): # formulario
    age= models.IntegerField() #edadd
    gender= models.TextField(max_length=100) #genero
    position= models.TextField(max_length=100) #posicion
    dominance= models.TextField(max_length=50) # dominancia
    project = models.ForeignKey(Project, on_delete=models.CASCADE)



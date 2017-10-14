from django.db import models   		#from es para las libreria, import para importar solo una parte, líneas para añadir algo de otros archivos
from django.utils import timezone

#Comienza la clase, Post es el nombre de la clase
# (models.Model) significa que Post es un modelo de Django 
class Post(models.Model):
	author = models.ForeignKey('auth.User')	    #este es un vínculo con otro modelo
	title = models.CharField(max_length=200) 	#así es como defines un texto con un número limitado de caracteres
	text = models.TextField()					#esto es para textos largos sin un límite
	created_date = models.DateTimeField(default=timezone.now) #esto es fecha y hora
	published_date = models.DateTimeField(blank=True, null=True)
	# def significa que se trata de una función o método
	# publish es el nombre del método
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	#metodo que retorna algo 
	def __str__(self):
		return self.title

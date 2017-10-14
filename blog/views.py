from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})
#En la función render ya tenemos el parámetro request
#y el archivo 'blog/post_list.html' como plantilla
#{} es un campo en el que podemos agregar algunas 
#cosas para que la plantilla las use.	

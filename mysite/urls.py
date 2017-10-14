from django.conf.urls import include, url
from django.contrib import admin

urlpatterns =[
	#Esto significa que para cada URL que empieza con admin/ 
	#Django encontrará su correspondiente view
	url(r'^admin/', include(admin.site.urls)),
	url(r'', include('blog.urls')),
]

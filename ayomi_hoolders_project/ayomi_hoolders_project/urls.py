from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^connexion/', include('connexion.urls', namespace='connexion')),
	url(r'^$', 'connexion.views.index', name='index'),
]

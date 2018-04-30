# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^profile[/]?$', views.profile, name='profile'),
	url(r'^logout_view[/]?$', views.logout_view, name='logout_view'),
	url(r'^profile/modify_infos', views.modify_infos, name='modify_infos'),
]

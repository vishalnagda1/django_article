from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^show', views.show, name='show'),
    url(r'^create', views.create, name='create'),
    url(r'^update', views.update, name='update'),
    url(r'^destroy', views.destroy, name='destroy'),
    url(r'^unarchive', views.unarchive, name='unarchive'),
    url(r'^archive', views.archive, name='archive'),
]
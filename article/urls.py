from django.conf.urls import url

from article import views


urlpatterns = [
    url(r'^$', views.articles, name='articles'),
    url(r'^(?P<pk>[0-9]+)/$', views.article_ops),
]
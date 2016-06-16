from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^favourite/article/(?P<article_id>\d+)/add/', views.add_favourite, name='add_favourite'),
    url(r'^favourites/', views.favourites_list, name='favourites'),
]

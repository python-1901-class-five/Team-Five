from django.conf.urls import url
from . import views
from .feeds import ArticlePost
app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rss/$', ArticlePost(), name='rss'),
    url(r'^single/(\d+)/$', views.single, name='single'),
    url(r'^choosetime/(\d+)/(\d+)/$', views.choosetime, name='choosetime'),
    url(r'^choosecate/(\d+)/$', views.choosecate, name='choosecate'),
    url(r'^choosetag/(\d+)/$', views.choosetag, name='choosetag'),
    url(r'^comments/$', views.comments, name='comments')
]
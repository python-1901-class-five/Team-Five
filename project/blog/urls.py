from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^(\d+)/$', views.index, name='index'),
    url(r'^single/(\d+)/$', views.single, name='single'),
    url(r'^classify/(\d+)/$', views.classify, name='classify')
]
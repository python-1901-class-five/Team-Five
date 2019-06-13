from django.conf.urls import url
from . import views

app_name = 'test2'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('list1/$', views.list1, name='list1'),
    url('detail/(\d+)/$', views.detail, name='detail'),
]

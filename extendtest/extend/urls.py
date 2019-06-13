from django.conf.urls import url
from . import views

app_name = 'extend'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('csrf1/$', views.csrf1, name='csrf1'),
    url('csrf2/$', views.csrf2, name='csrf2'),
    url('login/$', views.login, name='login'),
]
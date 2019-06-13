from django.conf.urls import url
from . import views


app_name = 'curd'
urlpatterns = [
    url(r'area/$', views.area,name='area'),
]
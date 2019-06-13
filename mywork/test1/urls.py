from django.conf.urls import url
from . import views
app_name = 'test1'

urlpatterns = [
    url('^$', views.index, name='index'),
]
from django.conf.urls import url
from . import views

app_name = 'vote'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'detail/(\d+)/$', views.detail, name='detail'),
    url(r'result/$', views.result, name='result'),
    url(r'addquestion/$', views.addquestion, name='addquestion'),
    url(r'addquestionhandler/$', views.addquestionhandler, name='addquestionhandler'),
    url(r'addchoice/(\d+)/$', views.addchoice, name='addchoice'),
    url(r'addchoicehandler/$', views.addchoicehandler, name='addchoicehandler'),
    url(r'modifyquestion/(\d+)/$', views.modifyquestion, name='modifyquestion'),
    url(r'modifyquestionhandler/$', views.modifyquestionhandler, name='modifyquestionhandler'),
    url(r'modifychoice/(\d+)/$', views.modifychoice, name='modifychoice'),
    url(r'modifychoicehandler/$', views.modifychoicehandler, name='modifychoicehandler'),
    url(r'deletequestion/(\d+)/$', views.deletequestion, name='deletequestion'),
    url(r'deletechoice/(\d+)/$', views.deletechoice, name='deletechoice'),
]

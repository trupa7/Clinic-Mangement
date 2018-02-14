<<<<<<< HEAD
from django.conf.urls import url
from laboratory import views

app_name='lab'
urlpatterns = [
    url(r'^details/$',views.getAllDetails,name='view-patient-tests'),
    url(r'^details/(?P<id>\d+)/$', views.getTestData, name='test_detail'),
    url(r'^test/(?P<id>\d+)/$', views.Test, name='test'),
    url(r'^update/$', views.updateTestData, name='test_update'),
=======
from django.conf.urls import url
from laboratory import views

app_name='lab'
urlpatterns = [
    url(r'^details/$',views.getAllDetails,name='view-patient-tests'),
    url(r'^details/(?P<id>\d+)/$', views.getTestData, name='test_detail'),
    url(r'^update/$', views.updateTestData, name='test_update'),
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
]
<<<<<<< HEAD
from django.conf.urls import url
from pharmacist import views

app_name='pharmacy'

urlpatterns = [
    url(r'^details/$',views.getAllDetails,name='view-patient-prescriptions'),
    url(r'^details/(?P<id>\d+)/$', views.getPrescriptionData, name='pres_detail'),
    url(r'^delete/(?P<id>\d+)/$', views.deletefromTable, name='del_detail'),
=======
from django.conf.urls import url
from pharmacist import views

app_name='pharmacy'

urlpatterns = [
    url(r'^details/$',views.getAllDetails,name='view-patient-prescriptions'),
    url(r'^details/(?P<id>\d+)/$', views.getPrescriptionData, name='pres_detail'),
    url(r'^delete/(?P<id>\d+)/$', views.deletefromTable, name='del_detail'),
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
]
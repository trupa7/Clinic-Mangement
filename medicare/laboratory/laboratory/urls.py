from django.conf.urls import url
from .views import LabDetails,TestDetails

urlpatterns = [
    url(r'^lab/$',LabDetails.as_view(),name='view-patient-tests'),
    url(r'^lab/(?P<test_id>[^/]+)/$',TestDetails.as_view(),name='test')
]
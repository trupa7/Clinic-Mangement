from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Laboratory
from django.utils import  timezone
# Create your views here.

class LabDetails(ListView):
    model=Laboratory
    template_name = "laboratory/Welcome Screen.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class TestDetails(DetailView):
    model=Laboratory
    template_name = "laboratory/test_details.html"

    def getTestData(request,test_id):

        data = Laboratory.objects.filter(test_id__contains=test_id)
        render(request,'laboratory/test_details.html',{'data':data})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['test_details'] = Laboratory.objects.filter(test_id__contains=kwargs)
    #     return context

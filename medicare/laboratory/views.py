from django.shortcuts import render,redirect
from .models import Laboratory
from .forms import TestFormSelect


# Create your views here.

def getAllDetails(request):
    data = Laboratory.objects.all()
    return render(request,'laboratory/la_desk.html',{'data':data,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
   
def getTestData(request,id):
    labObj = Laboratory.objects.filter(patient_id_id=id)
    return render(request,'laboratory/test_details.html',{'data':labObj,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})

def Test(request,id):
    labObj = Laboratory.objects.filter(id=id)
    return render(request,'laboratory/test.html',{'data':labObj,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})   

def updateTestData(request):
    id=request.POST.get('t_id',None)
    result_status=request.POST.get('result_status',None)
    test_details=request.POST.get('test_details',None)  
    if id:  
        
        Laboratory.objects.filter(id=id).update(result_status=result_status,test_details=test_details)
        return redirect('lab:view-patient-tests')
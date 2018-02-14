<<<<<<< HEAD
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
=======
from django.shortcuts import render,redirect
from .models import Laboratory
from .forms import TestFormSelect


# Create your views here.

def getAllDetails(request):
    data = Laboratory.objects.all()
    return render(request,'laboratory/WelcomeScreen.html',{'data':data})

def getTestData(request,id):
    labObj = Laboratory.objects.filter(patient_id_id=id)
    return render(request,'laboratory/test_details.html',{'data':labObj})

def updateTestData(request):
    val = request.POST.get('res_stat', None)
    print("VAl-------------",val)
    if(request.method == "POST"):
        print("insidePPOST")
        form = TestFormSelect()
        if form['result_status'] != None:
            print("inside")
            data = form.save(commit=False)
            data.result_status = val;
            return redirect('lab:test_update', {'data': data})
        else:
            return render(request, 'laboratory/WelcomeScreen.html',{'data': Laboratory.objects.all()})

    #
    # print("inside")
    # data = Laboratory.objects.filter(result_status__contains=val)
    #

>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408

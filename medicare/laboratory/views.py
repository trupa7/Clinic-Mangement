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


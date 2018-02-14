<<<<<<< HEAD
from django.shortcuts import render
from .models import Pharmacist,Prescription
# Create your views here.
def getAllDetails(request):
    data=Pharmacist.objects.all()
    return render(request,'pharmacist/ph_desk.html',{'data':data,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
   
def getPrescriptionData(request,id):
    prescDet = Prescription.objects.filter(pk=id)
    return render(request,'pharmacist/view_details.html',{'data':prescDet,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
   
# delete data when prescription is given
def deletefromTable(request,id):
    print("inside")
    Prescription.objects.filter(prescribedBy=id).delete()
    Pharmacist.objects.filter(id=id).delete()
    return render(request, 'pharmacy:view-patient-prescriptions', {})

=======
from django.shortcuts import render
from .models import Pharmacist,Prescription
# Create your views here.
def getAllDetails(request):
    data=Pharmacist.objects.all()
    return render(request,'pharmacist/view.html',{'data':data})

def getPrescriptionData(request,id):
    prescDet = Prescription.objects.filter(pk=id)
    return render(request,'pharmacist/view_details.html',{'data':prescDet})

# delete data when prescription is given
def deletefromTable(request,id):
    print("inside")
    Prescription.objects.filter(prescribedBy=id).delete()
    Pharmacist.objects.filter(id=id).delete()
    return render(request, 'pharmacist/view.html', {'data': Pharmacist.objects.all()})

>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
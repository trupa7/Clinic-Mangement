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


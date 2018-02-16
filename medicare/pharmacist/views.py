from django.shortcuts import render, redirect
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
 
    #Prescription.objects.filter(prescribedBy=id).delete()
    Pharmacist.objects.filter(prescription_id_id=id).delete()
    return redirect('pharmacy:view-patient-prescriptions')


from django.shortcuts import render, redirect

# Create your views here.

from .models import Nurses
from records.models import Admit
from .forms import NewFollowups
from django.template.context_processors import request

def nurses(request):
    admit_list=Admit.objects.all()
    return render(request, 'nurses/nu_desk.html',{"admit_list":admit_list,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
    
def new_history(request,id):
    
    patient_name=Admit.objects.filter(patient_id=id)
    nurses_list=Nurses.objects.filter(patient_id=id)
    return render(request, 'nurses/newhistory.html', {'patient_name':patient_name,'nurses_list': nurses_list,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})

def auth_followup(request):
    patient_id=request.POST.get('paitent_id',None)
    details=request.POST.get('details',None)  
    patient_name=Admit.objects.filter(patient_id=patient_id)
  
    if patient_id:  
        Nurses(patient_id_id=patient_id,details=details).save()
        return redirect('nurses:frontdesk')
    


def new_followup(request,id):
    patient_name=Admit.objects.filter(patient_id=id)
    return render(request, 'nurses/add_followups.html', {'patient_name':patient_name,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})

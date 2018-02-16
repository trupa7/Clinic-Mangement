from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import render,get_object_or_404
from django.template.context_processors import request, csrf
from django.http import Http404,HttpResponseRedirect
from employees.models import Employee,Doctor
from django.contrib.sessions.models import Session
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect



# Create your views here.
def index(request):
    try:
        return render(request, 'login/login.html', {"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
    except:
        request.session['for_id']=""
        request.session['userid']=""
        request.session['usertype']=""
        request.session['userspec']=""
        return render(request, 'login/login.html', {"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})

def about(request):
    try:
        return render(request, 'login/about.html', {"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
    except:
        request.session['for_id']=""
        request.session['userid']=""
        request.session['usertype']=""
        request.session['userspec']=""
        return render(request, 'login/about.html', {"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
  
    

def login(request):
    return render(request, 'login/login.html', {})

def logout(request):
    request.session['for_id']=""
    request.session['userid']=""
    request.session['usertype']=""
    request.session['userspec']=""
    return render(request, 'login/login.html', {"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})

def auth_view(request):
    
    username = request.POST['username']
    password = request.POST['pwd']
    #type_label = request.POST['sel1']
    
    try:
        user = Employee.objects.get(username=username,password=password)
        
        
        #str(AllUser.getSpec(user))
        if user is not None:
            try:
                doctor_user=Doctor.objects.get(username=username)
                request.session['for_id']=str(doctor_user.id)
            except:
                request.session['for_id']=""
            request.session['userid']=str(user)
            request.session['usertype']=Employee.getType(user)
            request.session['userspec']=Employee.getSpec(user)
            if 'DO' in request.session['usertype']:
                return redirect('doctors:appointments')
            elif 'RE' in request.session['usertype']:
                return redirect('records:frontdesk')
            elif 'NU' in request.session['usertype']:
                return redirect('nurses:frontdesk')
            elif 'LA' in request.session['usertype']:
                return redirect('lab:view-patient-tests')
            elif 'PH' in request.session['usertype']:
                return redirect('pharmacy:view-patient-prescriptions')
        #return HttpResponseRedirect('')
    except Employee.DoesNotExist:
       
        return render(request, 'login/login.html', {"error":'Invalid Input'})
    
    
  

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import render,get_object_or_404
from django.template.context_processors import request, csrf
from django.http import Http404,HttpResponseRedirect
<<<<<<< HEAD
from employees.models import Employee
from django.contrib.sessions.models import Session
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect


=======
from .models import AllUser
from django.contrib.sessions.models import Session
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408



global userid,usertype,userspec
userid,usertype,userspec="","",""
# Create your views here.
def index(request):
<<<<<<< HEAD
    try:
        return render(request, 'login/index.html', {"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
    except:
        request.session['userid']=""
        request.session['usertype']=""
        request.session['userspec']=""
        return render(request, 'login/index.html', {"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
    
=======

    return render(request, 'login/index.html', {"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408

def login(request):
    return render(request, 'login/login.html', {})

def logout(request):
    request.session['userid']=""
    request.session['usertype']=""
    request.session['userspec']=""
    return render(request, 'login/index.html', {"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})

def auth_view(request):
    
    username = request.POST['username']
    password = request.POST['pwd']
    type_label = request.POST['sel1']
<<<<<<< HEAD
    
    try:
        user = Employee.objects.get(username=username,password=password,type_label=type_label)
        #str(AllUser.getSpec(user))
        if user is not None:
            request.session['userid']=str(user)
            request.session['usertype']=Employee.getType(user)
            request.session['userspec']=Employee.getSpec(user)
            return redirect('login:index')
        #return HttpResponseRedirect('')
    except Employee.DoesNotExist:
=======
    try:
        user = AllUser.objects.get(username=username,password=password,type_label=type_label)
        #str(AllUser.getSpec(user))
        if user is not None:
            request.session['userid']=str(user)
            request.session['usertype']=AllUser.getType(user)
            request.session['userspec']=AllUser.getSpec(user)
            return redirect('login:index')
        #return HttpResponseRedirect('')
    except AllUser.DoesNotExist:
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
        a=[]
        a.append('INAVLID ID OR PASSWORD')
        return render(request, 'login/login.html', {"error":'Invalid Input'})
    
    
  

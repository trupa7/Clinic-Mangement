from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
# Create your views here.
from records.froms import NewPatientForm, NewAppointmentForm, NewAdmitForm
from records.models import Appointment,Admit,Patient
from nurses.models import Nurses
from doctors.models import CompleteAppointment,History
from pharmacist.models import Prescription 
from laboratory.models import Laboratory 

#
def front_desk(request):
    Appoinment_list=Appointment.objects.all()
   
    return render(request, "records/re_desk.html",{"Appoinment_list":Appoinment_list,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
    #return render(request, "front_desk.html",{"Appoinment_list":Appoinment_list,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
def view_patient(request):
    patient_list=Patient.objects.all()
    return render(request, "records/view_patient.html",{"patient_list":patient_list,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
    
def detail_patient(request,id):
    patient_list=Patient.objects.all()
    prescDet = Prescription.objects.filter(patient_id_id=id)
    labObj = Laboratory.objects.filter(patient_id_id=id)
    try:
        # isolate the patient and all appointments
      
        name = Patient.objects.get(id=id)
        # get patient name for display

        appointment = CompleteAppointment.objects.filter(patient_id=id)
        history = list(History.objects.all())
        # append the history for patient to val
        val = []
        for h in history:
            for a in appointment:
                if h.appointment_id == a.id:
                    val.append(h)
                    break
    
    except:
        raise Http404('no employee found')
    
    return render(request, "records/detail_patient.html",{'lab_data':labObj,'data':prescDet,'name':name, 'history':val,"patient_list":patient_list,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})
   

# add patient
def new_patient(request):
    if request.method == 'POST':
        form = NewPatientForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('records:frontdesk')
    else:
        form = NewPatientForm()
    return render(request, 'records/add_patient.html', {'record': form,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})


# add appointment
def new_appointment(request):
    if request.method == 'POST':
      
        form = NewAppointmentForm(request.POST)
        if form.is_valid():
           
            record = form.save(commit=False)
            record.save()
            return redirect('records:frontdesk')
        else:
            form = NewAppointmentForm()
            return render(request, 'records/add_appoinment.html', {'record': form,"error":'Slot alreay booked',"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})

    else:
        form = NewAppointmentForm()

    return render(request, 'records/add_appoinment.html', {'record': form,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})





# cancel appointment
def cancel_appointment(request):
    appointments = Appointment.objects.all()

    patient = request.GET.get('patient', None)

    for appointment in appointments:
        if str(appointment) == patient:
            # delete from Appointment by id
            Appointment.objects.filter(id=appointment.id).delete()
            return redirect('records:frontdesk')
            break

    return render(request, 'records/cancel_appointment.html', {'appointments': appointments,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})

# add admit
def new_admit(request):
    if request.method == 'POST':
        form = NewAdmitForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('records:frontdesk')
        else:
            a=[]
            a.append('INAVLID ID OR PASSWORD')
            return render(request, 'records/add_admit.html', {"error":'Already Admited','record': form,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})


    else:
        form = NewAdmitForm()

    return render(request, 'records/add_admit.html', {'record': form,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})


# cancel admit    
def cancel_admit(request):
    admits = Admit.objects.all()

    admit_id = request.GET.get('patient', None)
 
    for admit in admits:
        
        if str(admit) == admit_id:
            # delete from Appointment by id
            Admit.objects.filter(id=admit.id).delete()
            Nurses.objects.filter(patient_id_id=admit.patient_id_id).delete()
            return redirect('records:frontdesk')
            break

    return render(request, 'records/cancel_admit.html', {'admits': admits,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})

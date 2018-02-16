from django.shortcuts import render
from datetime import date
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from records.models import Appointment, Patient 
from .models import CompleteAppointment,History
from laboratory.forms import AddTestSelect
from laboratory.models import Laboratory
from pharmacist.forms import NewPharmacist,NewPrescription
from pharmacist.models import Pharmacist

# cancel appointment
def cancel_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    app = CompleteAppointment(patient=appointment.patient,
                              appointment_date=appointment.appointment_date,
                              appointment_time=appointment.appointment_time,
                              visit_reason=appointment.visit_reason,
                              doctor=appointment.doctor)
    app.save()
    record = History(appointment=app, prescription='n', prescribed='none', visit_record='Appointment Canceled')
    record.save()
    Appointment.objects.filter(id=appointment.id).delete()

    return appointments(request)



def appointments(request):
    appointments = list(Appointment.objects.all())
  
    history = list(History.objects.all())
    todays_appointments = []
    future_appointments = []
#     for a in appointments:
#         for h in history:
#             if a.id == h.appointment_id:
#                 appointments.remove(a)
    todays_date = date.today()
   
    for a in appointments:
        if str(a.appointment_date) == str(todays_date):
            todays_appointments.append(a)
        else:
            future_appointments.append(a)



    return render(request, 'doctors/do_desk.html', {'todays_appointments': todays_appointments,
                                                                 'future_appointments': future_appointments,
                                                                 'todays_date':todays_date,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})

def display_history(request, appointment_id):
    try:
        # isolate the patient and all appointments
        appointments = get_object_or_404(Appointment, pk=appointment_id)
        name = Patient.objects.get(id=appointments.patient_id)
        # get patient name for display

        appointment = CompleteAppointment.objects.filter(patient_id=appointments.patient_id)
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

    return render(request, 'doctors/display_history.html', {'name':name, 'history':val,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})


def update_history(request, appointment_id):
  
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    # get patient name for display
    prescription = request.POST.get('precription', None)
    prescribed = request.POST.get('medication', '')
    notes = request.POST.get('notes', None)
    prescript = 'n'
    if prescription == 'on':
        prescript = 'y'
    if notes:
        
        # create history record
        app = CompleteAppointment(patient=appointment.patient,
                                  appointment_date=appointment.appointment_date,
                                  appointment_time=appointment.appointment_time,
                                  visit_reason=appointment.visit_reason,
                                  doctor=appointment.doctor)
        app.save()
        record = History(appointment=app, prescription=prescript, prescribed=prescribed, visit_record=notes)
        record.save()
        # create complete appointment record
        # delete from current appointment
        Appointment.objects.filter(id=appointment.id).delete()
        return redirect('doctors:appointments')


    name = Patient.objects.get(id=appointment.patient_id)
    return render(request, 'doctors/custom_form.html',{"name":name,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})


def new_lab(request,id):
    if request.method == 'POST':
        form = AddTestSelect(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('doctors:appointments')
    else:
        form = AddTestSelect()
    return render(request, 'doctors/add_lab.html', {'patient_id':id,'record': form,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})

def new_prescription(request):
    
    if request.method == 'POST':
        prescription = request.POST.get('prescribedBy', None)
        form = NewPrescription(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
         
            new_id=int(str(record))
           
            record1=Pharmacist(name_id=prescription,prescription_id_id=new_id)
            record1.save()
            return redirect('doctors:appointments')
    else:
        form = NewPrescription()
    return render(request, 'doctors/add_prescription.html', {'record': form,"userid":request.session['userid'],"usertype":request.session['usertype'],"userspec":request.session['userspec']})



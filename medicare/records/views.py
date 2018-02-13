from datetime import date

from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from records.froms import NewPatientForm, NewAppointmentForm, NewHistoryForm
from records.models import Appointment, History, Patient


#
def front_desk(request):
    return render(request, "front_desk.html")


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

    return render(request, 'records/add_to_db.html', {'record': form})


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

    return render(request, 'records/add_to_db.html', {'record': form})




# cancel appointment
def cancel_appointment(request):
    appointments = list(Appointment.objects.all())
    history = list(History.objects.all())
    for a in appointments:
        for h in history:
            if a.id == h.appointment_id:
                appointments.remove(a)

    patient = request.GET.get('patient', None)

    for appointment in appointments:
        if str(appointment) == patient:
            # delete from Appointment by id
            Appointment.objects.filter(id=appointment.id).delete()
            break

    return render(request, 'records/cancel_app.html', {'appointments': appointments})


def appointments(request):
    appointments = list(Appointment.objects.all())
    history = list(History.objects.all())
    todays_appointments = []
    future_appointments = []
    for a in appointments:
        for h in history:
            if a.id == h.appointment_id:
                appointments.remove(a)
    todays_date = date.today()
    for a in appointments:
        if str(a.appointment_date) == str(todays_date):
            todays_appointments.append(a)
        else:
            future_appointments.append(a)



    return render(request, 'records/current_appointments.html', {'todays_appointments': todays_appointments,
                                                                 'future_appointments': future_appointments,
                                                                 'todays_date':todays_date})

# update history
# TODO:: new history should have appointment filled in automatically
# TODO:: need custom method to add to table
def new_history(request, appointment_id=None):
    if request.method == 'POST':
        form = NewHistoryForm(request.POST)
        print(form)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('records:frontdesk')
    else:
        form = NewHistoryForm()

    return render(request, 'records/add_to_db.html', {'record': form})


def display_history(request, appointment_id):
    try:
        # isolate the patient and all appointments
        appointments = get_object_or_404(Appointment, pk=appointment_id)
        # get patient name for display
        name = Patient.objects.get(id=appointments.patient_id)

        appointment = Appointment.objects.filter(patient_id=appointments.patient_id)
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

    return render(request, "records/display_history.html", {'name':name, 'history':val})

from django.shortcuts import render, redirect

# Create your views here.
from records.froms import NewPatientForm, NewAppointmentForm, NewHistoryForm
from records.models import Appointment


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


# update history
# TODO:: delete appintment ifno after history is updated
def new_history(request):
    if request.method == 'POST':
        form = NewHistoryForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.save()
            return redirect('records:frontdesk')
    else:
        form = NewHistoryForm()

    return render(request, 'records/add_to_db.html', {'record': form})


# cancel appointment
def cancel_appointment(request):
    appointments = Appointment.objects.all()

    patient = request.GET.get('patient', None)

    for appointment in appointments:
        if str(appointment) == patient:
            # delete from Appointment by id
            Appointment.objects.filter(id=appointment.id).delete()
            break

    return render(request, 'records/cancel_app.html', {'appointments': appointments})
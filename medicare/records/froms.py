from django import forms

<<<<<<< HEAD
from records.models import Patient, Appointment, History,Admit
=======
from records.models import Patient, Appointment, History

>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408

# add a patient
class NewPatientForm(forms.ModelForm):
    middle_name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=False)
    evening_phone = forms.CharField(max_length=10, required=False)

    class Meta:
        model = Patient
        fields = ('last_name', 'first_name', 'middle_name', 'sex', 'address', 'city',
                  'state', 'zip', 'email', 'day_phone', 'evening_phone',
                  'insurance')

<<<<<<< HEAD
=======

>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
# make an appointment for patient
class NewAppointmentForm(forms.ModelForm):
    visit_reason = forms.CharField(max_length=150, required=False)

    class Meta:
        model = Appointment
        fields = ('patient', 'appointment_date', 'appointment_time', 'visit_reason', 'doctor')

<<<<<<< HEAD
=======

>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408
# update patient history based on appointment
class NewHistoryForm(forms.ModelForm):
    prescribed = forms.CharField(max_length=150, required=False)

    class Meta:
        model = History
        fields = ('appointment', 'prescription', 'prescribed', 'visit_record')
<<<<<<< HEAD

class NewAdmitForm(forms.ModelForm):

    class Meta:
        model = Admit
        fields = ('patient_id', 'Room_id')
=======
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408

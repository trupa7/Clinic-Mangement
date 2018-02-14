from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from .models import Patient, History, Appointment,Rooms,Admit
from records.models import Admit
=======
from .models import Patient, History, Appointment
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408


class PatientAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'middle_name','sex', 'insurance',
                    'address', 'city', 'state', 'zip', 'email',
                    'day_phone', 'evening_phone']
    list_filter = ['last_name', 'first_name', 'sex', 'insurance']



class HistoryAdmin(admin.ModelAdmin):
    list_display = ['appointment', 'record_date']
    list_filter = ['appointment', 'record_date']
    # prepopulated_fields = {'appointment': ('record_date',)}


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'appointment_date', 'appointment_time', 'visit_reason']
    list_filter = ['appointment_date', 'patient']
    # prepopulated_fields = {'patient_id': ('appointment_time', 'visit_reason')}


admin.site.register(Patient, PatientAdmin)
<<<<<<< HEAD
admin.site.register(History, HistoryAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Rooms)
admin.site.register(Admit)

# admin.site.register(Record)
=======
#admin.site.register(History, HistoryAdmin)
admin.site.register(Appointment, AppointmentAdmin)
>>>>>>> bf50983dee3fcf5b70e95b4bb430d7795e532408

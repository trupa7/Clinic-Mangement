from django.contrib import admin

# Register your models here.
from .models import Patient, History, Appointment


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
admin.site.register(History, HistoryAdmin)
admin.site.register(Appointment, AppointmentAdmin)
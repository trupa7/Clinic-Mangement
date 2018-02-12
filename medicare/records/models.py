from datetime import date, datetime, time, timedelta
from django.db import models


# Create your models here.


class Patient(models.Model):
    SEX = (
        ('m', 'male'),
        ('f', 'female')
    )

    STATES = (
        ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'),
        ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'District of Columbia'), ('DE', 'Delaware'),('FL', 'Florida'),
        ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'),
        ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'),
        ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'),
        ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'),('ND', 'North Dakota'),
        ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'),
        ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'),
        ('WY', 'Wyoming')
    )

    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=SEX)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATES)
    zip = models.CharField(max_length=5)
    email = models.EmailField()
    day_phone = models.CharField(max_length=10)
    evening_phone = models.CharField(max_length=10)

    insurance = models.CharField(max_length=250)
    doctor = models.CharField(max_length=50) # models.ForeignKey('Doctor', on_delet=models.CASCADE)

    def __str__(self):
        return  '{}, {}'.format(self.last_name, self.first_name)


class History(models.Model):
    PRESCRIPTION = (
        ('y', 'yes'),
        ('n', 'no')
    )
    appointment = models.ForeignKey('Appointment', on_delete=models.CASCADE, )
    prescription = models.CharField(max_length=1, choices=PRESCRIPTION,)
    prescribed = models.CharField(max_length=150)
    record_date = models.DateTimeField(auto_now=datetime)
    visit_record = models.TextField()

    def __str__(self):
        return str(self.appointment)


class Appointment(models.Model):
    DATE = [] # set days to select
    TIME = [] # set time to select
    for i in range(120):
        today_d = date.today()
        d = today_d + timedelta(days=i)
        DATE.append((d,str(d)))
    for i in range(19):
        dt = datetime.combine(date.today(), time(8, 0)) + timedelta(minutes=(30*i))
        TIME.append((dt.time(),str(dt.time())))

    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    appointment_date = models.DateField(choices=DATE)
    appointment_time = models.TimeField(choices=TIME)
    visit_reason = models.CharField(max_length=150)

    class Meta:
        # cant make multiple appointments for same date and time
        unique_together = (('appointment_date', 'appointment_time'),)
        ordering = ('appointment_date',)
        verbose_name = 'appointment'
        verbose_name_plural = 'appointments'

    def __str__(self):
        return '{} {}, {}'.format(str(self.patient), self.appointment_time, self.appointment_date)

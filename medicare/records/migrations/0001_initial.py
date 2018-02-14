# Generated by Django 2.0.2 on 2018-02-13 16:43

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateField(choices=[(datetime.date(2018, 2, 13), '2018-02-13'), (datetime.date(2018, 2, 14), '2018-02-14'), (datetime.date(2018, 2, 15), '2018-02-15'), (datetime.date(2018, 2, 16), '2018-02-16'), (datetime.date(2018, 2, 17), '2018-02-17'), (datetime.date(2018, 2, 18), '2018-02-18'), (datetime.date(2018, 2, 19), '2018-02-19'), (datetime.date(2018, 2, 20), '2018-02-20'), (datetime.date(2018, 2, 21), '2018-02-21'), (datetime.date(2018, 2, 22), '2018-02-22'), (datetime.date(2018, 2, 23), '2018-02-23'), (datetime.date(2018, 2, 24), '2018-02-24'), (datetime.date(2018, 2, 25), '2018-02-25'), (datetime.date(2018, 2, 26), '2018-02-26'), (datetime.date(2018, 2, 27), '2018-02-27'), (datetime.date(2018, 2, 28), '2018-02-28'), (datetime.date(2018, 3, 1), '2018-03-01'), (datetime.date(2018, 3, 2), '2018-03-02'), (datetime.date(2018, 3, 3), '2018-03-03'), (datetime.date(2018, 3, 4), '2018-03-04'), (datetime.date(2018, 3, 5), '2018-03-05'), (datetime.date(2018, 3, 6), '2018-03-06'), (datetime.date(2018, 3, 7), '2018-03-07'), (datetime.date(2018, 3, 8), '2018-03-08'), (datetime.date(2018, 3, 9), '2018-03-09'), (datetime.date(2018, 3, 10), '2018-03-10'), (datetime.date(2018, 3, 11), '2018-03-11'), (datetime.date(2018, 3, 12), '2018-03-12'), (datetime.date(2018, 3, 13), '2018-03-13'), (datetime.date(2018, 3, 14), '2018-03-14'), (datetime.date(2018, 3, 15), '2018-03-15'), (datetime.date(2018, 3, 16), '2018-03-16'), (datetime.date(2018, 3, 17), '2018-03-17'), (datetime.date(2018, 3, 18), '2018-03-18'), (datetime.date(2018, 3, 19), '2018-03-19'), (datetime.date(2018, 3, 20), '2018-03-20'), (datetime.date(2018, 3, 21), '2018-03-21'), (datetime.date(2018, 3, 22), '2018-03-22'), (datetime.date(2018, 3, 23), '2018-03-23'), (datetime.date(2018, 3, 24), '2018-03-24'), (datetime.date(2018, 3, 25), '2018-03-25'), (datetime.date(2018, 3, 26), '2018-03-26'), (datetime.date(2018, 3, 27), '2018-03-27'), (datetime.date(2018, 3, 28), '2018-03-28'), (datetime.date(2018, 3, 29), '2018-03-29'), (datetime.date(2018, 3, 30), '2018-03-30'), (datetime.date(2018, 3, 31), '2018-03-31'), (datetime.date(2018, 4, 1), '2018-04-01'), (datetime.date(2018, 4, 2), '2018-04-02'), (datetime.date(2018, 4, 3), '2018-04-03'), (datetime.date(2018, 4, 4), '2018-04-04'), (datetime.date(2018, 4, 5), '2018-04-05'), (datetime.date(2018, 4, 6), '2018-04-06'), (datetime.date(2018, 4, 7), '2018-04-07'), (datetime.date(2018, 4, 8), '2018-04-08'), (datetime.date(2018, 4, 9), '2018-04-09'), (datetime.date(2018, 4, 10), '2018-04-10'), (datetime.date(2018, 4, 11), '2018-04-11'), (datetime.date(2018, 4, 12), '2018-04-12'), (datetime.date(2018, 4, 13), '2018-04-13'), (datetime.date(2018, 4, 14), '2018-04-14'), (datetime.date(2018, 4, 15), '2018-04-15'), (datetime.date(2018, 4, 16), '2018-04-16'), (datetime.date(2018, 4, 17), '2018-04-17'), (datetime.date(2018, 4, 18), '2018-04-18'), (datetime.date(2018, 4, 19), '2018-04-19'), (datetime.date(2018, 4, 20), '2018-04-20'), (datetime.date(2018, 4, 21), '2018-04-21'), (datetime.date(2018, 4, 22), '2018-04-22'), (datetime.date(2018, 4, 23), '2018-04-23'), (datetime.date(2018, 4, 24), '2018-04-24'), (datetime.date(2018, 4, 25), '2018-04-25'), (datetime.date(2018, 4, 26), '2018-04-26'), (datetime.date(2018, 4, 27), '2018-04-27'), (datetime.date(2018, 4, 28), '2018-04-28'), (datetime.date(2018, 4, 29), '2018-04-29'), (datetime.date(2018, 4, 30), '2018-04-30'), (datetime.date(2018, 5, 1), '2018-05-01'), (datetime.date(2018, 5, 2), '2018-05-02'), (datetime.date(2018, 5, 3), '2018-05-03'), (datetime.date(2018, 5, 4), '2018-05-04'), (datetime.date(2018, 5, 5), '2018-05-05'), (datetime.date(2018, 5, 6), '2018-05-06'), (datetime.date(2018, 5, 7), '2018-05-07'), (datetime.date(2018, 5, 8), '2018-05-08'), (datetime.date(2018, 5, 9), '2018-05-09'), (datetime.date(2018, 5, 10), '2018-05-10'), (datetime.date(2018, 5, 11), '2018-05-11'), (datetime.date(2018, 5, 12), '2018-05-12'), (datetime.date(2018, 5, 13), '2018-05-13'), (datetime.date(2018, 5, 14), '2018-05-14'), (datetime.date(2018, 5, 15), '2018-05-15'), (datetime.date(2018, 5, 16), '2018-05-16'), (datetime.date(2018, 5, 17), '2018-05-17'), (datetime.date(2018, 5, 18), '2018-05-18'), (datetime.date(2018, 5, 19), '2018-05-19'), (datetime.date(2018, 5, 20), '2018-05-20'), (datetime.date(2018, 5, 21), '2018-05-21'), (datetime.date(2018, 5, 22), '2018-05-22'), (datetime.date(2018, 5, 23), '2018-05-23'), (datetime.date(2018, 5, 24), '2018-05-24'), (datetime.date(2018, 5, 25), '2018-05-25'), (datetime.date(2018, 5, 26), '2018-05-26'), (datetime.date(2018, 5, 27), '2018-05-27'), (datetime.date(2018, 5, 28), '2018-05-28'), (datetime.date(2018, 5, 29), '2018-05-29'), (datetime.date(2018, 5, 30), '2018-05-30'), (datetime.date(2018, 5, 31), '2018-05-31'), (datetime.date(2018, 6, 1), '2018-06-01'), (datetime.date(2018, 6, 2), '2018-06-02'), (datetime.date(2018, 6, 3), '2018-06-03'), (datetime.date(2018, 6, 4), '2018-06-04'), (datetime.date(2018, 6, 5), '2018-06-05'), (datetime.date(2018, 6, 6), '2018-06-06'), (datetime.date(2018, 6, 7), '2018-06-07'), (datetime.date(2018, 6, 8), '2018-06-08'), (datetime.date(2018, 6, 9), '2018-06-09'), (datetime.date(2018, 6, 10), '2018-06-10'), (datetime.date(2018, 6, 11), '2018-06-11'), (datetime.date(2018, 6, 12), '2018-06-12')])),
                ('appointment_time', models.TimeField(choices=[(datetime.time(8, 0), '08:00:00'), (datetime.time(8, 30), '08:30:00'), (datetime.time(9, 0), '09:00:00'), (datetime.time(9, 30), '09:30:00'), (datetime.time(10, 0), '10:00:00'), (datetime.time(10, 30), '10:30:00'), (datetime.time(11, 0), '11:00:00'), (datetime.time(11, 30), '11:30:00'), (datetime.time(12, 0), '12:00:00'), (datetime.time(12, 30), '12:30:00'), (datetime.time(13, 0), '13:00:00'), (datetime.time(13, 30), '13:30:00'), (datetime.time(14, 0), '14:00:00'), (datetime.time(14, 30), '14:30:00'), (datetime.time(15, 0), '15:00:00'), (datetime.time(15, 30), '15:30:00'), (datetime.time(16, 0), '16:00:00'), (datetime.time(16, 30), '16:30:00'), (datetime.time(17, 0), '17:00:00')])),
                ('visit_reason', models.CharField(max_length=150)),
                ('doctor', models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
            ],
            options={
                'verbose_name': 'appointment',
                'verbose_name_plural': 'appointments',
                'ordering': ('appointment_date',),
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.CharField(choices=[('y', 'yes'), ('n', 'no')], max_length=1)),
                ('prescribed', models.CharField(max_length=150)),
                ('record_date', models.DateTimeField(auto_now=True)),
                ('visit_record', models.TextField()),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Appointment')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('sex', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=1)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DC', 'District of Columbia'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2)),
                ('zip', models.CharField(max_length=5)),
                ('email', models.EmailField(max_length=254)),
                ('day_phone', models.CharField(max_length=10)),
                ('evening_phone', models.CharField(max_length=10)),
                ('insurance', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('Room_no', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('available', models.CharField(choices=[('y', 'yes'), ('n', 'no')], max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.Patient'),
        ),
        migrations.AddField(
            model_name='admit',
            name='Room_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='records.Rooms'),
        ),
        migrations.AddField(
            model_name='admit',
            name='patient_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='records.Patient'),
        ),
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('appointment_date', 'appointment_time')},
        ),
    ]

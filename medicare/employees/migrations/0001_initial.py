# Generated by Django 2.0.2 on 2018-02-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('type_label', models.CharField(choices=[('DO', 'Doctor'), ('RE', 'Receptionist'), ('NU', 'Nurse'), ('PH', 'Pharmacist'), ('LA', 'Lab Technician')], max_length=200)),
                ('speciality_label', models.CharField(max_length=200)),
            ],
        ),
    ]
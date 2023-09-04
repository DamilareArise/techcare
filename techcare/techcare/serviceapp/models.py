from django.db import models
from django.contrib.auth.models import User
from techcare.userapp.models import Profile
from django.utils import timezone
# Create your models here.

class General():
    dept = [
        ("Emergency Care","Emergency Care"),
        ("Ambulance service", "Ambulance service"),
        ("Medicine & Pharmacy", "Medicine & Pharmacy"),
        ("Operation & Surgery", "Operation & Surgery"),
        ("Blood Testing", "Blood Testing"),
        ("Outdoor Checkup", "Outdoor Checkup"),
        ("General Health", "General Health"),
        ("Cardiology", "Cardiology"),
        ("Dental", "Dental"),
        ("Neurology", "Neurology"),
        ("Orthopaedics", "Orthopaedics"),
    ]

    user_status =[
        ('unknown','unknown'),
        ('Booked for test','Booked for test'),
        ('Transferred','Transferred'),
        ('Admitted', 'Admitted'),
        ('Discharged','Discharged'),
        ('Dead','Dead'),
    ]

class Service(models.Model):
    gen = General()
    service_id = models.AutoField(primary_key=True)
    service_option = models.CharField(choices=gen.dept, max_length=20, null=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    HoD = models.OneToOneField(User, on_delete=models.CASCADE, unique= True)
    service_logo = models.ImageField(upload_to='service_logo/', blank=True, null=True, unique=False)
    price = models.BigIntegerField(unique=False)
    description = models.CharField(max_length=300, blank=True, null=True)


class BookingService(models.Model):
        gen = General()
        
        booking_id = models.AutoField(primary_key=True)
        user = models.ForeignKey(User, null=False, blank=False, unique=False, on_delete=models.CASCADE)
        hod = models.ForeignKey(User, related_name="hod", null=False, blank=False, unique=False, on_delete=models.CASCADE, default=1)
        service = models.ForeignKey(Service, null=False, blank=False, unique=False, on_delete=models.CASCADE)
        service_name = models.CharField(max_length=100, blank=True, null=True, unique=False)
        date_created = models.DateField(auto_now_add=True)
        consultant_doctor = models.ForeignKey(User, related_name="consultant_doctor", null=False, unique=False, on_delete=models.CASCADE, default=1)
        resident_doctor = models.ForeignKey(User, related_name="resident_doctor", null=False, unique=False, on_delete=models.CASCADE, default=1)
        approved_date = models.DateField(null=True, blank=True, unique=False)
        approved_time = models.TimeField(null=True, blank=True, unique=False)
        description = models.CharField(max_length=300, blank=True, null=True)
        payment = models.BooleanField(default=False, blank=True, null=True, unique=False)
        served = models.BooleanField(default=False, blank=True, null=True, unique=False)
        patient_status = models.CharField(choices=gen.user_status, max_length=20, unique=False, null=True)
        doctor_remark = models.CharField(max_length=100, blank=True, null=True, unique=False)
        price = models.BigIntegerField(unique=False, default=00)

class PatientMedicalHistory(models.Model):
    gen = General()
        
    report_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=False, blank=False, unique=False, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=False, blank=False, unique=False, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    approved_doctor = models.ForeignKey(User, related_name="approved_doctor", null=False, unique=False, on_delete=models.CASCADE, default=1)
    next_approved_date = models.DateField(null=True, blank=True, unique=False)
    next_approved_time = models.TimeField(null=True, blank=True, unique=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    doctor_remark = models.CharField(max_length=100, blank=True, null=True, unique=False)
    service_name = models.CharField(max_length=100, blank=True, null=True, unique=False)
    patient_status = models.CharField(choices=gen.user_status, max_length=20, unique=False, null=True)

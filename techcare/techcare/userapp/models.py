from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    countries = [
        ("Nigeria", "Nigeria"),
        ("United Kingdom", "United Kingdom"),
        ("USA","USA")
    ] 

    states = [
        ("Oyo", "Oyo"),
        ("Abia", "Abia"),
        ("Ekiti", "Ekiti"),
        ("Abuja","Abuja"),
    ] 

    position = [
        ("CMD","CMD"),
        ("CMAC","CMAC"),
        ("HOD", "HOD"),
        ("HR", "HR"),
        ("Accountant", "Accountant"),
        ("Admin", "Admin"),
        ("Consultant", "Consultant"),
        ("Resident Doctor", "Resident Doctor"),
        ("Clerical Staff", "Clerical Staff"),
        ("Pharmacist","Pharmacist"),
        ("Medical Lab Scientist", "Medical Lab Scientist"),
        ("Scientific Oficer","Scientific Oficer")
    ]

    dept = [
        ("Emergency", "Emergency"),
        ("Operation & Surgery", "Operation & Surgery"),
        ("Outdoor Checkup", "Outdoor Checkup"),
        ("Ambulance Service", "Ambulance Service"),
        ("Medicine & Pharmacy", "Medicine & Pharmacy"),
        ("Medical Lab","Medical Lab")
    ]

    ma_status = [
        ("Single", "Single"),
        ("Married", "Married"),
        ("Engaged", "Engaged"),
        ("Divorced","Divorced")
    ]

    blood_g = [
        ("A+", "A+"),
        ("B+", "B+"),
        ("O+", "O+"),
        ("A-", "A-"),
        ("B-", "B-"),
        ("O-", "O-"),
        ("AB", "AB"),

    ]


    profile_id = models.AutoField(primary_key=True)  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(unique=False, max_length=20, null=True)
    address = models.CharField(unique=False, max_length=100, null=True)
    phone = models.CharField(unique=False, max_length=11, null=True)
    date_of_birth = models.CharField(unique=False, max_length=11, null=True)
    gender = models.CharField(unique=False, max_length=11, null=True)
    nationality = models.CharField(choices=countries, unique=False, max_length=50, null=True)
    state = models.CharField(choices=states, unique=False, max_length=20, null=True)
    department = models.CharField(choices=dept, unique=False, max_length=30, null=True)
    blood_group = models.CharField(choices=blood_g, unique=False, max_length=20, null=True)
    means_of_identity = models.ImageField(upload_to ='identityImage/', unique=False,  null=True)
    particulars = models.FileField(upload_to ='particularsImage/', unique=False, null=True)
    profile_passport = models.ImageField(upload_to ='profileImage/', unique=False, null=True,)
    position = models.CharField(choices=position, unique=False, max_length=25, null=True)
    marital_status = models.CharField(choices=ma_status, unique=False, max_length=25, null=True)
    staff = models.BooleanField(default=False, unique=False, null=False)
    next_of_kin = models.CharField(unique=False, max_length=20, null=True)


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()



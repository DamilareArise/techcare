from django import forms
from django.contrib.auth.models import User
from techcare.userapp.models import Profile
from .models import Service, BookingService, PatientMedicalHistory

class Service_form(forms.ModelForm):
    list_HOD = []
    for hod in Profile.objects.all().filter(position='HOD'):
        list_HOD.append((hod.user_id, hod.user.first_name + " " + hod.user.last_name + " (" + hod.department +")"))

    service_logo = forms.FileField(required=False)
    HoD = forms.ChoiceField(choices=list_HOD, required=True)
    description = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Service
        fields = [
            'service_option',
            'HoD',
            'service_logo',
            'price',
            'description'
        ]


class BooksService_form(forms.ModelForm):
  
    class Meta:
        model = BookingService
        fields = [
            'description',
        ]
        
        widgets = {
            "description": forms.Textarea(attrs={'cols':60, 'row': 3}),
        }     


class AcceptableBooks_forms(forms.ModelForm):

    class Meta:
        model = BookingService
        fields=[
            'description',
            'approved_date',
            'approved_time',
            'doctor_remark',
        ]

        widgets = {
            'approved_date': forms.NumberInput(attrs={'type':'date'}),
            'approved_time': forms.NumberInput(attrs={'type':'time'}),
            'description': forms.Textarea(attrs={'cols': 60, 'row': 3}),
            'doctor_remark': forms.Textarea(attrs={'cols': 60, 'row': 3}),
        }


class EditBookingService_form(forms.ModelForm):
    list_resident = [("", "---------------")]
    list_consultant = [("", "---------------")]

    for user in User.objects.filter(is_staff=True):
        if user.profile.position =="Resident doctor":
            list_resident.append((user.id, user.first_name + " " + user.last_name + " (" + user.profile.department +")"))
        
        elif user.profile.position =="Consultant":
            list_consultant.append((user.id, user.first_name + " " + user.last_name + " (" + user.profile.department +")"))

    resident_ = forms.ChoiceField(choices=list_resident, required = False) 
    consultant_ = forms.ChoiceField(choices=list_consultant, required = False) 

    class Meta:
        model = BookingService
        fields = [
            'description',
            'consultant_',
            'resident_', 
            'approved_date',
            'approved_time',
            'doctor_remark',
        ]

        widgets = {
            'approved_date': forms.NumberInput(attrs={'type':'date'}),
            'approved_time': forms.NumberInput(attrs={'type':'time'}),
            'description': forms.Textarea(attrs={'cols': 60, 'row': 3}),
            'doctor_remark': forms.Textarea(attrs={'cols': 60, 'row': 3}),
        }


class MedicalReportForm(forms.ModelForm):
    list_service = []
    for service in Service.objects.all():
        list_service.append((service.service_id, service.service_option))

    
    
    service_name = forms.ChoiceField(choices=list_service, required = False) 


    class Meta:
        model = PatientMedicalHistory
        fields = [
            'description',
            'served',
            'next_approved_date',
            'next_approved_time',
            'patient_status',
            'doctor_remark',
        ]

        widgets = {
            'next_approved_date': forms.NumberInput(attrs={'type':'date'}),
            'next_approved_time': forms.NumberInput(attrs={'type':'time'}),
            'description': forms.Textarea(attrs={'cols': 60, 'row': 3}),
            'doctor_remark': forms.Textarea(attrs={'cols': 60, 'row': 3}),
        }

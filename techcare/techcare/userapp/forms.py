from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
        

class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]



class AdminProfile_form(forms.ModelForm):
    gend = [
        ("Male", "Male"),
        ("Female", "Female")    
    ]
    user_status = [
        
        ("Active","Active"),
        ("Resigned","Resigned"),
        ("Retired", "Retired"),
        ("Suspended", "Suspended"),
        ("On leave", "On leave"),
        ("Admitted", "Admitted"),
        ("Retired", "Retired"),
        ("Discharged", "Discharged"),
        ("Dead", "Dead"),
    ]

    profile_passport = forms.ImageField(required=False, label='profile passport')
    means_of_identity = forms.ImageField(required=False, label='Means of identity')
    particulars = forms.FileField(required=False, label='particulars')
    gender = forms.ChoiceField(choices =gend, required=False, widget= forms.RadioSelect)
    status = forms.ChoiceField(choices=user_status, required=False)

    class Meta:
        model = Profile
        fields = [
            'address',
            'phone',
            'date_of_birth',
            'gender',
            'nationality',
            'state',
            'means_of_identity',
            'particulars',
            'profile_passport',
            'position',
            'department',
            'marital_status',
            'blood_group',
            'next_of_kin',
            'status',
            'staff',

        ]

        widgets = {
            'date_of_birth': forms.NumberInput(attrs={'type':'date'}),
        }


class UserProfile_form(forms.ModelForm):
    gend = [
        ("Male", "Male"),
        ("Female", "Female")    
    ]
 

    profile_passport = forms.ImageField(required=False, label='profile passport')
    means_of_identity = forms.ImageField(required=False, label='Means of identity')
    gender = forms.ChoiceField(choices =gend, required=False, widget= forms.RadioSelect)
    

    class Meta:
        model = Profile
        fields = [
            'address',
            'phone',
            'date_of_birth',
            'gender',
            'nationality',
            'state',
            'means_of_identity',
            'profile_passport',
            'marital_status',
            'blood_group',
            'next_of_kin',

        ]

        widgets = {
            'date_of_birth': forms.NumberInput(attrs={'type':'date'}),
        }
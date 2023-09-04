from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import SignUpForm, User_form, AdminProfile_form, UserProfile_form
from .models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponsePermanentRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url  = reverse_lazy("login")
    template_name = 'registration/signup.html'

@login_required
def my_account(request, userid):
    # Profile.objects.only("address", "email").filter(profile_id=userid) #selecting only this columns from the database
    # Profile.objects.exclude("address", "email").filter(profile_id=userid) #selecting all aside the ones selescted
    # Profile.objects.all() #selecting all the details in the database

    profile = Profile.objects.all().filter(user_id=userid)

    return render(request=request, template_name='userapp/my_account.html', context={"userprofile":profile})

def editAdmin_account(request, userid):
    user = get_object_or_404(User, id=userid)
    if request.method == "POST":
        user_form = User_form(request.POST, instance=user)
        admin_profile_form = AdminProfile_form(request.POST or None, request.FILES or None, instance=user.profile)
        if user_form.is_valid() and admin_profile_form.is_valid():
            user_form.save()
            admin_profile_form.save()
            if admin_profile_form.cleaned_data['staff']:
                user.is_staff = True
            else:
                user.is_staff = False
            user.save()
            messages.success(request, 'Your profile was successfully updated!')
            return my_account(request, userid)
        else:
        #     print("invalid invalid")
            messages.error(request, 'Please correct the error below.')
            return HttpResponsePermanentRedirect(reverse('editAdmin_account', args=(userid,)))
    else:
        user_form = User_form(instance=user)
        admin_profile_form = AdminProfile_form(instance=user.profile)

        return render(request, 'userapp/edit_profile_form.html', {'user_form': user_form, 'admin_profile_form': admin_profile_form})

def editUser_account(request, userid):
    user = get_object_or_404(User, id=userid)
    if request.method == "POST":
        user_form = User_form(request.POST, instance=user)
        profile_form = UserProfile_form(request.POST or None, request.FILES or None, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # if profile_form.cleaned_data['staff']:
            #     user.is_staff = True
            # else:
            #     user.is_staff = False
            # user.save()

            messages.success(request, 'Your profile was successfully updated!')
            return my_account(request, userid)
        else:
        #     print("invalid invalid")
            messages.error(request, 'Please correct the error below.')
            return HttpResponsePermanentRedirect(reverse('editUser_account', args=(userid,)))
    else:
        user_form = User_form(instance=user)
        profile_form = UserProfile_form(instance=user.profile)

        return render(request, 'userapp/edit_profile_form.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def deactivate_account(request, userid):
    user = User.objects.get(id = userid)
    if user.is_active:
        User.objects.filter(id = userid).update(is_active = False)
    else:
        User.objects.filter(id = userid).update(is_active = True)

    messages.success(request, 'Deactivation succesfull')
    return HttpResponsePermanentRedirect(reverse("my_account",args=(userid,)))


@login_required
def allUser(request, user):
    if user == 'staff':
       all_user = Profile.objects.filter(staff=True)
    else:
       all_user = Profile.objects.filter(staff=False)

    return render(request,'userapp/display_user.html', {'allUser':all_user, 'users':user})
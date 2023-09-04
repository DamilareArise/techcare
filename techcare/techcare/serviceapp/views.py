from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Service, BookingService, PatientMedicalHistory
from .forms import Service_form, BooksService_form, AcceptableBooks_forms, EditBookingService_form
from techcare.userapp.models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponsePermanentRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.core.mail import send_mail

def homepage_service(request):
    services = Service.objects.all()
    services = services[0:3]
    return render (request, 'index.html', {'services':services})

@login_required
def  displayService(request, display):
    services = Service.objects.all()
    if display ==  'service_user':
        return render (request, 'serviceapp/service.html', {'services':services})
    else:
        return render (request, 'serviceapp/display_service.html', {'services':services})
    
@login_required
def  createService(request):
    if request.method == "POST":
        service_form = Service_form(request.POST, request.FILES )
        if service_form.is_valid():
            service_form.save()
        return displayService(request, 'service_admin')
    else:
        service_form = Service_form()
        return render(request, 'serviceapp/create_service.html', {'serviceForm': service_form})

@login_required
def  editService(request, servid):
    form = get_object_or_404(Service, service_id=servid)
    if request.method == "POST":
        service_form = Service_form(request.POST or None, request.FILES or None, instance=form)
        if service_form.is_valid():
            service_form.save()
            messages.success(request, 'Your Service was successfully updated!')
            return HttpResponsePermanentRedirect(reverse('display_service', args=('service_admin',)))
        else:
            messages.error(request, 'Please correct the error below.')
            return HttpResponsePermanentRedirect(reverse('edit_service', args=(servid,)))
    else:
        service_form = Service_form(instance=form)
        return render(request, 'serviceapp/edit_service_form.html', {'serviceForm': service_form})

@transaction.atomic
@login_required
def serviceDetail(request, servid):
    if request.method == 'POST':
        service_form = BooksService_form(request.POST)
        service = Service.objects.get(service_id = servid)
        if service_form.is_valid():
            form = service_form.save(commit=False)
            form.hod_id = service.HoD_id
            form.user_id = request.user.id
            form.service_id = service.service_id
            form.price = service.price
            form.service_name = service.service_option
            form.save()
 
            send_mail(
            'Booking has been made by a patient',# Subject of the mail
            f'Dear Dr. {service.HoD.first_name}, a patient has booked a service. Please do a proper follow up ', # Body of the mail
            'techcare@gmail.com', # From email (Sender)
            [service.HoD.email], # To email (Receiver)
            fail_silently=False, # Handle any error
            )

            messages.success(request, ('Booking created successfully!'))
            return HttpResponsePermanentRedirect(reverse('service_detail', args=(servid,)))
        else:
            messages.error(request, ('Please correct the error below.'))
            return HttpResponsePermanentRedirect(reverse('service_detail', args=(servid,)))
    else:
        service_detail = Service.objects.filter(service_id=servid)
        service_form = BooksService_form()
        return render(request=request, template_name='serviceapp/service_details.html', context={"service_detail":service_detail, "serviceForm": service_form})

@login_required
def myBooking(request, user):
    booking = BookingService.objects.filter(user_id=user).order_by("approved_date")
    return render(request=request, template_name='serviceapp/my_booking.html', context={"booking_service":booking})

@login_required
def patientBooking(request, user):
    if request.user.profile.position == "CMD":
       my_booking = BookingService.objects.all().order_by('date_created').reverse()

    elif request.user.profile.position == "HOD":
        my_booking = BookingService.objects.filter(service_name=request.user.profile.department).order_by('date_created').reverse()
        
    
    elif request.user.profile.position == "Consultant":
        my_booking = BookingService.objects.filter(consultant_doctor_id=request.user.id, service_name=request.user.profile.department).order_by('date_created').reverse()
    
    elif request.user.profile.position == "Resident":
        my_booking = BookingService.objects.filter(resident_doctor_id=request.user.id, service_name=request.user.profile.department).order_by('date_created').reverse()
    
    return render(request=request, template_name='serviceapp/patient_booking.html', context={"patient_booking":my_booking})


@login_required
def bookingPayment(request, book_id):
    pass

@login_required
def viewBookingDetail(request, book_id):
    my_booking = BookingService.objects.filter(booking_id = book_id)
    return render (request, 'serviceapp/view_booking_details.html', {'my_booking':my_booking})

@login_required
def acceptBooking(request, book_id):
    if request.method == 'POST':
        booking = get_object_or_404(BookingService, booking_id = book_id)
        booking_form = AcceptableBooks_forms(request.POST, instance=booking)
        if booking_form.is_valid():
            patient_email = booking.user.email
            booking_form.save()
            
            #send mail notification to patient
            send_mail(
                'Booking Approval',
                f'Dear {booking.user.first_name}, Your booking has been approved. see your booking details for more information or click <a href= "http://127.0.0.1:8000/serviceapp/view_booking_detail/{booking.user_id}">Booking details</a>.\n Thanks. \n http://127.0.0.1:8000/serviceapp/view_booking_detail/{booking.user_id} ',
                'techcare@gmail.com',
                [patient_email],
                fail_silently=False,
            )


            #send confirmation mail to HOD
            send_mail(
                'Your refered patient was accepted',
                f'Dear HOD, Dr. {booking.consultant_doctor.first_name}, accepted your the patient named {booking.user.first_name} you refer to him or her . Thanks',
                'techcare@gmail.com',
                [booking.hod.email],
                fail_silently=False,
            )

            messages.success(request, ('Boking edited successfully'))
            return HttpResponsePermanentRedirect(reverse('view_booking_detail', args=(book_id,)))
        else:
            messages.error(request, ('Please coorect the error below'))
            return HttpResponsePermanentRedirect(reverse('edit_booking', args=(book_id,)))
        
    else:
        booking = get_object_or_404(BookingService, booking_id = book_id)
        booking_form = AcceptableBooks_forms(instance=booking)
        return render (request, 'serviceapp/edit_booking_service_form.html', {'booking_form':booking_form})
    
@login_required
def referBooking (request, book_id):
    if request.method == 'POST':
        booking = get_object_or_404(BookingService, booking_id = book_id)
        booking_form = EditBookingService_form(request.POST, instance=booking)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            if booking_form.cleaned_data["resident_"]:
                email = booking.resident_doctor.email
                booking.resident_doctor_id = booking_form.cleaned_data['resident_']
            else:
                email = booking.consultant_doctor.email
                booking.resident_doctor_id = booking_form.cleaned_data['consultant_']

            booking.save()

            #send confirmation mail to HOD
            send_mail(
                'Your refered patient was accepted',
                f'Dear, Dr. {booking.user.first_name}, a patient booking has been refered to you. please accepted and fix an appointment. Thanks',
                'techcare@gmail.com',
                [email],
                fail_silently=False,
            )

            messages.success(request, ('Booking edited successfully'))
            return HttpResponsePermanentRedirect(reverse('view_booking_detail', args=(book_id,)))
        else:
            messages.error(request, ('Please coorect the error below'))
            return HttpResponsePermanentRedirect(reverse('edit_booking', args=(book_id,)))
        
    else:
        booking = get_object_or_404(BookingService, booking_id = book_id)
        booking_form = EditBookingService_form(instance=booking)
        return render (request, 'serviceapp/edit_booking_service_form.html', {'booking_form':booking_form})

@login_required
def declineBooking (request, book_id):
    pass

@login_required
def medicalHistory(request, user):
    medical_history = PatientMedicalHistory.objects.filter(user_id = user)
    
    return render (request, 'serviceapp/medical_history.html', {'medical_history':medical_history, 'user_id':user})

@login_required
def medicalReport(request):
    pass
from django.urls import re_path
from techcare.serviceapp import views as service_views


urlpatterns = [
    
    re_path(r'^create_service/',service_views.createService, name='create_service'),
    re_path(r'^display_service/(?P<display>\w+)/',service_views.displayService, name='display_service'),
    re_path(r'^edit_service/(?P<servid>\d+)/',service_views.editService, name='edit_service'),
    re_path(r'^service_detail/(?P<servid>\d+)/',service_views.serviceDetail, name='service_detail'),
    re_path(r'^my_booking/(?P<user>\d+)/', service_views.myBooking, name='my_booking'),
    re_path(r'^patient_booking/(?P<user>\d+)/', service_views.patientBooking, name='patient_booking'),
    re_path(r'^view_booking_detail/(?P<book_id>\d+)/', service_views.viewBookingDetail, name='view_booking_detail'),
    re_path(r'^accept_booking/(?P<book_id>\d+)/', service_views.acceptBooking, name='accept_booking'),
    re_path(r'^refer_booking/(?P<book_id>\d+)/', service_views.referBooking, name='refer_booking'),
    re_path(r'^decline_booking/(?P<book_id>\d+)/', service_views.declineBooking, name='decline_booking'),
    re_path(r'^medical_history/(?P<user>\d+)/', service_views.medicalHistory, name='medical_history'),
    re_path(r'^medical_report/(?P<user>\d+)/', service_views.medicalReport, name='medical_report'),

]

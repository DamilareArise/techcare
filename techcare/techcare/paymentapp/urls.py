from django.urls import re_path
from techcare.paymentapp import views as payment_views


urlpatterns = [

    re_path(r'^book_payment/(?P<book_id>\d+)/', payment_views.bookingPayment, name='book_payment'),
    re_path(r'^payment_success/(?P<book_id>\d+)/', payment_views.successPayment, name='payment_success'),
    re_path(r'^payment_fail/(?P<book_id>\d+)/', payment_views.failPayment, name='payment_fail'),

]
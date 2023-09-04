from django.urls import re_path
from techcare.userapp import views as user_views

urlpatterns = [
    
    re_path(r'^my_account/(?P<userid>\d+)/',user_views.my_account, name='my_account'),
    re_path(r'^editAmin_account/(?P<userid>\d+)/',user_views.editAdmin_account, name='editAdmin_account'),
    re_path(r'^editUser_account/(?P<userid>\d+)/',user_views.editUser_account, name='editUser_account'),
    re_path(r'^deactivate_account/(?P<userid>\d+)/',user_views.deactivate_account, name='deactivate_account'),
    re_path(r'^all_staff/(?P<user>\w+)/',user_views.allUser, name='all_staff'),
    re_path(r'^all_patient/(?P<user>\w+)/',user_views.allUser, name='all_patient'),
]
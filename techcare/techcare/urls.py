
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from techcare.userapp.views import SignUpView
from techcare.serviceapp.views import homepage_service
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', homepage_service, name="home"),
    path('doctors/', TemplateView.as_view(template_name='doctors.html'), name="doctors"),
    path('about/', TemplateView.as_view(template_name='about.html'), name="about"),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name="contact"),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/signup/$', SignUpView.as_view(), name="signup"),
    re_path(r'^userapp/', include("techcare.userapp.urls")),
    re_path(r'^serviceapp/', include("techcare.serviceapp.urls")),
    re_path(r'^paymentapp/', include("techcare.paymentapp.urls")),

    
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
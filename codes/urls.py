from django.urls import path, include
from . import views

app_name = 'codes'

urlpatterns = [
    path('', views.ValidatePhone.as_view(), name='verify_code'),
    path('resend-otp/', views.Resend.as_view(), name='resendotp')
]

from django.urls import path
from .views import *

urlpatterns = [
    path('',register, name = 'register'),
    path('login', login_user, name = 'login'),
    path('otp',otp,name = "otp"),
]

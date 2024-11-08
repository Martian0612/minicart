from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Profile
import random
from accounts.helpers import *

# Create your views here.
def register(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        # resending the otp
        if request.POST.GET('resend'):
            otp = generate_otp()
            send_otp_to_number(mobile,otp)

        user_email = User.objects.filter(email= email).first()
        print('user_name is ', user_email)
        user_number = Profile.objects.filter(mobile = mobile).first()
        print('user_mobile is ', user_number)

        otp = generate_otp()
        if user_email or user_number:      
            user = User(first_name= name, email = email)
            send_otp_to_number(mobile, otp)
            request.session['mobile'] = mobile
            print("verified profile is ", verify_otp(otp))

            if verify_otp(otp):
                profile = Profile(user = user, mobile = mobile, otp = otp)
                profile.save()
            print('User created successfully.')
            context = {messages: 'Account created successfully!', 'alert':'success'}
            return render(request,'register.html',context)

        else:
            
            if user_email is None:
                context = {messages:'Email already exist!', 'alert':'danger'}
                print('User already exist.')
                return render(request,'register.html',context)

            if user_number is None:
                context = {messages:'Phone number already exist!', 'alert':'danger'}
                print('User already exist.')
                return render(request,'register.html',context)

    return render(request,'register.html')

def login_user(request):
    if request.method == "POST":
        mobile = request.POST['mobile']
        otp = generate_otp()
        send_otp_to_number(mobile,otp)
        verify_otp(otp)
        # login()
    return render(request,'login.html')

def otp(request):
    return render(request,'otp.html')
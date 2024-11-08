import http.client
from django.shortcuts import render, redirect
from django.conf import settings
import random


def generate_otp():
    otp = str(random.randint(1000,9999))
    return otp

def send_otp_to_number(mobile, otp):
    conn = http.client.HTTPSConnection("api.msg91.com")
    headers = {'content-type' : 'application/json'}
    authkey = settings.AUTH_KEY
    url = "https://control.msg91.com/api/sendotp.php?otp="+otp+'&sender=abc&message='+'Your otp is '+otp +'&mobile='+mobile+'&authkey='+ authkey+'&country=+91'

    conn.request("GET",url, headers = headers)
    res = conn.getresponse()
    data = res.read()
    print("data is ", data)
    return None


def verify_otp(request,otp):
    otp_typed = request.otp
    mobile = request.session['mobile']
    context = {'mobile':mobile}
    if otp_typed == otp:
        return True
    else:
        context = {'mobile':mobile, 'messages':'Wrong OTP!'}
    return render(request,'otp.html',context)
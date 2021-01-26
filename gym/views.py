from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login


# Create your views here.
def about(request):
    return render(request,'About.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    error=""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username =u , password=p)
    
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d={'error':error}
    return render(request,'login.html',d)

def index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')


def logout_admin(request): 
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

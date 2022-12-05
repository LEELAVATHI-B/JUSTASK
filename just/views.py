from django.shortcuts import render,redirect
from .models import registration
# Create your views here.
import pandas as pd


def index(request):
    return render(request,"just/Justask.html")


def just(request):
    return render(request,"just/index.html")



def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        try:
            details=registration.objects.get(username=username)
            if details.password==password:
                return render(request,'just/category.html')# to be changed
            else:
                return redirect('/login')

        except:
            return redirect('/login')
    else:
        return render(request,"just/login.html")



def register(request):
    if request.method=="POST":
        fullname=request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        dob = request.POST.get('dob')
        city = request.POST.get('city')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        user=registration(username=username,fullname=fullname,email=email,phone_number=phone_number,Date_of_birth=dob,location=city,password=password,gender=gender)
        user.save()
        return redirect('/login')
    else:
        return render(request,"just/register.html")


def budget(request):
    df=pd.read_csv('just/static/just/data/leek 2.csv')
    json = df.to_json()
    return render(request,"just/bug.html",{'data':json})


def idea(request):
    df = pd.read_csv('just/static/just/data/leek 2.csv')
    json = df.to_json()
    return render(request,"just/idea.html",{'data':json})
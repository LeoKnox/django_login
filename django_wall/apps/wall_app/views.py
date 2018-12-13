from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User

def index(request):
    return render(request, "wall_app/index.html")
# Create your views here.

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hpwd = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name=request.POST["fname"],last_name=request.POST["lname"],password=hpwd,email=request.POST["email"])
        request.session['use'] = request.POST["fname"]
        return redirect("/welcome")

def login(request):
    errors = User.objects.pw_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        return redirect("/welcome")

def welcome(request):
    return render(request, "wall_app/welcome.html")
    
def show(request):
    print(User.objects.all().values())
    return redirect("/")

def delete(request):
    c=User.objects.all()
    c.delete()
    print(User.objects.all().values())
    return redirect("/")
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import About, Cards
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, "home.html")


def about(request):
    dict_Abt = {
        'abt': About.objects.all()
    }
    return render(request, "about.html", dict_Abt)


def file(request):
    dict_card = {
        'card': Cards.objects.all()
    }
    return render(request, "file.html", dict_card)


def contact(request):
    if request.method == 'POST':
        uname = request.POST['name']
        pass1 = request.POST['pswd']

        user = authenticate(request, username=uname, password=pass1)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Login!..")
            return redirect('contact')


        else:
            messages.error(request, "Invalid Username and Password")
            return redirect('contact')
            # return HttpResponse("<h1>Invalid Username and Password</h1>")

    return render(request, "contact.html")


def sign(request):
    if request.method == 'POST':
        uname = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pswd1']
        pass2 = request.POST['pswd2']

        if pass1 != pass2:
            return HttpResponse("<h1>Your password is incorrect</h1>")

        else:
            myuser = User.objects.create_user(username=uname, email=email, password=pass1)
            myuser.save()
            return redirect('contact')

    return render(request, 'signup.html')

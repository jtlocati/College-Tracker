from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


#Builder Versions
"""def login_view(request):
    return render(request, "Tracker/login.html", {})

def createaccount(request):
    return render(request, "Tracker/createaccount.html", {})"""

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = user.authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, "Tracker/login.html")
            return redirect("Tracker:home")
        else:
            return render(request, "Tracker/login.html", {
                "error": "invalid username or password."
            })
    return render(request, "Tracker/login.html", {})

def createaccount(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("Tracker:home")
        return render(request, "Tracker/createaccount.html",{
            "form": form
        })
    form = UserCreationForm()
    return render(request, "Tracker/createaccount.html", {
        "form": form
    })

def logout_view(request):
    auth_logout(request)
    return redirect("Tracker:login")

@login_required
def home(request):
    return render(request, "Tracker/home.html")
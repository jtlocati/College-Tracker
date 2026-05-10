from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, "Tracker/login.html", {})

def createaccount(request):
    return render(request, "Tracker/createaccount.html", {})

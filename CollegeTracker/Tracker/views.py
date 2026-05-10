from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import userprofile
from .forms import UserProfileForm, APScoreFormSet
from openai import OpenAI
import os
import time

def get_profile_data(profile):
    """Pull every field off a userprofile into a flat dict for easy access."""
    return {
        # Geographic
        "state": profile.State,
        "city": profile.City,
        "school": profile.School,

        # GPA
        "overall_gpa_uw": profile.OverallGPAUW,
        "overall_gpa_w": profile.OverallGPAW,
        "fresh_gpa_uw": profile.FreshGPAUW,
        "fresh_gpa_w": profile.FreshGPAU,
        "soph_gpa_uw": profile.SophGPAUW,
        "soph_gpa_w": profile.SophGPAW,
        "jun_gpa_uw": profile.JunGPAUW,
        "jun_gpa_w": profile.JunGPAW,
        "sen_gpa_uw": profile.SenGPAUW,
        "sen_gpa_w": profile.SenGPAW,

        # Standardized tests
        "sat": profile.SAT,
        "act": profile.ACT,

        # AP scores (list of APScore instances)
        "ap_scores": list(profile.ap_scores.all()),

        # Activities
        "activity1": profile.Activity1,
        "description1": profile.Description1,
        "activity2": profile.Activity2,
        "description2": profile.Description2,
        "activity3": profile.Activity3,
        "description3": profile.Description3,
        "activity4": profile.Activity4,
        "description4": profile.Description4,
        "activity5": profile.Activity5,
        "description5": profile.Description5,
        "activity6": profile.Activity6,
        "description6": profile.Description6,
        "activity7": profile.Activity7,
        "description7": profile.Description7,
        "activity8": profile.Activity8,
        "description8": profile.Description8,
        "activity9": profile.Activity9,
        "description9": profile.Description9,
        "activity10": profile.Activity10,
        "description10": profile.Description10,

        # Awards
        "award1": profile.Award1,
        "award2": profile.Award2,
        "award3": profile.Award3,
        "award4": profile.Award4,
        "award5": profile.Award5,

        # Letters of rec
        "teacher1": profile.Teacher1,
        "teacher2": profile.Teacher2,
        "teacher3": profile.Teacher3,
        "teacher4": profile.Teacher4,

        "note": profile.note,
        "pref_area": profile.pref_area,
        "major": profile.major
    }

def ping_ai(prompt):
    client = OpenAI(api_key=os.getenv("openAPIKEY"))

    Responce = client.responses.create(
        model="gpt-5",
        input= prompt
    )

    return Responce.output_text


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("Tracker:home")
        else:
            return render(request, "Tracker/login.html", {
                "error": "Invalid username or password."
            })
    return render(request, "Tracker/login.html", {})


def createaccount(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            # Send new users straight to their (empty) profile to fill in.
            return redirect("Tracker:UserProfile")
        return render(request, "Tracker/createaccount.html", {"form": form})
    form = UserCreationForm()
    return render(request, "Tracker/createaccount.html", {"form": form})


def logout_view(request):
    auth_logout(request)
    return redirect("Tracker:login_view")


@login_required
def home(request):
    return render(request, "Tracker/home.html")


@login_required
def UserProfile(request):
    # Get-or-create makes the profile object lazily — first visit creates an
    # empty row tied to the logged-in user; subsequent visits load it.
    profile, _ = userprofile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        formset = APScoreFormSet(request.POST, instance=profile)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect("Tracker:WelcomeUser")
    else:
        form = UserProfileForm(instance=profile)
        formset = APScoreFormSet(instance=profile)

    return render(request, "Tracker/UserProfile.html", {
        "form": form,
        "formset": formset,
    })

@login_required
def WelcomeUser(request):
    profile = request.user.profile
    data = get_profile_data(profile)
    #pull important info for anaysis
    state = data["state"]
    sat = data["sat"]
    act = data["sat"]
    note = data["note"]
    pref_area = data["pref_area"]
    activites_list = []
    award_list = []
    major = data["major"]

    for i in range(10):
        i=i+1
        activites_list.append(data[f"activity{i}"])
    
    for i in range(5):
        i = i+1
        award_list.append(data[f"award{i}"])

    Accepto_Responce = ping_ai(f"I need you to introduce yourself as an AI bot name 'Accepto' that is here to make the user feel confident you being able to find good coleges for them to apply to, given their information: sat: {sat}, act: {act}, activitys: {activites_list}, awards{award_list}, state: {state}, background: {note}, intended major: {major} and preffered area for a new college: {pref_area}. You must give them a 2 sentance summary about themselfs, making them fell confident. Aslo include 1-2 prospective schools. <=400 chars. end on a 'lets get started!' note")

    
    return render(request, "Tracker/WelcomeUser.html", {
        "Accepto_Responce": Accepto_Responce
    })


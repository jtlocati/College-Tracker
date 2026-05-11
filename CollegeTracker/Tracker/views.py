from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import userprofile
from .forms import UserProfileForm, APScoreFormSet
from openai import OpenAI
import os
from datetime import date

from .models import Colleges

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

def GetStats(request):
    profile = request.user.profile
    data = get_profile_data(profile)

    Activities_list = []
    Award_list = []
    Letter_list = []

    for i in range(10):
        i = i+1
        Activities_list.append(data[f"activity{i}"])
        Activities_list.append(data[f"description{i}"])
    
    for i in range(5):
        i = i+1
        Award_list.append(data[f"award{i}"])

    for i in range(4):
        i = i+1
        Letter_list.append(data[f"teacher{i}"])

    Stats = f"State: {data['state']}, city: {data['city']}, school: {data['school']}\
                    College type: {data['pref_area']}, major: {data['major']} \
                    Overall GPA(UW): {data['overall_gpa_uw']}, Overall GPA(W): {data['overall_gpa_w']}\
                    Freshman GPA(UW): {data['fresh_gpa_uw']}, Freshman GPA(W): {data['fresh_gpa_w']}\
                    Sphmore GPA UW/W: {data['soph_gpa_uw']}/{data['soph_gpa_w']}\
                    Junior GPA UW/W: {data['jun_gpa_uw']}/{data['jun_gpa_w']}\
                    Senior GPA UW/W: {data['sen_gpa_uw']}/{data['sen_gpa_w']}\
                    AP testing ([<Score1: Test1>, <Score2: test2>, ect]): \
                    {list(data['ap_scores'])} \
                    SAT: {data['sat']}, ACT: {data['act']} \
                    Activitys('Activity1' , 'Description1' , 'Activity2' , 'Description2' ,ect...):\
                    {Activities_list} \
                    Awards( 'Award1' , 'Award2' , 'Award3' ,ect...): \
                    {Award_list} \
                    Letters of reccomendation( 'Letter1' , 'Letter2' , 'Letter3', ect..)\
                    {Letter_list} \
                    Additional information: {data['note']}"
    return Stats
    

def split_college_data(colleges):
    schools = []

    for entry in colleges.strip().rstrip(";").split(";"):
        # Clean Data
        entry = entry.strip()
        if ":" not in entry:
            continue

        name, rest = entry.split(":", 1)
        parts = [p.strip() for p in rest.split(",")]
        if len(parts) < 5:
            continue

        teir = parts[0].lower()
        deadline = parts[1]
        likleyhood = parts[-1]
        url = parts[-2]
        major= ", ".join(parts[2:-2])

        # fix misspelling
        if teir == "saftey":
            teir = "safety"

        schools.append({
            "school_name": name.strip(),
            "tier": teir,
            "deadline_type": deadline,
            "major": major,
            "portal_url": url,
            "likelihood": likleyhood,
        })

    return schools 



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
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "delete":
            Colleges.objects.filter(user=request.user, id=request.POST.get("id")).delete()

        elif action == "reset":
            Colleges.objects.filter(user=request.user).delete()

        elif action == "update":
            school = Colleges.objects.filter(user=request.user, id=request.POST.get("id")).first()
            if school:
                if "deadline_type" in request.POST:
                    school.deadline_type = request.POST["deadline_type"]
                if "deadline" in request.POST:
                    school.deadline = request.POST["deadline"] or None
                if "Satus" in request.POST:
                    school.Satus = request.POST["Satus"]
                if "notes" in request.POST:
                    school.notes = request.POST["notes"]
                school.save()

        qs = request.META.get("QUERY_STRING", "")
        return redirect(f"{request.path}?{qs}" if qs else request.path)

    schools_qs = Colleges.objects.filter(user=request.user)

    active_tier = request.GET.get("tier", "all")
    if active_tier in {"reach", "match", "safety"}:
        schools_qs = schools_qs.filter(Tier=active_tier)

    active_status = request.GET.get("status", "any")
    if active_status == "decided":
        schools_qs = schools_qs.filter(Satus__in=["accepted", "rejected", "waitlisted", "deferred"])
    elif active_status != "any":
        schools_qs = schools_qs.filter(Satus=active_status)


    AllowedSorts = {"school_name", "-school_name", "Tier", "-Tier", "deadline_type", "-deadline_type", "deadline", "-deadline", "Satus", "-Satus"}

    sort = request.GET.get("sort", "school_name")

    if sort in AllowedSorts:
        schools_qs = schools_qs.order_by(sort)

    #compute Next deadline
    today = date.today()
    schools = []

    for cool in schools_qs:
        if cool.deadline:
            days_left = (cool.deadline - today).days
        else:
            days_left = None
        schools.append({"obj": cool, "days_left": days_left})

    return render(request, "Tracker/home.html", {
        "schools": schools,
        "active_tier": active_tier,
        "active_status": active_status,
        "current_sort": sort,
        "plan_choices": ["EA", "ED", "ED1", "ED2", "REA", "Reg", "Rolling"],
        "status_choices": Colleges.StatusOptions,
    })

        

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

@login_required
def Accepto_Reccomend(request):
    profile = request.user.profile
    data = get_profile_data(profile)

    Stats = GetStats(request)

    Schools = ping_ai(f"Given the following information I need you to generate a list of 10 reach, 10 match, and 5 safety schools for the person with the following profile, be honest, you are making serious career reccomendations, not making the person feel good/confident. i need you to put your responces in the format of: School1:reach/match/saftey,submission deadline(EA,ED,Reg,ect. Baised off of profile), major, school application url, likleyhood of admitance;School2:reach/match/saftey,submission deadline(EA,ED,Reg,ect. Baised off of profile), major, school application url, likleyhood of admitance;... DO NOT DEVIATE FROM THE FORMAT  Here are the stats: \
                      {Stats}")
    
    parsed = split_college_data(Schools)

    # Wipe this user's previous Accepto picks so they don't pile up on every regen.
    Colleges.objects.filter(user=request.user).delete()

    for s in parsed:
        Colleges.objects.create(
            user=request.user,
            school_name=s["school_name"],
            Tier=s["tier"],
            Satus="notstarted",
            deadline_type=s["deadline_type"],
            major=s["major"],
            portal_url=s["portal_url"],
            likelihood=s["likelihood"],
        )

    # Hand off to the home view so it loads the freshly-saved schools with
    # all the filter/sort context home.html expects.
    return redirect("Tracker:home")
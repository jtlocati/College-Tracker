
from django.urls import path
from . import views

app_name = "Tracker"

urlpatterns = [
    path("", views.login_view, name="login_view"),
    path("createaccount/", views.createaccount, name="createaccount"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.home, name="home"),
    path("UserProfile/", views.UserProfile, name="UserProfile"),
    path("WelcomeUser/", views.WelcomeUser, name="WelcomeUser"),
    path("accepto_schools", views.Accepto_Reccomend, name="AcceptoReccomend"),
    path("addschool/", views.AddSchool, name="AddSchool"),
    path("schoolsummary/<int:school_id>/", views.schoolsummary, name="schoolsummary"),
    path("api/college-search/", views.college_search_api, name="college_search_api"),
    path("edit-profile/", views.EditProfile, name="EditProfile"),
    path("update-colleges/", views.UpdateColleges, name="UpdateColleges"),
]
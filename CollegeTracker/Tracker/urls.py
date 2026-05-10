
from django.urls import path
from . import views

app_name = "Tracker"

urlpatterns = [
    path("", views.login_view, name="login_view"),
    path("createaccount/", views.createaccount, name="createaccount"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.home, name="home")

]
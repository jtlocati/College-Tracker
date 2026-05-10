
from django.urls import path
from . import views

app_name = "Tracker"

urlpatterns = [
    path("", views.login, name="login"),
    path("createaccount/", views.createaccount, name="createaccount"),

]
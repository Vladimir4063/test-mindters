from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.


def home(request):
    title = "Hello Word"
    return render(request, "home.html")


def signup(request):
    if request.method == "GET":
        print("Load forms")
        return render(request, "signup.html", {"forms": UserCreationForm})

    else:
        if request.POST["password1"] == request.POST["password2"]:
            # Register User
            print(request.POST["username"])
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"]
                )
                user.save()
                print("Send forms")
                login(request, user)
                return redirect("tasks")
                # return render(request, "tasks.html")
            except IntegrityError:
                return render(
                    request,
                    "signup.html",
                    {"forms": UserCreationForm, "error": "User already exists"},
                )
                # return HttpResponse('User already exists')
        return render(
            request,
            "signup.html",
            {"forms": UserCreationForm, "error": "Password do not match"},
        )


def tasks(request):
    return render(request, "tasks.html")

def signout(request):
    logout(request)
    return redirect("home")

def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})
    else:
        print(request.POST)
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )

        if user is None:
            print("NO ENTRA")
            return render(request, "signin.html", {"form": AuthenticationForm, "error":"Username or password is incorrect"})
        else:
            login(request, user)
            return redirect('tasks')

        # return render(request, "signin.html", {"form": AuthenticationForm})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    username = "some_user" # request.POST["username"]
    password = "some_password" # request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        print("User logged in")
        return redirect("/")
    else:
        # return an 'invalid login' error message.
        print("Invalid login")

    return render(request, "auth/login.html", {})
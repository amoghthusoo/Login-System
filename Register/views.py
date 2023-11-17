from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(request):

    return render(request, "index.html")
    

def signup(request):
    
    if(request.method == "POST"):
        
        username = request.POST["username"]
        password = request.POST["password"]

        if(User.objects.filter(username = username).exists()):
            messages.info(request, "Username not available!")
            return redirect("signup.html")
        else:
            user = User.objects.create_user(username = username, password = password)
            user.save()
            return redirect("login.html")
    else:
        return render(request, "signup.html")

def login(request):

    if(request.method == "POST"):
        
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username = username, password = password)

        if(user is not None):
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials!")
            return redirect("login.html")
        
    else:
        return render(request, "login.html")
    
def logout(request):
    auth.logout(request)
    return redirect("/")
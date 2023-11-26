from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

from Friends.friends_lib import Database

# Create your views here.

def index(request):

    return render(request, "index.html")
    

def signup(request):
    
    if(request.method == "POST"):
        
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if(len(username) == 0 or len(password) == 0 or len(confirm_password) == 0):
            messages.info(request, "Please Enter all the details!")
            return redirect("signup")

        print(password, confirm_password)

        if(password != confirm_password):
            messages.info(request, "Passwords do not match!")
            return redirect("signup")

        elif(User.objects.filter(username = username).exists()):
            messages.info(request, "Username not available!")
            return redirect("signup")
        else:
            user = User.objects.create_user(username = username, password = password)
            user.save()
            return redirect("login")
    else:
        return render(request, "signup.html")

def login(request):

    database = Database()

    if(request.method == "POST"):
        
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username = username, password = password)

        if(user is not None):
            auth.login(request, user)

            # creating tables for friend list and request list

            if(not database.if_table_friends_exists(username)):    
                database.create_table_friends(username)
    
            if(not database.if_table_requests_exists(username)):
                database.create_table_requests(username)


            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials!")
            return redirect("login")
        
    else:
        return render(request, "login.html")
    
def logout(request):
    auth.logout(request)
    return redirect("/")

def delete_account(request):
    
    if(request.method == "POST"):

        password = request.POST["password"]
        user = auth.authenticate(username = request.user, password = password)

        if(user is not None):
            request.user.delete()
            return redirect("/")
        else:
            messages.info(request, "Incorrect Password!")
            return redirect("delete_account")
    else:
        return render(request, "delete_account.html")
    
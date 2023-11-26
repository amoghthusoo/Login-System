from django.shortcuts import render, redirect
from . import friends_lib
from django.contrib import messages


# Create your views here.

def friends(request):
    
    database = friends_lib.Database()
    friend_list = database.pull_friends(str(request.user))

    return render(request, "friends.html", {"friend_list" : friend_list})

def requests(request):

    database = friends_lib.Database()
    request_list = database.pull_requests(str(request.user))

    return render(request, "requests.html", {"request_list" : request_list})

def send_request(request):

    database = friends_lib.Database()

    if(request.method == "POST"):
        
        username = request.POST["username"]
        
        if(database.if_user_exists(username)):
            
            if(username == str(request.user)):
                messages.info(request, "Can't send request!")
                return redirect("send_request")
            
            elif(database.if_request_already_send(str(request.user), username)):
                messages.info(request, "Friend request already sent!")
                return redirect("send_request")
            
            elif(database.if_already_friends(str(request.user), username)):
                messages.info(request, "You are already friends!")

            else:
                database.send_friend_request(str(request.user), username)
                messages.info(request, "Request sent!")
                return redirect("send_request")

        else:
            messages.info(request, "User not found!")
            return redirect("send_request")

        return redirect("send_request")
    
    else:
        return render(request, "send_request.html")

def remove(request, target):
    
    database = friends_lib.Database()
    user = str(request.user)

    database.remove_friend(user, target)

    return redirect("friends")

def accept(request, source_user):
    
    database = friends_lib.Database()
    destination_user = str(request.user)

    database.make_friends(source_user, destination_user)

    return redirect("requests")

def reject(request, source_user):
    
    database = friends_lib.Database()
    destination_user = str(request.user)
    
    database.reject_friend_request(source_user, destination_user)

    return redirect("requests")

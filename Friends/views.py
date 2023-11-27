from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from . import friends_lib
from django.contrib import messages



# Create your views here.

def friends(request):
    
    database = friends_lib.Database()
    friend_list = database.pull_friends(str(request.user))

    database.close_connection()
    return render(request, "friends.html", {"friend_list" : friend_list})

def requests(request):

    database = friends_lib.Database()
    request_list = database.pull_requests(str(request.user))

    database.close_connection()
    return render(request, "requests.html", {"request_list" : request_list})

def send_request(request):

    database = friends_lib.Database()

    if(request.method == "POST"):
        
        username = request.POST["username"]
        
        if(database.if_user_exists(username)):
            
            if(username == str(request.user)):
                messages.info(request, "Can't send request!")

                database.close_connection()
                return redirect("send_request")
            
            elif(database.if_request_already_send(str(request.user), username)):
                messages.info(request, "Friend request already sent!")

                database.close_connection()
                return redirect("send_request")
            
            elif(database.if_already_friends(str(request.user), username)):
                messages.info(request, "You are already friends!")

            else:
                database.send_friend_request(str(request.user), username)
                messages.info(request, "Request sent!")

                database.close_connection()
                return redirect("send_request")

        else:
            messages.info(request, "User not found!")

            database.close_connection()
            return redirect("send_request")

        database.close_connection()
        return redirect("send_request")
    
    else:
        database.close_connection()
        return render(request, "send_request.html")

def remove(request, target):
    
    database = friends_lib.Database()
    user = str(request.user)

    database.remove_friend(user, target)

    database.close_connection()
    return redirect("friends")

def accept(request, source_user):
    
    database = friends_lib.Database()
    destination_user = str(request.user)

    database.make_friends(source_user, destination_user)

    database.close_connection()
    return redirect("requests")

def reject(request, source_user):
    
    database = friends_lib.Database()
    destination_user = str(request.user)
    
    database.reject_friend_request(source_user, destination_user)

    database.close_connection()
    return redirect("requests")


def dm(request, source_user, dest_user):
    
    return render(request, "dm.html", {"dest_user" : dest_user})


def get_dms(request):

    database = friends_lib.Database()
    
    source_user = str(request.user)
    dest_user = request.GET["dest_user"]
    
    messages = database.pull_dms(source_user, dest_user)

    database.close_connection()
    return JsonResponse({"messages" : messages})

def put_dm(request):

    database = friends_lib.Database()

    source_user = str(request.user)
    dest_user = request.POST["dest_user"]
    message = request.POST["message"]

    database.push_dm(source_user, dest_user, message)

    database.close_connection()
    return HttpResponse()

def clear_chat(request, dest_user):

    database = friends_lib.Database()
    source_user = str(request.user)
    
    database.clear_chat(source_user, dest_user)
    
    database.close_connection()
    return redirect(f"/Friends/dm/{source_user}/{dest_user}")
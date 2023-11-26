from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from . import chat_lib

# Create your views here.

def chat(request):
    return render(request, "chat.html")
    
def get_messages(request):
    
    database = chat_lib.Database()
    
    message_list = database.pull()
    messages = [message[0] for message in message_list]

    return JsonResponse({"messages" : messages})

def put_message(request):
    
    database = chat_lib.Database()
    
    message = request.POST["message"]
    if(len(message) > 0):
        message = str(request.user) + " : " + message
        database.push(message)

    return HttpResponse()

def clear(request):
    
    database = chat_lib.Database()
    database.clear_chat()
    return redirect("chat")


# "amoghthusoo.mysql.pythonanywhere-services.com", "amoghthusoo", "<kivymd.>", "amoghthusoo$login_system"
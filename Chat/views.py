from django.shortcuts import render, redirect
from django.http import JsonResponse
from . import chat_lib

# Create your views here.

def chat(request):

    if(request.method == "POST"):

        database = chat_lib.Database()
        message = request.POST["message"]
        
        if(len(message) > 0):
            message = str(request.user) + " : " + message
            database.push(message)

        # record_list = database.pull()
        # messages = [message[0] for message in record_list]
        
        return render(request, "chat.html")
    
    else:
        
        # record_list = database.pull()
        # messages = [message[0] for message in record_list]
        return render(request, "chat.html")
    
def get_messages(request):
    
    database = chat_lib.Database()
    
    message_list = database.pull()
    messages = [message[0] for message in message_list]

    return JsonResponse({"messages" : messages})
        
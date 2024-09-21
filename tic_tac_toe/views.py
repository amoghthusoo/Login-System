from django.shortcuts import render
from django.http import JsonResponse
import mysql.connector as mc


# Create your views here.

# host = "localhost"
# user = "root"
# password = "root"
# database = "tic_tac_toe"

init = None
buffer_X = None
buffer_O = None


def synchronize(request, data):
    global init

    if(data == "_"):
        # hdl = mc.connect(host = host, user = user, password = password, database = database, autocommit = True)
        # crs = hdl.cursor()
        # crs.execute("select value from config where _key = 'init';")
        # for row in crs:
        #     val = row[0]
        #     break
        
        # if(val != None):
        #     crs.execute(f"update config set value = null where _key = 'init';")
        
        # crs.close()


        val = init
        if(val != None):
            init = None

        return JsonResponse({"val" : val})

    else:
        # hdl = mc.connect(host = host, user = user, password = password, database = database, autocommit = True)
        # crs = hdl.cursor()
        # crs.execute(f"update config set value = '{data}' where _key = 'init';")
        # crs.close()

        init = data
        return JsonResponse({})
    

def get_X(request):
    # hdl = mc.connect(host = host, user = user, password = password, database = database, autocommit = True)
    # crs = hdl.cursor()
    # crs.execute("select value from config where _key = 'buffer_X';")
    # for row in crs:
    #     val = row[0]
    #     break
    # crs.execute("update config set value = null where _key = 'buffer_X'")
    # crs.close()
    
    global buffer_X
    val = buffer_X
    buffer_X = None
    return JsonResponse({"val" : val})


def get_O(request):
    # hdl = mc.connect(host = host, user = user, password = password, database = database, autocommit = True)
    # crs = hdl.cursor()
    # crs.execute("select value from config where _key = 'buffer_O';")
    # for row in crs:
    #     val = row[0]
    #     break
    # crs.execute("update config set value = null where _key = 'buffer_O'")
    # crs.close()
    
    global buffer_O
    val = buffer_O
    buffer_O = None
    return JsonResponse({"val" : val})


def put_X(request, data):
    # hdl = mc.connect(host = host, user = user, password = password, database = database, autocommit = True)
    # crs = hdl.cursor()
    # crs.execute(f"update config set value = '{data}' where _key = 'buffer_X';") 
    # crs.close()
    
    global buffer_X
    buffer_X = data
    return JsonResponse({})

def put_O(request, data):
    # hdl = mc.connect(host = host, user = user, password = password, database = database, autocommit = True)
    # crs = hdl.cursor()
    # crs.execute(f"update config set value = '{data}' where _key = 'buffer_O';")
    # crs.close()
    
    global buffer_O
    buffer_O = data
    return JsonResponse({})

def reset(reset):
    
    global init
    global buffer_O
    global buffer_X

    init = None
    buffer_X = None
    buffer_O = None
    
    return JsonResponse({})
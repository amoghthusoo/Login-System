from django.shortcuts import render, redirect
from django.contrib import messages
from . import sgpa_lib


# Create your views here.

def calculate_save(request):

    if (request.method == "POST"):

        sgpa = sgpa_lib.SGPA()
        database = sgpa_lib.Database()

        try:
            course_code = request.POST["course_code"]

            semester = int(request.POST["semester"])

            credits = request.POST["credits"]
            credit_list = credits.split(",")
            credit_list = [int(credit) for credit in credit_list]

            marks = request.POST["marks"]
            marks_list = marks.split(",")
            marks_list = [int(marks) for marks in marks_list]

            sgpa = sgpa.calculate(credit_list, marks_list)
            database.push(request.user, semester,
                          course_code, credits, marks, sgpa)

            database.close_connection()
            return render(request, "sgpa_save.html")

        except:
            messages.info(request, "Invalid Data!")

            database.close_connection()
            return render(request, "sgpa_save.html")

    else:
        database.close_connection()
        return render(request, "sgpa_save.html")


def records(request):

    database = sgpa_lib.Database()

    record_list = database.pull(request.user)

    keys = ["record_list", "semester", "course_code", "credits", "marks", "sgpa"] 
    records = []

    for row in record_list:
        records.append(dict(zip(keys, row)))

    database.close_connection()
    return render(request, "records.html", {"records" : records})

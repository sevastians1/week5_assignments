from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import School # import our School class

my_school = School("Django School") # create a school instance
my_object={"clicker_counter": 0, }

def index(request):
    my_data = { 
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    data={"my_school": my_school}
    return render(request, "pages/list_staff.html", data)


def staff_detail(request, employee_id):
    data={"staff": my_school.find_staff_by_id(employee_id)}
    return render(request, "pages/staff_details.html", data)


def list_students(request):
    data={"my_school": my_school}
    return render(request, "pages/list_students.html", data)


def student_detail(request):
    print(request.POST)
    my_id=int(request.POST['student_id'])
    data={"student": my_school.find_student_by_id(my_id)}
    return render(request, "pages/student_details.html", data)

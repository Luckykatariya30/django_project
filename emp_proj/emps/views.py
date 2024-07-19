from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Role
from datetime import datetime
from django.db.models import Q

# Create your views here.


def home(request):
    return render(request, 'home.html')


def all_emps(request):
    emps = Employee.objects.all()
    context = {
        "emps": emps
    }
    return render(request, "all_emps.html", context)


def add_emp(request):
    if request.method == "POST":
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        dept = int(request.POST["dept"])
        role = int(request.POST["role"])
        phone = int(request.POST["phone"])
        salary = int(request.POST["salary"])
        employee = Employee(fname=first_name, lname=last_name, dept_id=dept,
                            role_id=role, salary=salary, phone=phone, hire_date=datetime.now())
        employee.save()
        return HttpResponse("employee added succeses....!")
    elif request.method == "GET":
        return render(request, "add_emp.html")
    else:
        return HttpResponse("This employee details in error occured ....!")


def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(fname__icontains = name ) | Q(lname__icontains = name))
        if dept:
            emps = emps.filter(dept__name = dept)
        if role:
            emps = emps.filter(role__name = role)
        context = {
            'emps':emps
        }
        return render(request, "all_emps.html" , context)
    elif request.method == "GET":
        return render(request , "filter_emp.html")
    else:
        return HttpResponse("Wrong fill employee details.......!")



def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_remoce = Employee.objects.get(id=emp_id)
            emp_to_be_remoce.delete()
            return HttpResponse('this employee id removed.....!')
        except:
            return HttpResponse("this employee details are worng ....")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }

    return render(request, "remove_emp.html", context)

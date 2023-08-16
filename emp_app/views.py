from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Role
from django.db.models import Q
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, 'index.html')


def all_emp(request):
    # emps = Employee.objects.all()
    emps = Employee.objects.filter(
        (Q(dept__dept__contains="Developer") & Q(salary__gte="1600000")) |
        Q(dept__dept__contains="HR") & Q(bonous__lte=100000))
    context = {
        'emps': emps
    }

    print(context)

    return render(request, 'all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        salary = int(request.POST['salary'])
        bonous = int(request.POST['bonous'])
        phone = int(request.POST['phone'])
        new_emp = Employee(first_name=first_name, last_name=last_name, dept_id=dept, role_id=role, salary=salary, bonous=bonous, phone=phone,
                           hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee Successfully Added')
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('Exception Raised')


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_remmoved = Employee.objects.get(id=emp_id)
            emp_to_be_remmoved.delete()
            return HttpResponse('Employee Deleted')
        except:
            return HttpResponse('Enter Valid Employee Id')
        else:
            return HttpResponse('Successfully')

    get_employee = Employee.objects.all()
    context = {
        "emp_id": get_employee
    }
    return render(request, 'remove_emp.html', context)


def filter_emp(request):
    return render(request, 'filter_emp.html')

from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def emp_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, 'emp_register/emp_list.html', context)


def emp_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, 'emp_register/emp_form.html', {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('emp_list'))


def emp_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return HttpResponseRedirect(reverse('emp_list'))


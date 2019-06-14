from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from apps.employees.models import Employee
from apps.employees.forms import EmployeeForm


class EmployeeList(ListView):
    model = Employee
    template_name = 'employees_list.html'

    def get_queryset(self):
        current_company = self.request.user.employee.company
        return Employee.objects.filter(company = current_company)
    
class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'departments']

class EmployeeDelete(DeleteView):
    model = Employee
    success_url = reverse_lazy('employees:list')

class EmployeeCreate(CreateView):
    template_name = 'employees/employee_form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('employees:list')

    def form_valid(self, form):
        employee_form = form.save(commit = False)
        employee_form.company = self.request.user.employee.company
        user = User()
        user.username = form.cleaned_data['username'],
        user.first_name = form.cleaned_data['first_name']
        user.password = make_password(form.cleaned_data['first_name'])
        user.save()
        employee_form.user = user
        employee_form.save()
        return super().form_valid(form)

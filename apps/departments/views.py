from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.departments.models import Department


class DepartmentList(ListView):
    model = Department
    template_name = 'departments/department_list.html'

    def get_queryset(self):
        current_company = self.request.user.employee.company
        return Department.objects.filter(company = current_company)

class DepartmentCreate(CreateView):
    model = Department
    fields = ['name', 'company']
    success_url = reverse_lazy('departments:list')

    def form_valid(self, form):
        department_form = form.save(commit = False)
        department_form.company = self.request.user.employee.company
        department_form.save()
        return super().form_valid(form)

class DepartmentUpdate(UpdateView):
    model = Department
    fields = ['name', 'company']

class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('departments:list')

    
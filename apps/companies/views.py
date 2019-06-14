from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from apps.companies.models import Company

class CompanyCreate(CreateView):
    model = Company
    fields = ['name']
    template_name = 'companies/company_form.html'

    def form_valid(self, form):
        company = form.save()
        employee = self.request.user.employee
        employee.company = company
        employee.save()
        return super().form_valid(form)


class CompanyUpdate(UpdateView):
    model = Company
    fields = ['name']
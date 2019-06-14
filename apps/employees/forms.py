from django import forms
from apps.employees.models import Employee
from apps.departments.models import Department

class EmployeeForm(forms.ModelForm):
    name = forms.CharField()
    username = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = Employee
        fields = ['name', 'departments']
       

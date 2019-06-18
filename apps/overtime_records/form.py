from django import forms
from apps.overtime_records.models import OvertimeRecords
from apps.employees.models import Employee

class OvertimeRecordsForm(forms.ModelForm):
    def __init__(self,user, *args, **kwargs):
        super(OvertimeRecordsForm, self).__init__(*args, **kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(company= user.employee.company) 

    class Meta:
        model = OvertimeRecords
        fields = ['reason', 'employee', 'hours']
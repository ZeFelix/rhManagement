from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from apps.overtime_records.models import OvertimeRecords
from apps.overtime_records.form import OvertimeRecordsForm

class OvertimeRecordsList(ListView):
    model = OvertimeRecords
    template_name = 'overtime_records/overtime_records_list.html'

    def get_queryset(self):
        current_company = self.request.user.employee.company
        return OvertimeRecords.objects.filter(employee__company = current_company)


class OvertimeRecordsUpdate(UpdateView):
    model = OvertimeRecords
    form_class = OvertimeRecordsForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs

class OvertimeRecordsDelete(DeleteView):
    model = OvertimeRecords
    success_url = reverse_lazy('overtime_records:list')

class OvertimeRecordsCreate(CreateView):
    model = OvertimeRecords
    form_class = OvertimeRecordsForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs
    


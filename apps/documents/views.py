from django.shortcuts import render
from django.views.generic import CreateView
from apps.documents.models import Document

class DocumentCreate(CreateView):
    model = Document
    fields = ['description','file']
    template_name = 'documents/document_form.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.employee_id = self.kwargs['pk']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



from django.db import models
from django.urls import reverse
from apps.employees.models import Employee


class Document(models.Model):
    description = models.CharField(max_length=100, help_text=('description of the document'))
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    file = models.FileField(upload_to="files", max_length=100)

    def get_absolute_url(self):
        return reverse("employees:update", kwargs={"pk": self.employee.pk})
    
    
    def __str__(self):
        return self.description
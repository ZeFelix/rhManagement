from django.db import models
from apps.employees.models import Employee


class Document(models.Model):
    description = models.CharField(max_length=100, help_text=('description of the document'))
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self):
        return self.description
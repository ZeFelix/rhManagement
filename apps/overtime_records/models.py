from django.db import models
from apps.employees.models import Employee


class OvertimeRecords(models.Model):
    reason = models.CharField(max_length=70)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self):
        return self.reason


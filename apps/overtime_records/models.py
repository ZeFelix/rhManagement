from django.db import models
from django.urls import reverse
from apps.employees.models import Employee


class OvertimeRecords(models.Model):
    reason = models.CharField(max_length=70)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    hours = models.DecimalField(max_digits=5, decimal_places=2)

    def get_absolute_url(self):
        return reverse("overtime_records:update", kwargs={"pk": self.pk})

    def __str__(self):
        return self.reason


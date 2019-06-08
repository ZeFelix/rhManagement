from django.db import models


class OvertimeRecords(models.Model):
    reason = models.CharField(max_length=70)

    def __str__(self):
        return self.reason


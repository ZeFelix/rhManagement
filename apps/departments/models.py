from django.db import models


class Departament(models.Model):
    name = models.CharField(max_length=70, help_text = 'Departament name')

    def __str__(self):
        return self.name

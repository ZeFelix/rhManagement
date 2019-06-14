from django.db import models
from django.urls import reverse
from apps.companies.models import Company


class Department(models.Model):
    name = models.CharField(max_length=70, help_text = 'Department name')
    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("departments:list")
    
    def __str__(self):
        return self.name

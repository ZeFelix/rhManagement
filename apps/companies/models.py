from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=100, help_text = "Company Name")

    def get_absolute_url(self):
        return reverse("companies:company_update", kwargs={"pk": self.pk})
        
    def __str__(self):
        return self.name

    

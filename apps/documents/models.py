from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=100, help_text=('description of the document'))

    def __str__(self):
        return self.description
from django.urls import path
from apps.documents.views import DocumentCreate


app_name = 'documents'

urlpatterns = [
    path('new/employee/<int:pk>',DocumentCreate.as_view(), name='new'),
]

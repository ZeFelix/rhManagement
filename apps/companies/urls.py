from django.urls import path
from apps.companies.views import CompanyCreate, CompanyUpdate

app_name = 'companies'

urlpatterns = [
    path('new', CompanyCreate.as_view(), name = 'company_create'),
    path('<int:pk>/update', CompanyUpdate.as_view(), name = 'company_update'),
]

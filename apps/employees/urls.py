from django.urls import path
from apps.employees.views import EmployeeList, EmployeeUpdate, EmployeeDelete, EmployeeCreate

app_name = 'employees'

urlpatterns = [
    path('', EmployeeList.as_view(), name = 'list'),
    path('new', EmployeeCreate.as_view(), name = 'new'),
    path('<int:pk>', EmployeeDelete.as_view(), name = 'delete'),
    path('<int:pk>/update', EmployeeUpdate.as_view(), name = 'update')
]
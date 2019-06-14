from django.urls import path
from apps.departments.views import DepartmentList, DepartmentCreate, DepartmentUpdate, DepartmentDelete

app_name = 'departments'

urlpatterns = [
    path('', DepartmentList.as_view(), name = 'list'),
    path('new', DepartmentCreate.as_view(), name = 'new'),
    path('<int:pk>', DepartmentDelete.as_view(), name = 'delete'),
    path('<int:pk>', DepartmentUpdate.as_view(), name = 'update'),
]
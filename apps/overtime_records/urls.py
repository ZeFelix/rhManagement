from django.urls import path
from apps.overtime_records.views import (
    OvertimeRecordsList, OvertimeRecordsUpdate, 
    OvertimeRecordsDelete, OvertimeRecordsCreate)

app_name = 'overtime_records'

urlpatterns = [
    path('', OvertimeRecordsList.as_view(), name = 'list'),
    path('new', OvertimeRecordsCreate.as_view(), name = 'new'),
    path('<int:pk>', OvertimeRecordsDelete.as_view(), name = 'delete'),
    path('<int:pk>/update', OvertimeRecordsUpdate.as_view(), name = 'update')
]
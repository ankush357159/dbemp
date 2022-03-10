from django.urls import path
from app.views import createEmployee, listEmployees, updateEmployee, deleteEmployee, employeeDetails

urlpatterns= [
    path("create/",createEmployee, name="create_employee"),
    path("list/",listEmployees, name="list_employee"),
    path("update/<str:pk>/",updateEmployee, name="update_employee"),
    path("details/<str:pk>/",employeeDetails, name="details_employee"),
    path("delete/<str:pk>/",deleteEmployee, name="delete_employee"),
]
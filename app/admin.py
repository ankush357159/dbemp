from django.contrib import admin
from app.models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        "id", "first_name", "last_name", "email", "employee_id", "address", "department"
        ]
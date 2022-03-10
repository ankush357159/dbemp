from django.db import models
import uuid

class Employee(models.Model):   
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    employee_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.first_name)


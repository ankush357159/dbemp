from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from app.serializers import EmployeeSerializer
from app.models import Employee
from rest_framework.response import Response


# Create Employee
@api_view(['POST'])
def createEmployee(request, *args,**kwargs):        
    employee = Employee.objects.create(
            first_name = request.data["first_name"],
            last_name = request.data["last_name"],
            department = request.data["department"],
            email = request.data["email"],
            address = request.data["address"]
        )
    employee.save()
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)


# Get list of employees
@api_view(['GET'])
def listEmployees(request):
    employee = Employee.objects.all().order_by("-id")
    serializer = EmployeeSerializer(employee, many=True)
    return Response(serializer.data)


# Update employees
@api_view(['PUT'])
def updateEmployee(request, pk):
    employee = Employee.objects.get(id=pk)
    data = request.data

    employee.first_name = data["first_name"]
    employee.last_name = data["last_name"]
    employee.department = data["department"]
    employee.email = data["email"]
    employee.address = data["address"]

    employee.save()
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)

# Get details of a employee
@api_view(['GET'])
def employeeDetails(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)


# Delete Employee
@api_view(['DELETE'])
def deleteEmployee(request, pk):    
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return Response("Employee deleted successfully")


        

        
    



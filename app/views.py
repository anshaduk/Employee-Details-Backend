from django.shortcuts import render
from . models import Employee
from . serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class RegisterEmployeeView(APIView):
    def post(self,request):
        print(request.data,"data")
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            employee=serializer.save()
            print(employee.id,"idddd")
            print(serializer.validated_data['first_name'])
            return Response({"message":"Employee Registered successfully!","id":employee.id },status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):
    def get(self,request,pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"error":"Employee not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"error":"Employee not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(employee,data=request.data,partial=True)
        if serializer.is_valid():
            employee=serializer.save()
            return Response({"message":"Employee updated successfully", "data":serializer.data, "id":employee.id})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


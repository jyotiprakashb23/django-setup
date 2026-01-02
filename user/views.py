from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Person
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  rest_framework import status

# Create your views here.

@api_view(['POST'])
def create_user(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    phone_number = request.data.get('phone_number')
    address = request.data.get('address')
    print(first_name, last_name, email, phone_number, address)

    if not all([first_name, last_name, phone_number]):
        return Response({"error": "first_name, last_name, and phone_number are required."}, status=status.HTTP_400_BAD_REQUEST)
    person = Person.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        phone_number=phone_number,
        address=address
    )
    return Response({"message": "User created successfully", "user_id": person.id}, status=status.HTTP_201_CREATED)

# LOGIN API FOR USER    
# @api_view(['POST'])
# def login_user(request):
#     phone_number = request.data.get('phone_number')
#     password = request.data.get('password')

#     if not all([phone_number, password]):
#         return Response({"error": "phone_number and password are required."}, status=status.HTTP_400_BAD_REQUEST)
    
#     try:
#         user = User.objects.get(phone_number=phone_number, password=password)
#         return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
#     except User.DoesNotExist:
#         return Response({"error": "Invalid phone number or password"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_all_users(request):
    users = Person.objects.all()
    user_data = [
        {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone_number": user.phone_number,
            "address": user.address
        }
        for user in users
    ]
    return Response(user_data, status=status.HTTP_200_OK)

def home(request):
    return HttpResponse("<h1>Welcome to USER app !</h1>")
# def get_all_users(request):
#     return HttpResponse("<h2>List of all users</h2>")



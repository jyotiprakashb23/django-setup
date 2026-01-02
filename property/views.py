# property/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Property
from .serializers import PropertySerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='post', request_body=PropertySerializer, responses={201: PropertySerializer})
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_property(request):
    serializer = PropertySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def test(request):
    return Response({"message": "Test endpoint is working!"}, status=status.HTTP_200_OK)
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import AllowAny, IsAuthenticated 

@api_view(['GET']) 
@permission_classes([AllowAny]) 
def public_view(request): 
    return Response({"message": "This is a public endpoint"}) 
@api_view(['GET']) 
@permission_classes([IsAuthenticated]) 
def protected_view(request): 
    return Response({"message": f"Hello {request.user.username}, this is a protected endpoint"}) 

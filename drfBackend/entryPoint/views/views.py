from django.shortcuts import render
# Create your views here.

# DRF
# https://www.django-rest-framework.org/api-guide/views/#api_view
# https://www.django-rest-framework.org/api-guide/authentication/

from rest_framework.decorators import api_view
from rest_framework.response import Response

# https://www.django-rest-framework.org/api-guide/permissions/
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_from_database(request):
    return Response({"message": "Hello, world!"})
from django.shortcuts import render
from django.core.exceptions import ValidationError

# Create your views here.

# DRF
# https://www.django-rest-framework.org/api-guide/views/#api_view
# https://www.django-rest-framework.org/api-guide/authentication/

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializer import clientReqSerializer
from ..models import AnswerAndKeywords

# https://www.django-rest-framework.org/api-guide/permissions/
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_keywordsAnswer_from_postgres(request):
    try:
        print(request)
        print("get_keywordsAnswer_from_postgres function called")
        # Assuming you want to retrieve all records from the AnswerAndKeywords model
        dataFromDatavase = AnswerAndKeywords.objects.all()
        hibikiSerializer = clientReqSerializer(dataFromDatavase, many=True)
        return Response(hibikiSerializer.data, status=status.HTTP_200_OK)
    

        
    except ValidationError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e: 
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # return Response({"message": "Hello, world!"})
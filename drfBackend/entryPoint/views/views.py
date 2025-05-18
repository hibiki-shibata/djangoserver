from django.shortcuts import render
from django.core.exceptions import ValidationError

# Create your views here.

# DRF
# https://www.django-rest-framework.org/api-guide/views/#api_view
# https://www.django-rest-framework.org/api-guide/authentication/

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from ..serializers.serializer import clientGetReqSerializer, serverResSerializer
from ..models import AnswerAndKeywords

# https://www.django-rest-framework.org/api-guide/permissions/
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated

    

class answerAndKeywordsViewSet(APIView):    

    def get(self, request):
        try:
            print(request)
            print("GET_keywordsAnswer_from_postgres function called")
            # Assuming you want to retrieve all records from the AnswerAndKeywords model
            dataFromDatavase = AnswerAndKeywords.objects.all()
            hibikiSerializer = clientGetReqSerializer(dataFromDatavase, many=True)
            return Response(hibikiSerializer.data, status=status.HTTP_200_OK)
        
            
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e: 
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    def post(self, request):
        try:
            print(request)
            print("POST_keywordsAnswer_from_postgres function called")

            postReqSerializer = serverResSerializer(data=request.data)
            if postReqSerializer.is_valid():
                postReqSerializer.save()
                # return Response(postReqSerializer.data, status=status.HTTP_201_CREATED)
                return Response("Post data were successfully saved", status=status.HTTP_201_CREATED)
            else:
                return Response(postReqSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e: 
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

    def delete(self, request):
        try:
            print(request)
            print("DELETE_keywordsAnswer_from_postgres function called")

            line_to_delete = request.data.get('id')
            if line_to_delete is None:
                return Response({"error": "ID to be deleted is not provided"}, status=status.HTTP_400_BAD_REQUEST)

            deleted = AnswerAndKeywords.objects.filter(id=line_to_delete).delete()
            if deleted[0] == 0:
                return Response({"error": "No record found to delete"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"message": "Record deleted successfully"}, status=status.HTTP_200_OK)

            
            
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e: 
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        






############ Original Code ############

# # @permission_classes([IsAuthenticated])
# @api_view(['GET'])
# def get_keywordsAnswer_from_postgres(request):
#     try:
#         print(request)
#         print("GET_keywordsAnswer_from_postgres function called")
#         # Assuming you want to retrieve all records from the AnswerAndKeywords model
#         dataFromDatavase = AnswerAndKeywords.objects.all()
#         hibikiSerializer = clientGetReqSerializer(dataFromDatavase, many=True)
#         return Response(hibikiSerializer.data, status=status.HTTP_200_OK)
    

        
#     except ValidationError as e:
#         return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e: 
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#         # return Response({"message": "Hello, world!"})



# @api_view(['POST'])
# def post_keywordsAnswer_from_postgres(request):
#     try:
#         print(request)
#         print("POST_keywordsAnswer_from_postgres function called")

#         postReqSerializer = serverResSerializer(data=request.data)
#         if postReqSerializer.is_valid():
#             postReqSerializer.save()
#             # return Response(postReqSerializer.data, status=status.HTTP_201_CREATED)
#             return Response("Post data were successfully saved", status=status.HTTP_201_CREATED)
#         else:
#             return Response(postReqSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
#     except ValidationError as e:
#         return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e: 
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#         # return Response({"message": "Hello, world!"})



# @api_view(['DELETE'])
# def delete_keywordsAnswer_from_postgres(request):
#     try:
#         print(request)
#         print("DELETE_keywordsAnswer_from_postgres function called")

#         line_to_delete = request.data.get('id')
#         if line_to_delete is None:
#             return Response({"error": "ID to be deleted is not provided"}, status=status.HTTP_400_BAD_REQUEST)

#         deleted = AnswerAndKeywords.objects.filter(id=line_to_delete).delete()
#         if deleted[0] == 0:
#             return Response({"error": "No record found to delete"}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             return Response({"message": "Record deleted successfully"}, status=status.HTTP_200_OK)

        
        
#     except ValidationError as e:
#         return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e: 
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)     
# https://www.django-rest-framework.org/api-guide/serializers/
# Serializer is basically for REST API, not for GraphQL.

from rest_framework import serializers
from ..models import AnswerAndKeywords

# class clientGetReqSerializer(serializers.Serializer): # This is a basic serializer - full conf = verrvose.
class clientGetReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerAndKeywords
        # fields = '__all__' # Better to avoid not to handle unknow field from clients' req.
        fields = ['id', 'keywords', 'answer', 'timeStamp']
        read_only_fields = ['timeStamp']
    # created = serializers.DateTimeField()



# This is for when client sent POST request to the server.
class serverResSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerAndKeywords
        fields = ['keywords', 'answer']
        # read_only_fields = ['timeStamp']

        
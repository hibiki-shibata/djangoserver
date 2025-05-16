# https://www.django-rest-framework.org/api-guide/serializers/

from rest_framework import serializers
from ..models import AnswerAndKeywords

class clientGetReqSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerAndKeywords
        # fields = '__all__' # Better to avoid not to handle unknow field from clients' req.
        fields = ['id', 'keywords', 'answer', 'timeStamp']
        read_only_fields = ['timeStamp']
    # created = serializers.DateTimeField()


class serverResSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerAndKeywords
        fields = ['keywords', 'answer']
        # read_only_fields = ['timeStamp']
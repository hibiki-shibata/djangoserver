# Doc: https://docs.graphene-python.org/projects/django/en/latest/installation/

import graphene
from graphene_django import DjangoObjectType

from ..models import AnswerAndKeywords


class clientReqQuery(DjangoObjectType):
    class Meta:
        model = AnswerAndKeywords
        fields = ('id', 'keywords', 'answer', 'timeStamp')

        


class Query(graphene.ObjectType):
    all_keywordsAnswer = graphene.List(clientReqQuery) #Graphene automatically converts field names to camelCase by default... so they will understnad it as "allKeywordsAnswer"
    keywordsAnswer = graphene.Field(clientReqQuery, id=graphene.Int())

    def resolve_all_keywordsAnswer(self, info):
        return AnswerAndKeywords.objects.all()
    
    def resolve_keywordsAnswer(self, info, id):
        try:
            return AnswerAndKeywords.objects.get(id=id)
        except AnswerAndKeywords.DoesNotExist:
            return None
        
# class CreateKeywordsAnswer(graphene.Mutation): 
#     class Arguments:
#         keywords = graphene.List(graphene.String)
#         answer = graphene.String()

#     keywordsAnswer = graphene.Field(clientReqQuery)

#     def mutate(self, info, keywords, answer):
#         keywordsAnswer = AnswerAndKeywords(keywords=keywords, answer=answer)
#         keywordsAnswer.save()
#         return CreateKeywordsAnswer(keywordsAnswer=keywordsAnswer)

schema = graphene.Schema(query=Query)
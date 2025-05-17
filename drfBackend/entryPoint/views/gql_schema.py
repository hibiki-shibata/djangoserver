# Doc: https://docs.graphene-python.org/projects/django/en/latest/installation/

import graphene
from graphene_django import DjangoObjectType

from ..models import AnswerAndKeywords


class clientReqQuery(DjangoObjectType):
    class Meta:
        model = AnswerAndKeywords
        fields = ('id', 'keywords', 'answer', 'timeStamp')




# Because of saving data through Query class is not a good practice
class SaveKeywordsAnswer(graphene.Mutation):        
    class Arguments:
        keywords = graphene.List(graphene.String, required=True)
        answer = graphene.String(required=True)

    keywordsAnswer = graphene.Field(clientReqQuery)

    def mutate(self, info, keywords, answer):
        try:
            keywordsAnswer = AnswerAndKeywords(keywords=keywords, answer=answer)
            keywordsAnswer.save()
            return SaveKeywordsAnswer(keywordsAnswer=keywordsAnswer)
        except Exception as e:
            return None




class Query(graphene.ObjectType):
    all_keywordsAnswer = graphene.List(clientReqQuery) #Graphene automatically converts field names to camelCase by default... so they will understnad it as allKeywordsAnswer"
    keywordsAnswer = graphene.Field(clientReqQuery, id=graphene.Int())
    save_keywordsAnswer = graphene.Field(clientReqQuery, keywords=graphene.List(graphene.String), answer=graphene.String())

    def resolve_all_keywordsAnswer(self, info):
        return AnswerAndKeywords.objects.all()
    
    def resolve_keywordsAnswer(self, info, id):
        try:
            return AnswerAndKeywords.objects.get(id=id)
        except AnswerAndKeywords.DoesNotExist:
            return None
        


class Mutation(graphene.ObjectType):
    save_keywordsAnswer = SaveKeywordsAnswer.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
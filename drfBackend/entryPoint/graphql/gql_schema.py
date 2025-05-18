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

    keywordsAnswer = graphene.Field(clientReqQuery) # This is defining of return type aganst req.

    def mutate(self, info, keywords, answer):
        try:
            savingkeywordsAnswer = AnswerAndKeywords(keywords=keywords, answer=answer)
            savingkeywordsAnswer.save()
            return SaveKeywordsAnswer(savingkeywordsAnswer=savingkeywordsAnswer) # Return to client
        except Exception as e:
            return None


class DeleteKeywordsAnswer(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    keywordsAnswer = graphene.Field(clientReqQuery)
    

    def mutate(self, info, id):
        try:            
            deletingKeyWordsAndAnswer, _ = AnswerAndKeywords.objects.get(id=id)
            deletingKeyWordsAndAnswer.delete() # 
            return DeleteKeywordsAnswer(success=True)
        
        except Exception as e:
            return DeleteKeywordsAnswer(success=False)



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
        

# This is necessary to call the mutation from the client side - suitable for updating data.
class Mutation(graphene.ObjectType):
    save_keywordsAnswer = SaveKeywordsAnswer.Field() # Call Mutation schema.
    delete_keywordsAnswer = DeleteKeywordsAnswer.Field() 

schema = graphene.Schema(query=Query, mutation=Mutation)
from django.urls import path
from .views.views import answerAndKeywordsViewSet

from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .views.gql_schema import schema

urlpatterns = [
    path('restapi', answerAndKeywordsViewSet.as_view(), name='postgres_keywordsAndAswer'),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True,  schema=schema))), #schema = schema.. not necessary bc I already specifed it in settings.py
 
]
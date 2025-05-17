from django.urls import path
from .views.views import get_keywordsAnswer_from_postgres, post_keywordsAnswer_from_postgres, delete_keywordsAnswer_from_postgres

from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .views.gql_schema import schema

urlpatterns = [
    path('getresponse', get_keywordsAnswer_from_postgres, name='get_keywordsAndAswer'),
    path('postresponse', post_keywordsAnswer_from_postgres , name='post_keywordsAndAswer'),
    path('deleteresponse',  delete_keywordsAnswer_from_postgres , name='delete_keywordsAndAswer'),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))), 


]
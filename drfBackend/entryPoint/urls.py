from django.urls import path
from .views.views import get_keywordsAnswer_from_postgres, post_keywordsAnswer_from_postgres, delete_keywordsAnswer_from_postgres

urlpatterns = [
    path('getresponse', get_keywordsAnswer_from_postgres, name='get_keywordsAndAswer'),
    path('postresponse', post_keywordsAnswer_from_postgres , name='post_keywordsAndAswer'),
    path('deleteresponse',  delete_keywordsAnswer_from_postgres , name='delete_keywordsAndAswer')

]
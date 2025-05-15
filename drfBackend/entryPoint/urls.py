from django.urls import path
from .views.views import get_keywordsAnswer_from_postgres

urlpatterns = [
    path('getresponse', get_keywordsAnswer_from_postgres, name='get_keywordsAndAswer')

]
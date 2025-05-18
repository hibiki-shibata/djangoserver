# This task is using celery.
# Doc: https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html

from celery import shared_task
# https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#choosing-a-broker
# import asyncio
import httpx

# from ..models import AnswerAndKeywords


# https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json
@shared_task
def send_request_to_weather_server():
    try:
        with httpx.Client(http1=True, http2=False) as client:
            response = client.get('https://consumer-api.development.dev.woltapi.com/home-assignment-api/v1/venues/home-assignment-venue-helsinki/static')
            print(response.status_code)        
            print(response.text)
            print("RESPONSED LOGGED HIHIHI")


    except Exception as e:
        print(f"Error occurred: {e}")
        
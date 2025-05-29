# This demo task is using celery.
# Doc: https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html

from celery import shared_task
# https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#choosing-a-broker
# import asyncio
import httpx

# from ..models import AnswerAndKeywords


# https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json
@shared_task(
    bind=True, # This is required for use retry feature
    autoretry_for=(Exception,),                    # Retry on any exception
    retry_kwargs={'max_retries': 5},               # Max 5 attempts
    retry_backoff=True                             # Waits 1s, 2s, 4s, 8s, 16s...
)
def send_request_to_weather_server(self):
    try:
        with httpx.Client(http1=True, http2=False) as client:
            response = client.get('https://consumer-api.development.dev.woltapi.com/home-assignment-api/v1/venues/home-assignment-venue-helsinki/static', timeout=5.0)
            print(response.status_code)        
            print(response.text)
            print("RESPONSED LOGGED HIHIHI")


    except Exception as e:
        print(f"Error occurred: {e}")
        

## dev server
`python3 manage.py runserver`

## Dependencies
`pip3 install -r requirements.txt`
`pip3 freeze > requirements.txt`


## Run on production
`gunicorn drfBackend.wsgi:application --bind 0.0.0.0:8000`
In ./drf-server/drfBackend directry

**Don't forget to add model classes and urls classes in each modoleed directlies __init__

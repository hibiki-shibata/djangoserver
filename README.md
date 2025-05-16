
## dev server
`python3 manage.py runserver`

## Dependencies
`pip3 install -r requirements.txt`
`pip3 freeze > requirements.txt`


## Run on production
`gunicorn drfBackend.wsgi:application --bind 0.0.0.0:8000`
In ./drf-server/drfBackend directry

**Don't forget to add model classes and urls classes in each modoleed directlies `__init__`, otherwise it will be impossible to make migration


## Tech Stack
* Django
* djangrestframework (serializer)
* GraphQL
* REST API
* Celery and async.
* Postgres

## -- Tech Concepts--
Cirkitbreaker
Database integrity
Retly
Timeout


## Example test get req:
```
fetch('http://127.0.0.1:8000/random/getresponse') 
    .then(response => 
    response.json()
    .then(data =>
    console.log(data)
    )
    .catch(error  => console.log("Json parce failed:", error))
    )
```

## Database with Postgres official docker image
```
 nerdctl run -p 5432:5432 -d \
    -e POSTGRES_PASSWORD=hibikey \
    -e POSTGRES_USER=hibikiadmin \
    -e POSTGRES_DB=hibikidb \
    -v pgdata:/var/lib/postgresql/data \
    --name dockerPosgtgres \
    postgres
```

-v pgdata > it tellings the database ensure to hold the data, evne after the VM deleted.
nerdctl volume rm pgdata
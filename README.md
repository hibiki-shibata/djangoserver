##
How to start
- `python3 -m venv venv`
- `source ./venv/bin/activate`
- `pip3 install -r requirements.txt`
- `python3 manage.py makemigrations`
- `python3 manage.py makemigrations entryPoint` Read models in entryPoint app
- `python3 manage.py migrate`
- `python3 manage.py migrate --database=HibikiPostgres`
- `python3 manage.py runserver`
Start Postgres server
- `nerdctl pull postgres`
- Check out the container-run command below.



## Run dev server
`python3 manage.py runserver`

## Handle Dependencies
`pip3 install -r requirements.txt`
`pip3 freeze > requirements.txt`


## Run on production
`gunicorn drfBackend.wsgi:application --bind 0.0.0.0:8000 --timeout 30`
In ./drf-server/drfBackend directry

**Don't forget to add model classes and urls classes in each modoleed directlies `__init__`, otherwise it will be impossible to make migration


## --Tech Stack--
* Django - ✅
* djangrestframework (serializer) - ✅
* GraphQL✅ (Only Accept GET & POST )
* REST API - ✅
* Celery and async.
* Postgres - ✅

## -- Tech Concepts--
* Cirkitbreaker
- Database integrity - ✅ 
 - Validation (Data types) ✅
 - @Transaction.Atomic (Prevent partial update, Race condition, Deadlock) 🚫
 - Race condition(.select_for_update()) 🚫
 - Largequery(Separate data) 🚫
* Retly
* Timeout✅
* Authentication
* Unit Test


## Example test get req:
```

function testGetRequest() {
    fetch('http://127.0.0.1:8000/random/getresponse')
        .then(response =>
            response.json()
                .then(data => {
                    console.log(data)
                })

                .catch(error => {
                    console.error('Error parsing JSON:', error);
                }
                )
        )

}


const examplePostRequest = {
    "keywords": ["hibiki", "asfasf", "hibibibi"],
    "answer": 1121312
}


function testPostRequest() {
    fetch('http://127.0.0.1:8000/random/postresponse', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(examplePostRequest)
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}


const exampleDeleteRequest = {
    "idd": "5"
}

function testDeleteRequest() {
    fetch('http://127.0.0.1:8000/random/deleteresponse', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(exampleDeleteRequest)
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}


function testGraphQLRequest() {
    fetch("http://127.0.0.1:8000/random/graphql/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            query: `
      {
        allKeywordsanswer {
          id
          answer
        }
      }
    `
        }),
    })
        .then(async (res) => {
            const data = await res.json();
            if (!res.ok) {
                console.error("GraphQL error response:", data);
            } else {
                console.log("GraphQL success:", JSON.stringify(data, null, 2));
            }
        })
        .catch(err => console.error("Network error:", err));

}

// testPostRequest()
// testDeleteRequest()
// testGetRequest()
testGraphQLRequest()
```

-v pgdata > it tellings the database ensure to hold the data, evne after the VM deleted.
nerdctl volume rm pgdata

Access To database:
`psql -h localhost -p 5432 -U hibikiadmin -d hibikidb`
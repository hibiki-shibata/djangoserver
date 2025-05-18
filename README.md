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
* REST API - (Handle / making req)
 * When a request comes, it will make a request to slack BOT but it through celery, while making sure the data is sent once for sure.
* Celery and async. (Idempotency)
* Postgres - ✅

## -- Tech Concepts--
* Cirkitbreaker🚫 (Handle in infrastructure level)
- Database integrity - ✅ 
 - Validation (Data types) ✅
 - @Transaction.Atomic (Prevent partial update, Race condition, Deadlock)🚫
 - Race condition(.select_for_update()) 🚫
 - Largequery(Separate data) 🚫
* Error handling retly / Idempotency, timeout, Taskqueueing, transaction.on_commit()
* Timeout✅
* Authentication
* Unit Test


## Example test get req:
```
function testGetRequest() {
    fetch('http://127.0.0.1:8000/random/restapi')
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
    fetch('http://127.0.0.1:8000/random/restapi', {
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
    "id": "5"
}

function testDeleteRequest() {
    fetch('http://127.0.0.1:8000/random/restapi', {
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
    fetch("http://127.0.0.1:8000/random/graphql", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            query: `
      {
        keywordsAnswer(id: 9) {
            id
            keywords
            answer
            timeStamp

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


function saveKeywordsAnswer(keywords, answer) {
    fetch("http://127.0.0.1:8000/random/graphql", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            query: `
        mutation saveKeywordsanswer($keywords: [String!]!, $answer: String!) {
          saveKeywordsanswer(keywords: $keywords, answer: $answer) {
            keywordsAnswer {
              id
              keywords
              answer
              timeStamp
            }
          }
        }
      `,
            variables: {
                keywords: keywords,
                answer: answer
            }
        })
    })
        .then(res => res.json())
        .then(data => {
            console.log("Success:", JSON.stringify(data, null, 2));
        })
        .catch(err => {
            console.error("Error:", err);
        });
}





function deleteAnswerById(id) {
    fetch("http://127.0.0.1:8000/random/graphql", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            query: `
        mutation deleteKeywordsanswer($id: Int!) {
          deleteKeywordsanswer(id: $id) {
            success
          }
        }
      `,
            variables: { id: id }
        })
    })
        .then(async (res) =>
            await res.json())
        .then(data => {
            console.log(JSON.stringify(data, null, 2));
        })
        .catch(err => console.error("Network error:", err));
}


testPostRequest()
testDeleteRequest()
testGetRequest()

testGraphQLRequest()
saveKeywordsAnswer(["django", "graphql", "api"], "GraphQL mutation test!");
deleteAnswerById(12);
```

-v pgdata > it tellings the database ensure to hold the data, evne after the VM deleted.
nerdctl volume rm pgdata

Access To database:
`psql -h localhost -p 5432 -U hibikiadmin -d hibikidb`
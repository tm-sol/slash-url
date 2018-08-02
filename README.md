# slash-url
Example URL shortening API in Flask and MongoDB.

# Pre-requisites:
 - Python 3.x
 - MongoDB
 - pip install -r requirements.txt
 - internet connection

# Running
1. Ensure Mongo DB
Prior to running tests or running code a MongoDB instance should be started on your machine.  For example instantiate on windows:
```
"D:\Program Files\MongoDB\Server\3.6\bin\mongod.exe" --dbpath d:\test\mongodb\data
```

2. Run Python Application

```
python app.py
```

3. Use following calls

```
    POST: <APP URL>/shorten_url
    in body:
    {
	    "url":"<URL TO SHORTEN>"
    }

    e.g. http://127.0.0.1:5000/shorten_url
    {
	    "url":"www.google.com"
    }

    returned:
        (if valid) <APP URL>/<CODE> as url
        (if invalid) Error 400 and Error MSG

    GET: <APP URL>/<CODE>
     returned:
        (if valid) 301 and redirect
        (if invalid) Error 400 and Error MSG
```

## Running tests

```
python -m unittest discover -s tests
```

# Discussion
## URL Validation
Validation has been taken to mean leads to a live resource.  A live internet connection is needed.  Many formats are valid urls as the official standard is quite forgiving so makes this test may need more context.  An option to allow users to force a url to be shorted even if not live or valid could be a good compromise here.  If basic formatting checking needed a regex could be used.

# Acknowledgements
## Base62 Encoding
Base62 used to generate part of the url string and sourced from:
https://stackoverflow.com/questions/1119722/base-62-conversion


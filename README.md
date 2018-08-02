[![Build Status](https://travis-ci.com/tm-sol/slash-url.svg?branch=master)](https://travis-ci.com/tm-sol/slash-url)

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
	    "url":"https://www.google.com/search?q=google&client=firefox-b&source=lnms&tbm=isch&sa=X&ved=0ahUKEwifxaaV1c7cAhXI_qQKHUmeAKoQ_AUIDSgE&biw=1360&bih=607#imgrc=UEiT48pdXPdUAM:"
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

## Scaling Application
Current implementation would scale well as MongoDB copes well with large numbers of requests.  However the 'url shortening' can be much improved using a standard RDBS instead of Mongo.  The ID int could then be used to create the Base62 code which would be much shorter and just as quick.

## URL Validation
Validation has been taken to mean leads to a live resource.  A live internet connection is needed.  Many formats are valid urls as the official standard is quite forgiving so makes this test may need more context.  An option to allow users to force a url to be shorted even if not live or valid could be a good compromise here.  If basic formatting checking needed a regex could be used.

# Acknowledgements
## Base62 Encoding
Base62 used to generate part of the url string and sourced from:
https://stackoverflow.com/questions/1119722/base-62-conversion


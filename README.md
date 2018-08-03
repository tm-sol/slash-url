[![Build Status](https://travis-ci.com/tm-sol/slash-url.svg?branch=master)](https://travis-ci.com/tm-sol/slash-url)

# slash-url
Example URL shortening API in Flask and MongoDB using a hash to reduce size of the new url.

# Pre-requisites:
 - Python 3.x
 - MongoDB
 - pip install -r requirements.txt
 - internet connection

# Running
1. Ensure Mongo DB prior to running tests or running code, a MongoDB instance should be started on your machine.  For example, instantiate on windows by:
```
"<PATH>\Server\3.6\bin\mongod.exe" --dbpath <PATH>\data
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
```


```
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
Current architecture would scale very well as MongoDB can be sharded using this technique and it can cope well with large numbers of requests.  Flask can also use a cache to speed up requests.  Various different load balancing techniques and optimising techniques also exist such as asynchronous modules like https://gitlab.com/pgjones/quart but these depend on infrastructure setup.  Setting up *stress tests* to identify bottlenecks on deployment would be useful as part of bigger integration tests.  Flask would need to be hosted in suitable way to ensure efficient request handlin, example guides: https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18.

## URL Validation
Validation has been taken to mean leads to a live resource.  A live internet connection is needed.  Many formats are valid urls as the official standard is quite forgiving so maybe this test may need more context.  An option to allow users to force a url to be shorted even if not live or valid could be a good compromise here.  If basic formatting checking needed a regex could be used.

## Improvements

- *url shortening* can be much improved using a standard RDBS instead of Mongo.  The ID int could then be used to create the Base62 code which would be much shorter. Example of how to code in Base62 here: https://stackoverflow.com/questions/1119722/base-62-conversion.
- Current version does not check for duplicates in the DB.  Checking to see if url was previously encoded would save space.


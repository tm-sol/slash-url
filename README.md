# slash-url
URL shortening


## URL Validation
Validation has been taken to mean leads to a live resource.  Many formats are valid urls as the official standard is quite forgiving so makes this test need more definition.  An option to allow users to force a url to be shorted even if not live or valid could be a good compromise here.  If basic formatting checking needed a regex could be used but there are a lot of edge cases.

## Running tests

```
python -m unittest discover -s tests
```


## Base62 Encoding
Base62 used to generate part of the url string and sourced from:
https://stackoverflow.com/questions/1119722/base-62-conversion

